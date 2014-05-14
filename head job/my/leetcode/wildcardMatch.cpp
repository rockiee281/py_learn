#include <cstring>
#include <iostream>

using namespace std;

class Solution {
public:
bool isMatch(const char *s, const char *p) {  
  // Start typing your C/C++ solution below  
  // DO NOT write int main() function  
  bool star = false;  
  const char *str, *ptr;  
  for(str = s, ptr =p; *str!='\0'; str++, ptr++)  
  {  
    cout << *str << "|" << *ptr << endl;
    switch(*ptr)  
    {  
       case '?':  
         break;  
       case '*':  
         star =true;  
         s=str, p =ptr;  
         while(*p=='*')  
           p++;  
         if(*p == '\0') // 如果'*'之后，pat是空的，直接返回true  
           return true;  
         str = s-1;
         ptr = p-1;  
         break;  
       default:  
       {  
         if(*str != *ptr)  
         {  
           // 如果前面没有'*'，则匹配不成功  
           if(!star)  
             return false;  
           s++;  
           str = s-1;  
           ptr = p-1;  
         }  
       }  
     }  
   }  
   while(*ptr== '*')  
     ptr++;  
   return (*ptr == '\0');  
}  

};

int main(){
    char s[512];
    char p[512];
    strcpy(s, "asab");
    strcpy(p, "*sb");
    Solution *solution = new Solution();
    cout <<    solution->isMatch(s, p) << endl;

}
