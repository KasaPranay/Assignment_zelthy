from purchase.models import PurchaseStatusModels,PurchaseModel
import random
from datetime import datetime, timedelta
 
 
start = datetime(2019, 1, 1, 17, 00, 00)
end = datetime(2020, 3, 31, 22, 00, 00)
 

def gen_datetime(min_year=1900, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

statusList = ['Open','Delivered','Dispatched','Verified']
for i in PurchaseModel.objects.all():
    PurchaseStatusModels(
        purchase=i,
        status=statusList[int(random.random())%4],
        created_at = start + (end - start) * random.random(),
    ).save()
