from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from app.models import Post, PostLike, PostComment, UserFollow, User
from app.serializer import PostSerializer, PostLikeSerializer, CommentSerializer, UserFollowSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView


class CreatePost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]


class RetrievePost(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response({"success": True, "message": "Post successfully updated", "data": serializer.data})
        else:
            return Response({"success": False, "message": serializer.errors})


class DestroyPost(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            post = Post.objects.get(id=pk)
            if post.user.id == request.user.id:
                self.perform_destroy(post)
                return Response({"success": True, "message": "Post successfully destroyed", "data": request.data})
            else:
                return Response({"success": False, "message": "You do not have permission to delete post"
                                    , "data": request.data})
        except ObjectDoesNotExist:
            return Response({"success": False, "message": "Post does not exist", "data": request.data})


class RetrieveUserPost(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        post_users = Post.objects.filter(user=request.user.id)
        serializer = self.serializer_class(post_users, many=True)
        return Response({"success": True, "data": serializer.data})





class LikePost(APIView):
    authentication_classes = [TokenAuthentication]

    # serializer_class را با LikeSerializer جایگزین کنید (در صورت تعریف)

    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            likes = PostLike.objects.filter(post=post)
            # استفاده از LikeSerializer (در صورت تعریف)
            serializer = PostLikeSerializer(likes, many=True)
            return Response({"success": True, "لایک‌ها": serializer.data})
        except ObjectDoesNotExist:
            return Response({"success": False, "پیام": "پستی با این شناسه یافت نشد."})

    def post(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            like, created = PostLike.objects.get_or_create(user=request.user, post=post)
            if not created:
                like.delete()
                return Response({"success": False, "data": "unLike"})
            else:
                return Response({"success": True, "data": "like"})
        except ObjectDoesNotExist:
            return Response({"success", False})


class CommentPost(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            post = self.get_queryset().get(id=pk)
            comments = PostComment.objects.prefetch_related('user').filter(post=post)
            serializer = CommentSerializer(comments, many=True)
            return Response({"success": True, "data": serializer.data})
        except ObjectDoesNotExist:
            return Response({"success": False, "message": "پستی با این شناسه یافت نشد."})
        except Exception as e:
            # ثبت خطا در لاگ

            return Response({"success": False, "message": "خطایی در بازیابی نظرات رخ داده است.", "exception": e})

    def post(self, request, pk):
        try:
            context = {
                "request": request,
            }
            post = Post.objects.get(id=pk)
            #  request.data["post"] = post
            #  PostComment.objects.create(post=post, user=request.user, comment_text=request.data["comment_text"])
            serializer = self.serializer_class(context=context, data=request.data)
            if serializer.is_valid():
                serializer.save(post=post)
                return Response({"success": True, "message": "comment added"})
            else:
                print(serializer.errors)
                return Response({"success": False, "message": "error adding a comment"})


        except ObjectDoesNotExist:
            return Response({"success": False, "message": "post does not exist"})


class FollowUser(APIView):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        following = UserFollow.objects.filter(user=request.user)
        followers = UserFollow.objects.filter(follows=request.user)

        followers_serializer = UserFollowSerializer(followers, many=True)
        following_serializer = UserFollowSerializer(following, many=True)

        return Response({"success": True,
                         "following": following_serializer.data,
                         "followers": followers_serializer.data
                         })

    def post(self, request, pk):
        try:
            following_user = User.objects.get(id=pk)
            follow_user = UserFollow.objects.get_or_create(user=request.user, follows=following_user)
            if not follow_user[1]:
                follow_user[0].delete()
                return Response({"success": True, "message": "unfollowed user"})
            else:
                return Response({"success": True, "message": "followed user"})

        except User.DoesNotExist:
            return Response({"success": False, "message": "User does not exist"})


