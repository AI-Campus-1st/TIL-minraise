CREATE DATABASE IF NOT EXISTS fsc_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

USE fsc_db;

CREATE TABLE IF NOT EXISTS raw_item (
    raw_id        BIGINT AUTO_INCREMENT PRIMARY KEY,
    source        VARCHAR(50)  NOT NULL COMMENT '출처: fsc_api',
    url           TEXT                  COMMENT '요청 주소',
    collected_at  DATETIME     NOT NULL COMMENT '수집 시각',
    payload       LONGTEXT     NOT NULL COMMENT '원문 그대로',
    content_hash  CHAR(64)     NOT NULL COMMENT '중복 판정 스티커',

    UNIQUE KEY uq_hash (content_hash),         -- 같은 스티커는 하나만!
    KEY idx_source_date (source, collected_at)  -- 빨리 찾기용 색인
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
