grammar url;

// The main parser rule
start : url EOF;

url : scheme subdomain body tld path?;

body : TEXT '.' ;
tld : 'com' | 'org' | 'net' | 'gov' | phrase '.' ;
path : '/' phrase | '/' phrase path ;
phrase : TEXT | TEXT phrase ;

TEXT : [a-z]+ | [0-9]+ | [a-z] TEXT | [0-9] TEXT ; 

scheme : 'https://' | 'http://' ;
subdomain : 'www.' ;


//need to expand subdomain, scheme