#How To Add Files To This Repository 
    ##One Time Setup [ Do This Only Once ]

        1.Clone the Repository:
        ``` bash
        git clone https://github.com/vidyesh-kumar/HPE_CTY.git
        ``` 

        2.Create A New Branch:
        ``` bash
        git branch <Your Name>
        ``` 

        3.Go To The New Branch:
        ``` bash
        git checkout <Your Name>
        ``` 

        4.Create A New Folder in Learning Folder:
        ``` bash
        cd Learning
        mkdir <Your Name>
        ``` 

        5.Come Back to Main Folder:
        ``` bash
        cd ..
        ``` 

    ##Folder Modification [ Everytime Any Changes Done To The Folder Like Addition of New File(s), Modification of File(s), Deletion of File(s)]

        1.Make Sure You Are in The HPE_CTY Folder
        ``` bash
        pwd
        ``` 

        2.Make Sure You Are In Your Branch
        ``` bash
        git branch
        ``` 
        Note: Your branch will be highlighted with a star 

        2a. If You are not in Your Branch :
        ``` bash
        git checkout <Your Name>
        ``` 

        2b. And then Verify using 
        ``` bash
        git branch
        ``` 

        3.Save Your Changes:
        ``` bash
        git add .
        ``` 

        4.Commit Your Changes:
        ``` bash
        git commit -m "A Message regarding what u added/learnt"
        ``` 

        5.Push Your Changes To Your Branch:
        ``` bash
        git push -u origin <Your Name>
        ``` 