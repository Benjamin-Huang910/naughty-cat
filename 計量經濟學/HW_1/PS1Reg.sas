dm 'log;clear;output;clear';
proc datasets lib=Work kill;quit;
OPTIONS FORMCHAR="|----|+|---+=|-/\<>*"; 

libname myLib 'D:\Dropbox\Teaching\Metrics-College\2 CAPM\PS1';

data Stkdata;
	set mylib.Stkdata;
	where TICKER in ('AAPL' 'INTC' 'MSFT');
run;

proc sort data=Stkdata out=Stkdata;
	by DATE TICKER;
run;

data Mktdata;	
	set mylib.Mktdata;
run;

proc means data=Mktdata N Mean Median Std Min Max P10 P90;
	var MKTRF RF;
run;

proc sort data=Mktdata;
	by DATE;
run;

data Regdata;	
	merge Stkdata Mktdata;
	by DATE;
	RETRF = RET-RF;
run;

proc means data=Regdata N Mean Median Std Min Max P10 P90;
	class TICKER;
	var RETRF;
run;

proc sort data=Regdata;
	by TICKER DATE;
run;

proc reg data=Regdata;
	by TICKER;
	model RETRF=MKTRF;
quit;

proc reg data=Regdata;
	by TICKER;
	model RETRF=MKTRF SMB HML UMD;
quit;
