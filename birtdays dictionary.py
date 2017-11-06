from bokeh.plotting import figure, show, output_file
# x = ["Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sep", "Oct", "Nov", "Dec"]
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [1,0,0,0,0,1,1,1,0,1,2,0]

birthdays = {
	"Albert Einstein": "03/14/1879",
	"Ada Byron Lovelace": "12/10/1815",
	"Benjamin Franklin": "01/17/1706"
}

# for a in birthdays.keys():
#     date =  birthdays[a]
#     x.append(date[:2])

print x
print y

output_file("plot.html")

p = figure()
p.vbar(x=x, top=y, width=0.5)
show(p)

