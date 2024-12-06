
URL_grammar;

<start>: [“<url>”]
<url>: <scheme> + <subdomain> + <body> + <tld> + <path>
<body>: <text> + . | <text> + <body>
<tld>: .com | .org | .net | .gov | <phrase> + . | <phrase> + . + <tld>
<path>: / + <phrase> | / <phrase> + / + <path>
<phrase>: <text> | <text> + <phrase>
<text>: [a-z] | [0-9]
<scheme>: https:// | http:// | <phrase> + .
<subdomain>: www. | <phrase> + .
    