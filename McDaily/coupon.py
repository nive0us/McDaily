import re
from datetime import datetime, timedelta


class McDailyCoupon:

    def __init__(self, json):
        self.title               = json['coupon']['object_info']['title']
        self.redeem_end_datetime = datetime.strptime(json['coupon']['object_info']['redeem_end_datetime'], '%Y/%m/%d %H:%M:%S')
        self.current_datetime    = datetime.now()
        self.status              = json['coupon']['status']

        if self.redeem_end_datetime - self.current_datetime > timedelta():
            self.status          = 3

        # Coupon status
        # 1 == alive
        # 2 == redeemed
        # 3 == expired

        self.beautify()

    def beautify(self):
        self.title = re.sub(r'鷄', '雞', self.title)
        self.title = re.sub(r'\(G.*\)|\(S.*\)|_.*|\(新.*', '', self.title)
