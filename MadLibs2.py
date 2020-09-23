##value1 = "12345678912345"
##value2 = "3.141592653"
##
##example = str.format("Formatting string {0:10.10} {1:4.4} {2:^20} {4:>20} {5:<20}",value1,value2,"test",42,8,9.10)
##print(example)
##
##print(str.format("Example 'd':{0:15d}",150000))
##print(str.format("Example ',':{0:15,}",150000))
##print(str.format("Example 'e':{0:15e}",150000))
##print(str.format("Example 'f':{0:15f}",3.14159))
##print(str.format("Example 'g':{0:15g}",3.14159))
##print(str.format("Example '%':{0:15%}",0.75))

noun1 = input("Name a noun. ")
adj1 = input("Name an adjective. ")
percent = input("Name a percentage. ")
noun2 = input("Name a noun. ")
noun3 = input("Name a noun. ")
noun4 = input("Name a noun. ")
adj2 = input("Name an adjective. ")
noun5 = input("Name a noun. ")
verb1 = input("Name a verb. ")
adj3 = input("Name an adjective. ")
adj4 = input("Name an adjective. ")

str_table = "|---*---*---*---*---*---*---|Please Wait|---*---*---*---*---*---*---|"
print(str_table)

my_poem = str.format("""Life is short, though I keep this from my {}.
Life is short,
and I've shortened mine in a thousand {} ill-advised ways,
a thousand deliciously ill-advised ways
I'll keep from my children.
The world is at least {} terrible,
and that's a conservative estimate,
though I keep this from my children.
For every {}  there is a {} thrown at a {} 
For every loved child,a child broken, {} sunk in a {}.
Life is short and the world is at least half terrible,
and for every kind stranger,
there is one who would break you,
though I keep this from my children.
I am trying to sell them the world.
Any decent realtor, {} you through
a real shithole, chirps on about good bones:
This place could be {}, right?
You could make this place {}.""",noun1,adj1,percent,noun2,noun3,noun4,adj2,noun5,verb1,adj3,adj4)

print(my_poem)
input()
