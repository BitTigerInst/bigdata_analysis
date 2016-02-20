from yahoo_finance import Share
import time
c = 0
yahoo = Share('YHOO')
google = Share('GOOG')
microsoft = Share('MSFT')
apple = Share('AAPL')
amazon = Share('AMZN')
filename1 = "yahoo.txt"
filename2 = "google.txt"
filename3 = "microsoft.txt"
filename4 = "apple.txt"
filename5 = "amazon.txt"
while True:

	with open(filename1,"a") as f:
		f.write(yahoo.get_price())
		f.write(" ")
	with open(filename2,"a") as f:
		f.write(google.get_price())
		f.write(" ")
	with open(filename3,"a") as f:
		f.write(microsoft.get_price())
		f.write(" ")
	with open(filename4,"a") as f:
		f.write(apple.get_price())
		f.write(" ")
	with open(filename5,"a") as f:
		f.write(amazon.get_price())
		f.write(" ")	
	
	yahoo.refresh()
	google.refresh()
	microsoft.refresh()
	apple.refresh()
	amazon.refresh()
	
	time.sleep(30)
	c+=1
	if c > 60:
		break