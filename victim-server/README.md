## Victim server

Emulates a typical Java web-app. Technically it's a Spring-Boot application with an embedded  Apache Tomcat 8.5.16

## Prerequisites 
 * Java 1.8
 
## How to run

        ./mvnw spring-boot:run
        
* A page with a "HelloWorld1!" will be rendered after accessing [http://localhost:8080](http://localhost:8080)
* The number after HelloWorld will be incremented by 1 with each request. 
* An average response time is about 160ms, if ignore network latency.
       
        