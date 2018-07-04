#question 1
import re
l=["zuck26@facebook.com"]
s=re.split("[@.]",("(zuck26@facebook.com)" "(page33@google.com)""( jeff42@amazon.com)"))
print(s)

#question2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
pt=re.findall("[bB]\w+",text)
print(pt)


#question3
import re
x="A, very very; irregular_sentence"
s=re.sub("\W"," ",x)
print(s)

