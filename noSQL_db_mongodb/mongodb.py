from pymongo import MongoClient
client = MongoClient('localhost', 27017)
for item in client.Northwind["order-details"].aggregate([
		{
			'$group' : 
			{
				'_id' : "$OrderID", 
				'amount' : 
				{
					'$sum' : 
					{
						'$multiply' : ['$UnitPrice', '$Quantity'] 
					}
				}
			}
		},
		{
			'$sort' : 
			{
				'_id' : 1
			}
		}
	]):
	print(item)
