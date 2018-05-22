#include <iostream>
using namespace std;

//INSERTION SORT
int main()
{
   int i,j,a[10],key,N;
   cout<<"Enter the size of array N: ";
   cin>>N;
   cout<<"Enter the array elements:\n";
   for(i=0;i<N;i++)
    cin>>a[i];   //Input Array elements

// The sort begins...
   for(i=1;i<N;i++)
   {
       key=a[i];
       j=i-1;
       while(key<a[j] && j>=0)
       {
           a[j+1]=a[j];
           j--;  //Decrements the value of j
       }
       a[j+1]=key;

   }

   cout<<"\nThe elements sorted in ascending order are: ";
   for(i=0;i<N;i++)
   cout<<" "<<a[i];
}
