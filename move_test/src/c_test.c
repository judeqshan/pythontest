#if defined(_WIN32)

#include <tchar.h>
#include <windows.h>
#include <winnt.h>
#include <winbase.h>

#else
    #include "WinTypes.h"
    #include <unistd.h>

    #include <stdio.h>
#endif

int cHi()
{
   // printf() 中字符串需要引号
   printf("Hello, World!\n");

   BYTE number[10];
   number[0] = 0x6;
   int mask = 12;
   number[0] &=  ~(mask);
   number[0] |=  (0x8 & mask);
   return number[0];
   // return  1;
}