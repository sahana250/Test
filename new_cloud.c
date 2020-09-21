#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#define VIN_CODE "MALCU41DLCM070737"
#define TRUE            (0)
int main(void)
{
	CURL *curl;
	CURLcode res;
	struct curl_slist *headers = NULL;
	char buffer[80000] = {0};
	char dev_id[20] = "866758047254921";
	char temp[100];

	char iccId[15] = "12312432421534";
	char status = '0';
	/* In windows, this will init the winsock stuff */ 
	curl_global_init(CURL_GLOBAL_ALL);

#if 0
         sprintf(temp,"deviceID=%s&",dev_id);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"iccid=%s&",iccId);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"status=%c&",status);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"enginehours=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

	 
         sprintf(temp,"odometer=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"trip=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"totalfuel=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"crash=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"fixmode=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

	 sprintf(temp, "enginecoolanttemperature=%d&",123);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));


         sprintf(temp,"lat=%lf&",18.472730);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"lon=%lf&",73.811045);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"accuracy=%s&","null");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"gpstime=%d&",0);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"utctime=%d&", 0);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"version=%s&","iW-G26U-R2.0-REL1.0");
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"n=%c&",'1');
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"vin=%s&",VIN_CODE);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"alarm=%c&",'0');
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

         sprintf(temp,"speed=%d",120);
         strcat(buffer,temp);
         memset(temp,0,sizeof(temp));

#endif
//	 strcpy(buffer, "deviceID=86675804725492&iccid=89910009033890&status=0&enginehours=null&odometer=null&trip=null&totalfuel=null&crash=null&fixmode=null&enginecoolanttemperature=121&lat=10.000000&lon=10.000000&accuracy=null&gpstime=0&utctime=0&version=iW-G26U-R2.0-REL1.0&n=1&vin=MALCU41DLCM070737&alarm=0&speed=118");
	strcpy(buffer, "deviceID=866758047254921&iccid=12312432421534&status=0&enginehours=null&odometer=null&trip=null&totalfuel=null&crash=null&fixmode=null&enginecoolanttemperature=121&lat=18.472730&lon=73.811045&accuracy=null&gpstime=0&utctime=0&version=iW-G26U-R2.0-REL1.0&n=1&vin=MALCU41DLCM070737&alarm=0&speed=120");
        printf ("%s\n", buffer);



	/* get a curl handle */ 
	curl = curl_easy_init();
	if(curl)
       	{
		/* First set the URL that is about to receive our POST. This URL can
		   just as well be a https:// URL if that is what should receive the
		   data. */ 
		 //curl_easy_setopt (curl, CURLOPT_SSL_VERIFYPEER, TRUE);
        	 //curl_easy_setopt (curl, CURLOPT_CAINFO, "/etc/ssl/certs/ca-bundle1.crt");

		curl_easy_setopt(curl, CURLOPT_URL, "http://15.185.77.2/obd-response/api/web/v1/obd/d");


		//headers = curl_slist_append (headers, "Accept: application/json");
		//headers = curl_slist_append (headers, "Content-Type: application/json");


		//curl_easy_setopt (curl, CURLOPT_HTTPHEADER, headers);

		/* Now specify the POST data */ 
		time_t begin = time(NULL);
		curl_easy_setopt(curl, CURLOPT_POSTFIELDS, buffer);

		/* Perform the request, res will get the return code */ 
		res = curl_easy_perform(curl);

		time_t end = time(NULL);
		printf("Time elpased is %ld seconds", (end - begin));

		/* always cleanup */ 
		curl_easy_cleanup(curl);
		curl_slist_free_all(headers);
	}

	curl_global_cleanup();
	return 0;
}
