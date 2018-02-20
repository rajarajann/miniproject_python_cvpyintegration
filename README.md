
inwk6312-winter2018-miniproject-rajarajann created by GitHub Classroom

Project Title : User Interface for Commvault Simpana using Python

Problem statement : Commvault Simpana backup tool which is an Enterprise level backup suite has only GUI based operations since it can be hosted only on a windows server as it is dependent on MSSQL as its back end database. Because of this constrain we will not be able to perform any remote operations on this backup suite from a non-GUI based OS , mostly Unix servers. Hence this python program would create a python interface which will enable us to perform the operations on this suite.

Task description : I have initiated a windows server in Google Cloud platform which is being used as the Commvault backup server. One more GCP VM instance as a client machine that will be backedup by the Commvault server.The remote storage for this backup is a nearline storage offered in google cloud platform. My python program will act as a user interface from Unix machine to work with operations like, creating a client, running a backup, restoring the backup, browsing through the backup files etc on the server and alert us if the Google’s cloud storage is reaching the threshold that we set.

Tools planned to use and their reference links:

Tool : Commvault v11 (Evaluation version) API: Commvault REST Data formats : JSON, XML Work environment : Google cloud platform , Windows Server 2012, Windows Server 2008 R2,Pycharm

Future scope:

Improve support for user interactions by installing all the features available in the GUI console

References made till now:

http://documentation.commvault.com/commvault/v10/article?p=features/rest_api/rest_api_getting_started_python.htm
