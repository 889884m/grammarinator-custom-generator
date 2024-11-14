grammar ipv6;

start: ipv6address;

ipv6address:
	piece COLON piece COLON piece COLON piece COLON piece COLON piece;

piece: HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT;

HEXDIGIT: [0-9a-fA-F];
COLON: ':';
