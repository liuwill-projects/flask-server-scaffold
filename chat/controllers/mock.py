from chat.controllers import jsonify
from chat.controllers.base import Controller

class Mock(Controller):

    def getCookie(self):
        return jsonify({"foo":"bar","token":"1492499843375"})

    def me(self):
        return jsonify({
            "_id" : "57ee30ee5ffd454100714c6a",
            "email" : "liuwill@live.com",
            "modified" : "2017-04-17T03:28:40.866Z",
            "created" : "2017-04-17T03:28:40.866Z",
            "adsLeague" : 2,
            "useCytron" : True,
            "deny" : 0,
            "policyAgreed" : True,
            "status" : 2,
            "role" : "admin",
            "__v" : 0,
            "hashedPassword" : "",
            "salt" : "",
            "username" : "liuwei",
            "neverJoinAdsLeague" : True,
            "phone" : "15808652165",
            "masterRight" : 1,
            "secret" : ""
        })



