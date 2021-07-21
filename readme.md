In this tutorial we setup user authorization and authentication. Authentication
refers to determining the identity of who they are communicating with. Authorization
refers to determining what a user is alowed to do based on who they are. First we
will create a relationship between our note model and the built in django user model.
Then, we will enable 'token authentication'. A token is a randomly generated secret
that we can add to the headers of our requests to prove that we are a certain user.
We will also add an endpoint to get that token by providing a username and password.
With token authentication setup we can add IsAuthenticated permission to our model
viewset.
