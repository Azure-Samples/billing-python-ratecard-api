# Using this package which is a HTTP library
import requests
 
# Parameters need for API
subscription = '<subscriptionId>'
token = '<bearerToken>'
offer = '<offerId>'
currency = 'USD'
locale = 'en-US'
region = 'US'
rateCardUrl = "https://management.azure.com:443/subscriptions/{subscriptionId}/providers/Microsoft.Commerce/RateCard?api-version=2016-08-31-preview&$filter=OfferDurableId eq '{offerId}' and Currency eq '{currencyId}' and Locale eq '{localeId}' and RegionInfo eq '{regionId}'".format(subscriptionId = subscription, offerId = offer, currencyId = currency, localeId = locale, regionId = region)

# Don't allow redirects and call the RateCard API
response = requests.get(rateCardUrl, allow_redirects=False, headers = {'Authorization': 'Bearer %s' %token})

# Look at response headers to get the redirect URL
redirectUrl = response.headers['Location']

# Get the ratecard content by making another call to go the redirect URL
rateCard = requests.get(redirectUrl)

# Print the ratecard content
print(rateCard.content) 