grammar url;

// The main parser rule.
start: url EOF;

url: base query?;

base: scheme subdomain body tld path?;

body: TEXT '.';
tld: 'com' | 'org' | 'net' | 'gov' | phrase '.';
path: '/' phrase | '/' phrase path;
phrase: TEXT | TEXT phrase;

// Support arbitrary number of query parameters.
query: '?' pair ( '&' pair)*;
pair: key '=' value;
key: TEXT;
value: TEXT;

TEXT: [a-z]+ | [0-9]+ | [a-z] TEXT | [0-9] TEXT;

scheme: 'https://' | 'http://';
subdomain: 'www.';
