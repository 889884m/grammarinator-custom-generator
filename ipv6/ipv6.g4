grammar ipv6;

start: ipv6address;

ipv6address : full_address
            | ipv4_linked
			;

full_address: ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end    // 8 groups
            | ipv6_comp_st ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end  // 7 groups
            | ipv6_comp ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_comp ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_comp ipv6_group ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_comp ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_group ipv6_comp ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_comp ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_comp
            | ipv6_comp_st ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end             // 6 groups
            | ipv6_comp ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_comp ipv6_group ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_comp ipv6_group ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_comp ipv6_group ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_group ipv6_comp ipv6_end
            | ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv6_comp
            | ipv6_comp_st ipv6_group ipv6_group ipv6_group ipv6_group ipv6_end                        // 5 groups 
            | ipv6_comp ipv6_group ipv6_group ipv6_group ipv6_end                              
            | ipv6_group ipv6_comp ipv6_group ipv6_group ipv6_end                              
            | ipv6_group ipv6_group ipv6_comp ipv6_group ipv6_end                              
            | ipv6_group ipv6_group ipv6_group ipv6_comp ipv6_end                            
            | ipv6_group ipv6_group ipv6_group ipv6_group ipv6_comp                               
			| ipv6_comp_st ipv6_group ipv6_group ipv6_group ipv6_end                                   // 4 groups               
			| ipv6_comp ipv6_group ipv6_group ipv6_end                         
			| ipv6_group ipv6_comp ipv6_group ipv6_end                         
			| ipv6_group ipv6_group ipv6_comp ipv6_end                       
			| ipv6_group ipv6_group ipv6_group ipv6_comp             
			| ipv6_comp_st ipv6_group ipv6_group ipv6_end                                              // 3 groups             
			| ipv6_comp ipv6_group ipv6_end              
			| ipv6_group ipv6_comp ipv6_end              
			| ipv6_group ipv6_group ipv6_comp        
			| ipv6_comp_st ipv6_group ipv6_end                                                         // 2 groups       
			| ipv6_comp ipv6_end      
			| ipv6_group ipv6_comp     
			| ipv6_comp_st ipv6_end                                                                    // 1 group
			| ipv6_comp                                                                                    
			| ipv6_comp_st                                                                             // 0 groups                                              
			;

ipv4_linked : ipv6_group ipv6_group ipv6_group ipv6_group ipv6_group ipv4_linked ipv4_address          // 6 groups
            | ipv6_comp_st ipv6_group ipv6_group ipv6_group ipv6_group ipv4_linked ipv4_address        // 5 groups 
            | ipv6_comp ipv6_group ipv6_group ipv6_group ipv4_linked ipv4_address                             
            | ipv6_group ipv6_comp ipv6_group ipv6_group ipv4_linked ipv4_address                              
            | ipv6_group ipv6_group ipv6_comp ipv6_group ipv4_linked ipv4_address                             
            | ipv6_group ipv6_group ipv6_group ipv6_comp ipv4_linked ipv4_address                                
			| ipv6_comp_st ipv6_group ipv6_group ipv6_group ipv4_linked ipv4_address                   // 4 groups               
			| ipv6_comp ipv6_group ipv6_group ipv4_linked ipv4_address                        
			| ipv6_group ipv6_comp ipv6_group ipv4_linked ipv4_address                        
			| ipv6_group ipv6_group ipv6_comp ipv4_linked ipv4_address             
			| ipv6_comp_st ipv6_group ipv6_group ipv4_linked ipv4_address                              // 3 groups             
			| ipv6_comp ipv6_group ipv4_linked ipv4_address             
			| ipv6_group ipv6_comp ipv4_linked ipv4_address         
			| ipv6_comp_st ipv6_group ipv4_linked ipv4_address                                         // 2 groups       
			| ipv6_comp ipv4_linked ipv4_address      
			| ipv6_comp_st ipv4_linked ipv4_address                                                    // 1 group
			;


ipv6_group   : fourhex COLON;
ipv6_comp    : fourhex DOUBLECOLON;
ipv6_comp_st : DOUBLECOLON;
ipv6_end     : fourhex;
ipv4_linked  : IPV4LINK COLON;
ipv4_address : threeoct PERIOD threeoct PERIOD threeoct PERIOD threeoct  ;

fourhex  : HEXDIGITNOZERO HEXDIGIT HEXDIGIT HEXDIGIT
         | HEXDIGITNOZERO HEXDIGIT HEXDIGIT
		 | HEXDIGITNOZERO HEXDIGIT
		 | HEXDIGITNOZERO
		 ;

threeoct : DECIMAL DECIMAL DECIMAL
         | DECIMAL DECIMAL
		 | DECIMAL
		 ;


HEXDIGIT       : [0-9a-fA-F];
HEXDIGITNOZERO : [1-9a-fA-F];
COLON          : ':';
DOUBLECOLON    : '::';

DECIMAL        : [0-9];
PERIOD         : '.';
IPV4LINK       : 'FFFF';
