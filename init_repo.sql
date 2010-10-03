-- ������������ ���������
CREATE TABLE "user" (
    "name" TEXT PRIMARY KEY NOT NULL, -- ��� (�����) ������������
    "password" TEXT NOT NULL, -- ����� ���� ������ ������, �� �� NULL
    "notes" TEXT, -- �����������, ������� � ������������, ��� ��������
    "group" TEXT NOT NULL DEFAULT 'USER' -- ������ ���������� ����� ������������. ��������: USER, ADMIN
);

-- ������� (������, ������) ��������� ������
CREATE TABLE "item" (
	"id" INTEGER PRIMARY KEY NOT NULL, 
	"name" TEXT NOT NULL, 
	"notes" TEXT, 
	"user_name" TEXT, -- ������������-�������� (��� ������ �������)
	FOREIGN KEY ("user_name") REFERENCES "user"("name")
);

-- ������ �� ����������� ��������� ���������� (������)
CREATE TABLE "data" (
    "url" TEXT PRIMARY KEY NOT NULL, -- ��� ���� � ����� �������. ����� ���������, ��� URL ������� ��������
    "hash" TEXT, -- ��� �� ����������� �����, NULL ��� url-������
    "date_hashed" INTEGER, -- ����/����� ���������� ����
    "size" INTEGER NOT NULL DEFAULT 0, -- ������ ����� � ������, ��� url ������ ����� ����
    "order_key" INTEGER, -- ���� ��� ���������� � �������� ������ object-�
	"item_id" INTEGER, -- id �������-���������. ����� ���� ����� � NULL
	"user_name" TEXT, -- ������������, ������� ������� ����/url � ���������. ����� ���� NULL, ����� ��� "�����" ����/url
	FOREIGN KEY ("item_id") REFERENCES "item"("id"),
	FOREIGN KEY ("user_name") REFERENCES "user"("name")
);

-- ��� (�������� �����)
CREATE TABLE "tag" (
    "name" TEXT NOT NULL,		-- ��� ����
    "user_name" TEXT NOT NULL,	-- ������������-�������� ����
    "synonym_id" INTEGER,		-- id ������ ���������. ��� ���� ������� ���������� ��-NULL �������� ����� ���� ��������� ����������
    PRIMARY KEY ("name", "user_name"),
	FOREIGN KEY ("user_name") REFERENCES "user"("name")
);

-- ���� ���� ����=�������� --
CREATE TABLE "field" (
    "name" TEXT NOT NULL,
    "user_name" TEXT NOT NULL,
    "value_type" TEXT NOT NULL DEFAULT 'STRING', -- ��� ������ ����. ��������: STRING, NUMBER --
    "synonym_id" INTEGER,
	PRIMARY KEY ("name", "user_name"),
	FOREIGN KEY ("user_name") REFERENCES "user"("name")
);

-- ����� ����� item � field �����-��-������ --
CREATE TABLE "item_field" (
    "item_id" TEXT NOT NULL,
    "field_name" TEXT NOT NULL,
    "field_user_name" TEXT NOT NULL,
    "field_value" TEXT NOT NULL,
	PRIMARY KEY ("item_id", "field_name", "field_user_name"),
	FOREIGN KEY ("item_id")  REFERENCES "item"("id"),
	FOREIGN KEY ("field_name", "field_user_name") REFERENCES "field"("name", "user_name")
);

-- ����� ����� item � tag �����-��-������ --
CREATE TABLE "item_tag" (
    "item_id" INTEGER NOT NULL,
    "tag_name" TEXT NOT NULL,
    "tag_user_name" TEXT NOT NULL,
	PRIMARY KEY ("item_id", "tag_name", "tag_user_name"),
	FOREIGN KEY ("item_id")  REFERENCES "item"("id"),
	FOREIGN KEY ("tag_name", "tag_user_name") REFERENCES "tag"("name", "user_name")
);

-- ������ �����/�����. ������������ ����� ������������� ������ ���� ������ 
-- �� ��������� � ��� ����� ��� ���� ��� � ����� ���� � ����
CREATE TABLE "bundle" (
    "name" TEXT NOT NULL,
    "user_name" TEXT NOT NULL,
    "notes" TEXT,
	PRIMARY KEY ("name", "user_name"),
	FOREIGN KEY ("user_name") REFERENCES "user"("name")
);

-- ����� ����� bundle � tag �����-��-������
CREATE TABLE "bundle_tag" (
    "bundle_name" TEXT NOT NULL,
    "bundle_user_name" TEXT NOT NULL,
    "tag_name" TEXT NOT NULL,
    "tag_user_name" TEXT NOT NULL,
	PRIMARY KEY ("bundle_name", "bundle_user_name",  "tag_name", "tag_user_name") ,
	FOREIGN KEY ("bundle_name", "bundle_user_name") REFERENCES "bundle"("name", "user_name"),
	FOREIGN KEY ("tag_name", "tag_user_name") REFERENCES "tag"("name", "user_name")
);

-- ����� ����� bundle � field �����-��-������
CREATE TABLE "bundle_field" (
    "bundle_name" TEXT NOT NULL,
    "bundle_user_name" TEXT NOT NULL,
    "field_name" TEXT NOT NULL,
    "field_user_name" TEXT NOT NULL,
	PRIMARY KEY ("bundle_name", "bundle_user_name", "field_name", "field_user_name"),
	FOREIGN KEY ("bundle_name", "bundle_user_name") REFERENCES "bundle"("name", "user_name"),
	FOREIGN KEY ("field_name", "field_user_name") REFERENCES "field"("name", "user_name")
);

