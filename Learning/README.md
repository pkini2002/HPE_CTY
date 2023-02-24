How To Add Files To This Repository 

One Time Setup [ Do This Only Once ]

Clone the Repository:
git clone https://github.com/vidyesh-kumar/HPE_CTY.git

Create A New Branch:
git branch <Your Name>

Go To The New Branch:
git checkout <Your Name>

Create A New Folder in Learning Folder:
cd Learning
mkdir <Your Name>

Come Back to Main Folder:
cd ..

Folder Modification [ Everytime Any Changes Done To The Folder Like Addition of New File(s), Modification of File(s)]

Make Sure You Are in The HPE_CTY Folder
pwd

Make Sure You Are In Your Branch
git branch
Note: Your branch will be highlighted with a star 

If You are not in Your Branch 
git checkout <Your Name>
and then Verify using git branch

Save Your Changes:
git add .

Commit Your Changes:
git commit -m "A Message regarding what u added/learnt"

Push Your Changes To Your Branch:
git push -u origin <Your Name>