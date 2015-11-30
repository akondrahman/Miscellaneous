# Akond Rahman 
## Documentation for Proxy Server (Option -2) 
## Github Link: <https://github.ncsu.edu/aarahman/CSC791HW_Redis>

### Demonstration 
 
  1. routing created for */*, */get*, and */set*. See images below. 
     ![root](root.png?raw=true=400x300) 
     ![get](get.png?raw=true=400x300) 
     ![set](set.png?raw=true=400x300)
      
  2. Most recent pages are displayed too : 
     ![recent](recent.png?raw=true=400x300)     
  
  3. routing created for */upload*, and */meow*. 
     See corresponding images below. A queue-lke structure was   	 implemented to store the uploaded picture ina  FILO fashion.  
     ![uploadMeow](uploadMeow.png?raw=true=400x300) 
  
  4. Multiple servers are runnign and load is balanced accordingly amomgst the two   
     proxy server. See console output below.  
     ![proxy](proxy.png?raw=true=400x300) 
