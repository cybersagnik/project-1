"""Author : Sagnik Ray 
   Date: 29/06/2024
   
   THIS IS THE SIMPLE POC SCRIPT OF BYPASSING SNORT'S PRECONFIGURED SCAN RULES THAT COMES WITH THE FREE VERSION OF SNORT
   THE RULE SET IS STANDARD AS PER SECURITY NORMS AND KNOWN SCANNING TECHNIQUES.
   IT DETECTS MAJOR SCANNING TECHNIQUES (SYN FIN , XMAS ,NULL SCAN,SYN SCAN) BUT IT FAILS TO DETECT ANY NEW SCANNING TECHNQUE.
   
   THIS POC DEMONSTRATE HOW PRECONFIGURED RULES IN AN IDS OR IPS CAN BE BYPASSED BY INTRODUCING SOME NEW METHODS 

   Github repo to read about the scan.rules : https://github.com/eldondev/Snort/blob/master/rules/scan.rules
   ##### RULESET OF SNORT THAT IS IMPORTANT FOR THE POC
      { 
       alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN FIN"; flow:stateless; flags:F,12; reference:arachnids,27; classtype:attempted-recon; sid:621; rev:7;)
       # alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN ipEye SYN scan"; flow:stateless; flags:S; seq:1958810375; reference:arachnids,236; classtype:attempted-recon; sid:622; rev:8;)
       alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN NULL"; flow:stateless; ack:0; flags:0; seq:0; reference:arachnids,4; classtype:attempted-recon; sid:623; rev:6;)
       alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN SYN FIN"; flow:stateless; flags:SF,12; reference:arachnids,198; classtype:attempted-recon; sid:624; rev:7;)
       alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN XMAS"; flow:stateless; flags:SRAFPU,12; reference:arachnids,144; classtype:attempted-recon; sid:625; rev:7;)
       alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN nmap XMAS"; flow:stateless; flags:FPU,12; reference:arachnids,30; classtype:attempted-recon; sid:1228; rev:7;)
       # alert tcp $EXTERNAL_NET any -> $HOME_NET any (msg:"SCAN synscan portscan"; flow:stateless; flags:SF; id:39426; reference:arachnids,441; classtype:attempted-recon; sid:630; rev:7;) 
      }
      AS YOU CAN SEE IT IS ALERTING AGAINST ALL THE STANDARD KNOWN SCANNING TECHNIQUES BUT ANY MODIFIED TECHNIQUE WOULD BYPASS IT . IF ANYONE FACES TROUBLE UNDERSTANDING THE RULES DO CHECK THE RESOURCES SECTION TO UNDERSTAND IT IN DETAIL
  #####
   
   
   UNDERSTANDING THE TCP FLAGS USED IN THIS POC AND HOW AND WHY THEY WORK IN OUR SCENARIO
   
   PUSH(P): THE PSH FLAG INSTRUCTS THE RECEIVING TCP STACK TO DELIVER THE DATA TO THE RECEIVING APPLICATION IMMEDIATELY , RATHER THAN WAITING TO ACCUMULATE A FULL BUFFER OF DATA.
   
   ADVANTAGE OF PSH FLAG: THIS TCP SPECIFICATION DOES NOT REQUIRE ANY SPECIAL ACKNOWLEDGEMENT OR RESPONSE SPECIFICALLY FOR SEGMENTS WITH THE PSH FLAG SET. THE FLAG'S PURPOSE IS PURELY FOR EFFICIENT DATA HANDLING 
   WITHIN THE RECEIVER'S TCP STACK AND THEREFORE IN THE POC SCRIPT WE DONT HANDLE ANY ACKNOWLEDGEMENT FROM THE RECEIVER'S END IF THERE IS NO RESPONSE THIS INDICATES THE PORT IS OPEN [**WE NEED TO DOUBLE CHECK THE LOGIC 
   AS IF SNORT IS CONFIGURED IN IPS MODE IT MIGHT  DROP THE PACKET GENEREATING NO RESPONSE] AND IF THE SERVER SENDS A PACKET WITH RST FLAG SET THEN ITS A CLEAR INDICATION THAT THE PORT IS CLOSED.
   
   URGENT(U): THE URG FLAG IS USED TO INFORM THE RECEIVING SERVER THAT CERTAIN DATA WITHIN A SEGMENT IS URGENT AND SHOULD BE PRIORITIZED .IF URG FLAG IS SET THE RECEIVING STATION EVALUATES THE URGENT POINTER (
   A 16 BIT FIELD IN THE TCP HEADER ) . THE POINTER INDICATES HOW MUCH OF THE DATA IN THE SEGMENT , COUNTING FROM THE FIRST BYTE , IS URGENT.
   
   ADVANTAGE OF THE URG FLAG: SAME LIKE PSH FLAG URG FLAG NEEDS NO SPECIAL ACKNOWLEDGEMENT (**WHILE SOME APPLICATIONS PREFER/NEED TO SEND ACKNOWLEDEMENT IN CASE OF BOTH PSH AND URG ) THE POC CAN BE CONDUCTED WIHT PSH FLAG ALONE 
   IT DOES NOT REQUIRE THE URGENT FLAG AND VICE VERSA . BUT IT ADDS A LAYER OF BIT DECORATION JUST LIKE XMAS SCAN ..."""
   
from scapy.all import *
from termcolor import colored
import random
import time

open_ports=[]
target= "192.168.56.108" #Edit it As per your network configuration
def send_forged_packet():
  top_ten=[21,22,23,25,80,139,80,110,445,143,443,3306,3389]
  for port in top_ten:
      ip = IP(dst=target)
      tcp = TCP(sport=random.randint(1,65535),dport=port,flags="PU",urgptr=1)
      packet = ip/tcp
      response = sr1(packet,timeout=2,verbose=False)
      end_time = time.time()
      if response and TCP in response and response[TCP].flags == 'RA':
        continue
      else:
        open_ports.append(port)
      

def main_func():
  send_forged_packet()
  for open_port in open_ports:
    print(colored(f"[+]Port: {open_port} is Open",'green'))

if __name__ == '__main__':
  print(colored(f"\nScanned of open ports for Target : {target}",'cyan'))
  main_func()
