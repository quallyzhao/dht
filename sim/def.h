#ifndef INCL_DEF
#define INCL_DEF

#ifndef MAX_INT
#define MAX_INT  0x7fffffff
#endif

#ifndef TRUE
#define TRUE 1
#define FALSE 0
#endif

#define NUM_BITS      4
#define MAX_NUM_DOCS 50

#define AVG_PKT_DELAY    2
#define STABILIZE_PERIOD 1000

/* maximum simulation time */
#define MAX_TIME     1e+05 /* in usec */   

/* used in node.c */
#define POWER_HASH_TABLE 10
#define HASH_SIZE        1024

/* used in event.c */
#define MAX_NUM_ENTRIES  4096
#define ENTRY_TUNIT 100 /* 0.1 msec */ 

#endif 
