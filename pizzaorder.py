size=input("which pizza do younwant? S, M or L:")
bill=0
if size=="s":
  bill=bill+15
elif size=="m":
  bill=bill+20
else:
  bill=bill+25
add_pepperoni=input("do you want peppeoni? Y or N:")
if add_pepperoni=="y":
  if size=="s":
    bill=bill+2
  else:
    bill=bill+3
add_chesse=input("do you want extra chesse? Y or N:")
if add_chesse=="y":
   bill=bill+1
print(f"your final bill is{bill}") 
