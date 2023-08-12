from brickowl.models.wishlists import ExtendedWishlist, WishlistItemList, WishlistList
from .base import APIEndpoint

#from brickowl.models.wishlists import WishlistList

class WishlistMethods(APIEndpoint):

    def __init__(self, api):
        super(WishlistMethods, self).__init__(api, "wishlist")

    def list(self, status=None, wishlistTime=None, limit=None, listType=None):
        url = '{0}/list'.format(self.endpoint)
        #params = {}
        #if status: params['status'] = status
        #if wishlistTime: params['wishlist_time'] = wishlistTime
        #if limit: params['limit'] = limit
        #if listType: params['list_type'] = listType

        status, headers, respJson = self.api.get(url)
        if status in [400, 401, 403, 404, 405, 415, 422]:
            return WishlistList().parseError(respJson)

        return respJson
