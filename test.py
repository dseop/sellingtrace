import sqlite3
con = sqlite3.connect("rank_DB.db")
c = con.cursor()

c.execute("")

"""
create table if not exists 'rank_economy_2' ('rank_num' integer, 'code' integer, 'collect_date' text, 'rank_var' integer); 
create table if not exists 'rank_economy_ebiz_2' ('rank_num' integer, 'code' integer, 'collect_date' text, 'rank_var' integer);
create table if not exists 'rank_humanities_2' ('rank_num' integer, 'code' integer, 'collect_date' text, 'rank_var' integer);
create table if not exists 'rank_economy_invest_2' ('rank_num' integer, 'code' integer, 'collect_date' text, 'rank_var' integer);

INSERT INTO rank_economy_2 SELECT rank_num, code, collect_date, rank_var FROM rank_economy;
INSERT INTO rank_economy_ebiz_2 SELECT rank_num, code, collect_date, rank_var FROM rank_economy_ebiz;
INSERT INTO rank_humanities_2 SELECT rank_num, code, collect_date, rank_var FROM rank_humanities;
INSERT INTO rank_economy_invest_2 SELECT rank_num, code, collect_date, rank_var FROM rank_economy_invest;

DROP TABLE rank_economy;
DROP TABLE rank_economy_invest;
DROP TABLE rank_economy_ebiz;
DROP TABLE rank_humanities;

ALTER TABLE rank_economy_invest RENAME TO rank_economy_invest_temp ;
ALTER TABLE rank_economy_ebiz RENAME TO rank_economy_ebiz_temp ;
ALTER TABLE rank_humanities RENAME TO rank_humanities_temp ;

ALTER TABLE rank_economy_2 RENAME TO rank_economy ;
ALTER TABLE rank_economy_invest_2 RENAME TO rank_economy_invest ;
ALTER TABLE rank_economy_ebiz_2 RENAME TO rank_economy_ebiz ;
ALTER TABLE rank_humanities_2 RENAME TO rank_humanities ;

ALTER TABLE Locations RENAME COLUMN Address TO Street;
"""

con.commit()
con.close()