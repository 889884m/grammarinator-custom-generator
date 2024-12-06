grammar url;

// The main parser rule
start : url EOF;

url : scheme subdomain body tld path?;

body : TEXT '.' ;
tld : 'com' | 'org' | 'net' | 'gov' | 'edu' | 'mil' | 'int' | 'ru' | 'uk' | phrase '.' ;
path : '/' phrase | '/' phrase pathText | '/' TEXT phrase ;
phrase : TEXT | TEXT phrase ;

TEXT : [a-z]+ | [0-9]+ | [a-z] TEXT | [0-9] TEXT ; 

pathText: '<' | '>' | '%' | '&' | '$' ; 

scheme : 'https://' | 'http://' | 'ftp://' | 'file://' | 'imap://' | 'irc://' ;
subdomain : 'www.' ;

