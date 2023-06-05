CREATE TABLE dim_country (
    country_iso3 VARCHAR(3) NOT NULL PRIMARY KEY,
    country_name VARCHAR(50) NOT NULL,
	mcc INT NOT NULL
);

CREATE TABLE dim_sim (
    inventory_id INT NOT NULL PRIMARY KEY,
    company_name VARCHAR(50) NOT NULL
);

CREATE TABLE fct_cdr (
    cdr_id VARCHAR(36) NOT NULL PRIMARY KEY,
    icc_id VARCHAR(20) NOT NULL,
	inventory_id INT NOT NULL REFERENCES dim_sim(inventory_id),
    type VARCHAR(10) NOT NULL,
    connect_time TIMESTAMP NOT NULL,
    close_time TIMESTAMP NOT NULL,
    duration BIGINT NOT NULL CHECK (DURATION >= 0),
    direction VARCHAR(10),
    called_party VARCHAR(15),
    calling_party VARCHAR(15),
    country_iso3 VARCHAR(3) NOT NULL REFERENCES dim_country(country_iso3),
    mnc VARCHAR(3) NOT NULL,
    imsi_id INT NOT NULL,
    imsi_no VARCHAR(15) NOT NULL
);

CREATE INDEX idx_dim_sim ON fct_cdr(inventory_id);
CREATE INDEX idx_dim_country ON fct_cdr(country_iso3);
