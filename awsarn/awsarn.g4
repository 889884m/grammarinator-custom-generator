grammar AwsArn;

start: awsArn EOF;

awsArn          : 'arn' ':' partition ':' service ':' region ':' accountId ':' resourceType resourceId;

partition       : 'aws' | 'aws-cn' | 'aws-us-gov'; // main three partitions
service         : TEXT; // service names are alphanumeric, may include hyphens
region          : 'us-east-1' | 'us-east-2' | 'us-west-1' | 'us-west-2' |
                  'af-south-1' | 'ap-east-1' | 'ap-south-1' | 'ap-northeast-1' |
                  'ap-northeast-2' | 'ap-northeast-3' | 'ap-southeast-1' |
                  'ap-southeast-2' | 'ap-southeast-3' | 'ca-central-1' |
                  'eu-central-1' | 'eu-west-1' | 'eu-west-2' | 'eu-west-3' |
                  'eu-north-1' | 'eu-south-1' | 'me-south-1' | 'sa-east-1';// [a-z]{2}-[a-z]+-[0-9]{1}; // Region format e.g. us-west-2, etc.
accountId       : NUM NUM NUM NUM NUM NUM NUM NUM NUM NUM NUM NUM; // 12 digit AWS account number
resourceType    : TEXT; // Alphanumeric resource type
resourceId      : ( TEXT | '/' TEXT )+; // Resource ID can include slashes for nested resources

TEXT            : [a-zA-Z0-9-]+
NUM             : [0-9]

// WS              : [ \t\r\n]+ -> skip; // Skip whitespace

// format arn:partition:service:region:account-id:resource-type/resource-id
