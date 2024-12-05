grammar AwsArn;

start: awsArn EOF;

awsArn          : 'arn' ':' partition ':' service ':' region ':' accountId ':' resourceType resourceId;

partition       : 'aws' | 'aws-cn' | 'aws-us-gov'; // main three partitions
service         : [a-zA-Z0-9-]+; // service names are alphanumeric, may include hyphens
region          : [a-z]{2}-[a-z]+-[0-9]{1}; // Region format e.g. us-west-2, etc.
accountId       : [0-9]{12}; // 12 digit AWS account number
resourceType    : [a-zA-Z0-9-]+; // Alphanumeric resource type
resourceId      : ( [a-zA-Z0-9-]+ | '/' [a-zA-Z0-9-]+ )+; // Resource ID can include slashes for nested resources

// WS              : [ \t\r\n]+ -> skip; // Skip whitespace

// format arn:partition:service:region:account-id:resource-type/resource-id
