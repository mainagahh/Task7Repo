int n, a = 0;
    int arr[n];
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    } 

    for(int i=0; i<n; i++)
    {
        for(int j=i+1; j<n; j++) { if(arr[i]>arr[j])
            {
                a = arr[i];
                arr[i] = arr[j];
                arr[j] = a;
            }
        }
    }
    cout << arr[n-1] <<endl;
    return 0;