from re import *

text="abced12KABC5o4_@#"

#pattern="\d""[0-9]"
#pattern="\D" #[^0-9]
#pattern="\w" #[a-zA-Z0-9]
#pattern="\W"   #special characters
pattern="[^aeiou_\W\d]"#consonents


matcher=finditer(pattern,text.casefold())

for m in matcher:
    print(m.group(),m.start())