#include <iostream>

/*
int main()
{
    int arr[100];
    for (int i =0;i<100;i++)
    {
        arr[i]=0;
    }

    
    for (int monkey = 1; monkey <= 100; monkey++)
    {
        for (int i = 0; i < 100; i++)
        {
            if (i%monkey == 0)
            {
                if (arr[i] == 0)
                    arr[i] = 1;
                else                
                    arr[i] = 0;                
            }
            
        }
    }


    for (int i = 0; i < 100; i++)
    {
        if (arr[i] == 1)
            std::cout << i << std::endl;
    }
    return 0;
}*/

void initialize_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)    
        arr[i] = 0;
    
}

void toggle_doors(int arr[],int size)
{
    for ( int monkey =1 ; monkey <=size; monkey++)
    {
        for (int i=0; i<size; i++)
        {
            if (i%monkey == 0)
            {
                if (arr[i] == 0)
                    arr[i] = 1;
                else                
                    arr[i] = 0;                
            }
            
        }
    }
}

void print_array(int arr[],int size)
{
    for (int i=0; i <size; i++)
    {
        if (arr[i] == 1)
            std::cout << i << std::endl;
    }
}

int main()
{
    int size=100;
    int arr[size];

    initialize_array(arr, size);
    toggle_doors(arr, size);
    print_array(arr, size);
    return 0;
}