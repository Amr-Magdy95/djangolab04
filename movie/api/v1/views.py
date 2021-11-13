from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from movie.models import Movie
from .serializers import MovieSerializer


@api_view(["GET", "POST"]) # tells django that this is a type of rest view
def hello_world(request):
    if request.method == 'POST':
        return Response(
        {'message': 'Post request-Response'}, status=status.HTTP_201_CREATED)
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def movie_index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_movie(request):
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##CRUD
#C
@api_view(['POST'])
def movie_create(request):
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#R
@api_view(["GET"])
def movie_list(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(instance=movies, many=True)
    return Response(data=serialized_movies.data,status=status.HTTP_200_OK)

@api_view(["GET"])
def single_movie(request, pk):
    try:
        movie  = Movie.objects.get(pk = pk)
    except Exception as e:
        return Response(data={"msg": "this movie does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serialized_movie = MovieSerializer(instance=movie)
    return Response(data=serialized_movie.data,status=status.HTTP_200_OK)


#U
@api_view(["PUT", "PATCH"])
def update_movie(request, pk):
    try:
        movie  = Movie.objects.get(pk = pk)      
    except Exception as e:
        return Response(data={"msg": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serialized_movie = MovieSerializer(instance=movie, data = request.data )
    if serialized_movie.is_valid():
        serialized_movie.save()
        return Response(serialized_movie.data, status=status.HTTP_200_OK)
    return Response(serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)

#D
@api_view(["DELETE"])
def delete_movie(request, pk):
    res = {}
    try:
        movie  = Movie.objects.get(pk = pk)
        movie.delete()
        res['data']= 'Successfully deleted the movie'
        res['status'] = status.HTTP_200_OK
    except Exception as e:
        res['data']= 'Error While Deleting: {}'.format(str(e))
        res['status'] = status.HTTP_400_BAD_REQUEST
    
    return Response(data=res.get('data'), status = res.get('status'))


