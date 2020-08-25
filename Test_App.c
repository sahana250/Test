#include <stdio.h>
#include <curl/curl.h>
#include <string.h> 
#include <stdlib.h>
#include <time.h>

char *Json_Data = " ";
char Uni_ID[10] = "12345" ;
char ENVT[10] = "Avnet";
char baseURL[128] = "https://avnetagent.iotconnect.io/api/2.0/agent/sync";
char CPID[50] = "98f5b52a59aa4503999894c10bc33dca" ;
char Host_Name[60] = "poc-iotconnect-iothub-eu.azure-devices.net";
char ID[50] = "98f5b52a59aa4503999894c10bc33dca-12345";
char *Sensor_Data(void);
static char buffer[2048] = {0};

char *Sensor_Data(void)
{
        char temp[512] = {0};

	int hours, minutes, seconds, day, month, year;
        time_t t = time(NULL);
        struct tm *local = localtime(&t);

        hours = local->tm_hour;
        minutes = local->tm_min;
        seconds = local->tm_sec;
        day = local->tm_mday;
        month = local->tm_mon + 1;
        year = local->tm_year + 1900;

        sprintf(temp,"{\"Unique_ID\":\"%s\",", Uni_ID);
        strcpy(buffer, temp);
        memset(temp, 0, sizeof(temp));

        sprintf(temp, "\"time\":\"%d/%d/%d\", \"%2d:%2d:%2d\", ", day, month, year, hours, minutes, seconds );
        strcat(buffer, temp);
        memset(temp, 0, sizeof(temp));

        sprintf(temp, "\"reporting\":{\"Humidity\":\"%d\",", 2345);
        strcat(buffer,temp);
        memset(temp, 0, sizeof(temp));

        sprintf(temp, "\"axis\" : {\"X_axis\":\"%f\",\"Y_axis\":\"%f\",\"Z_axis\":\"%f\"", 18.234, 10.678, 13.345);
        strcat(buffer, temp);
        memset(temp, 0, sizeof(temp));

	strcat(buffer,"}}}");
        printf("\nFRAME_FINAL_PACKET buffer\n %s", buffer);

	return buffer;
}

int main(void)
{
	int rc = 0, count = 0;
	rc = cloud_init();
        if (rc != 0)
                printf("\n Cloud_init failed.\n");
	while(count < 10)
	{
		Json_Data = Sensor_Data();		
		rc = HTTPConnection(Json_Data);
		sleep(10000);
		count++;
		if(rc != 0)
			printf("\n\n HTTP Connection Failed.. \n ");
	}
}

int cloud_init()
{
	int rc = 0;
	int err = 0;
	char postData[8192];
	struct curl_slist *headers = NULL;
	CURL *curl;
  	rc = curl_global_init(CURL_GLOBAL_ALL);
	if(rc != CURLE_OK)
		err = rc;
	printf("\n curl_global_init %d -\n", err);
	curl = curl_easy_init();
  	rc = curl_easy_setopt(curl,CURLOPT_CAINFO,"/etc/ssl/certs/ca-bundle1.crt");
	if(curl) 
	{
    		rc = curl_easy_setopt(curl, CURLOPT_URL, "https://avnetagent.iotconnect.io/api/2.0/agent/sync");
 		 
		strcpy(postData, "{\"cpId\":\"");
          	strcat(postData, CPID);
          	strcat(postData, "\",\"uniqueId\":\"");
          	strcat(postData, Uni_ID);
          	strcat(postData, "\",\"option\":{\"attribute\":false,\"setting\":false, ");
		strcat(postData, "\"protocol\":true,");
		strcat(postData, "\"device\":false,\"sdkConfig\":false,\"rule\":false}}");
	
		headers = curl_slist_append(headers, "Accept: application/json");
	        headers = curl_slist_append(headers, "Content-Type: application/json");
		
		curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
		curl_easy_setopt(curl, CURLOPT_POSTFIELDS, postData);
    		
		rc = curl_easy_perform(curl);
		printf("\n curl_easy_perform1 %d - \n", rc);
    		curl_slist_free_all(headers);
  	}
	curl_global_cleanup();
  	return rc;
}

int HTTPConnection(char *Json_Data)
{
	int rc = 0;
	char Url[180];
	CURL *curl;
	//struct curl_slist *headers = NULL;
	strcpy (Url, "https://");
	strcat (Url, Host_Name);
	strcat (Url, "/devices/");
	strcat (Url, ID);
	strcat (Url, "/messages/events");
	strcat (Url, "?api-version=2016-02-03");
		printf("\n\n URL = %s\n", Url);

	curl = curl_easy_init();
        rc = curl_easy_setopt(curl, CURLOPT_CAINFO, "/etc/ssl/certs/ca-bundle1.crt");
        if(curl == NULL)
                return -1;

	//headers = curl_slist_append(headers, "Accept: application/json");
	//headers = curl_slist_append(headers, "Content-Type: application/json");

	rc = curl_easy_setopt(curl, CURLOPT_URL, Url);
                printf("\n curl_easy_setopt 1 %d -\n", rc);
	rc = curl_easy_setopt(curl, CURLOPT_POSTFIELDS, Json_Data);
		printf("\n curl_easy_setopt 2 %d -\n", rc);
	rc = curl_easy_perform(curl);
		printf("\n curl_easy_perform 2 %d -\n", rc);

	//curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
	return rc;
}
































