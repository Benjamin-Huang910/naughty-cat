dm 'log;clear;output;clear';
proc datasets lib=Work kill;quit;
OPTIONS FORMCHAR="|----|+|---+=|-/\<>*"; 

libname myLib 'D:\Dropbox\Teaching\Metrics-College\2 CAPM\PS1';

/* Merging data */
data Stkdata;
	set mylib.Stkdata;
	where TICKER in ('AAPL' 'INTC' 'MSFT');
run;

proc sort data=Stkdata out=Stkdata;
	by DATE TICKER;
run;

proc sort data=mylib.Mktdata out=Mktdata;
	by DATE;
run;

data regdata;
	merge Stkdata Mktdata;
	by DATE;
	RETRF = RET-RF;
run;

proc sort data=regdata;
	by TICKER DATE;
run;

/* CAPM estimation */
proc reg data=regdata;
	by TICKER;
	model RETRF = MKTRF;
	title 'CAPM';
quit;

/* FF-3 model estimation and F-test (against CAPM) */
proc reg data=regdata;
	by TICKER;
	model RETRF = MKTRF SMB HML;
	title 'FF3';
	test SMB=0, HML=0;
quit;

/* Collinearity */
proc reg data=mylib.mktdata;
	model MKTRF = SMB HML;
	model SMB = MKTRF HML;
	model HML = MKTRF SMB;
	title 'Collinearity';
quit;

proc reg data=regdata;
	by TICKER;
	model RETRF = MKTRF SMB HML /vif;
	title 'VIF';
quit;


/* Constructing D variable */
data regdata;
	set regdata;
	if MKTRF >= 0 then D=1;
		else D=0;
run;

/* Chow Test */
data regdata;
	set regdata;
	DMKTRF = D*MKTRF;
	DHML = D*HML;
	DSMB = D*SMB;
run;

proc reg data=regdata;
	by TICKER;
	model RETRF = MKTRF SMB HML D DMKTRF  DSMB DHML;
	title 'Chow Test';
	test D=0, DMKTRF=0, DSMB=0, DHML=0;
quit;

