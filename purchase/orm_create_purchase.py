from purchase.models import PurchaseModel

thisdict = {"Joe": 5,"Rahul": 6,"Raveena": 7,"Paul": 8,"Amanda": 9,}
for i in range(0, 1000):
    for x, y in thisdict.items():
        PurchaseModel(
            purchaser_name=x,
            quantity=y,
        ).save()


