# var firstName = document.getElementById('firstName').value;
#     var secondName = document.getElementById('secondName').value;
#     firstName = firstName.trim().toLowerCase(); secondName = secondName.trim().toLowerCase();

#     for (var i = 0; i < firstName.length; i++) {
#         for (var j = 0; j < secondName.length; j++) {
#             if (firstName[i] == secondName[j]) {
#                 firstName = firstName.replace(firstName[i], " ")
#                 secondName = secondName.replace(secondName[j], " ");
#                 break;
#             }
#         }
#     }

#     firstName = firstName.replace(/ /g, ""); secondName = secondName.replace(/ /g, "");
#     var num = firstName.length + secondName.length;
#     var obj = { 'f': "Family", "l": "Love", "a": "Affection", "m": "Marrage", "e": "Enemy", "s": "Sex", "u": "Direct shobanam" };
#     var result = "flames";
#     if (num == 0) {
#         console.log("direct shobanam");
#         result = "u"
#     }
#     else {
#         while (result.length != 1) {
#             var r = num % result.length
#             if (r == 0) {
#                 result = result.substring(0, result.length - 1);
#             }
#             else {
#                 result = result.substring(r, result.length) + result.substring(0, r - 1);
#             }
#         }
#     }
#     document.getElementById("result").innerHTML = "FLAMES DECIDES : " + obj[result];

name1=list(input().strip().lower().replace(" ",""))
name2=list(input().strip().lower().replace(" ",""))
print(name1,name2)
for i in range(len(name1)):
    for j in range(len(name2)):
        if name1[i] == name2[j]:
            print(i,j)
            name1[i]=""
            name2[j]=""
name1.remove('')
name2.remove('')
print(name1,name2)
