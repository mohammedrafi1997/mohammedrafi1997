# importing the module
import tweepy
 
# personal details
consumer_key ="vqpSuPgGWlc2VnT3ZYxypYWG7"
consumer_secret ="vZbBzF8CX3zxacsAdoY0rkR2BhpOvFqMocQJtzFrv6e9FDJwdV"
access_token ="984846403233918977-s2FQDfadpa65iKGUvvUXlLWb72KPc4F"
access_token_secret ="vLPpGbxP7WFyED78c1uqEXlz4fBf22YI2OD20W7dtWxLR"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="hello guys")
