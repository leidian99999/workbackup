use �������ݸ���



alter table dbo.[3.8] add ������  int
alter table dbo.[3.8] add ǩ���� int
alter table dbo.[3.8] add ������ int
alter table dbo.[3.8] add �������� int

alter table dbo.[3.8] add ����ʡ varchar(255)
alter table dbo.[3.8] add ������ varchar(255)
alter table dbo.[3.8] add ��Ʒ���� varchar(255)
alter table dbo.[3.8] add ����ʱЧ varchar(255)
alter table dbo.[3.8] add �Ա�  varchar(255)

alter table dbo.[3.8] add ǩ��ʱЧ varchar(255)
alter table dbo.[3.8] add ����ʱЧ varchar(255)
alter table dbo.[3.8] add ����  int
alter table dbo.[3.8] add ����ʱЧ varchar(255)

alter table dbo.[2.1-2.15����-2.16ȡ] add �������� varchar(255)

alter table dbo.[3.8] add ���¼����� int
alter table dbo.[3.8] add ���ϼ����� int


alter table dbo.[7������-8��23��ȡ] add ���Ա varchar(255)
alter table dbo.[7������-8��23��ȡ] add ���Ա�绰 varchar(255)


alter table dbo.[3.8] add 8����Ӫ�� varchar(255)
alter table dbo.[3.8] add �Ŷ� varchar(255)

alter table dbo.[ƥ�������] add ʮ�³����� varchar(255)
alter table dbo.[ͨѶ��Ϣթƭ����] add ���¶������ varchar(255)
alter table dbo.[ͨѶ��Ϣթƭ����] add ���¶�����Դ varchar(255)
alter table dbo.[ͨѶ��Ϣթƭ����] add �����ջ���ַ varchar(255)
alter table dbo.[ͨѶ��Ϣթƭ����] add ʮ���ջ���ַ varchar(255)

alter table  dbo.[10.1-10.22���¼����] add ����ʱЧ varchar(255)
alter table dbo.[11������-12.24ȡ] add ���еȼ� varchar(255)

alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)
alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)
alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)

alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)
alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)
alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)

alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)
alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)
alter table dbo.[����ID��ֵ�ɹ���ϸ] add ���� varchar(255)



update dbo.[3.8]
set ������=
case 
when ��������!='' then 1
when ��������='' and ����״̬='�������' then 1
when ��������='' and ����ǩ��ʱ��!='' then 1
else 0
end
/*������*/

update dbo.[3.8]
set ǩ����=
case 
when ����ǩ��ʱ��!='' then 1
when ����ǩ��ʱ��='' and ����״̬='�������' then 1
else 0
end
/*ǩ����*/

update dbo.[3.8]
set ������=
case 
when ����״̬='�������' then 1
else 0
end
/*������*/

update dbo.[3.8]
set ��������=
case 
when ������=0 and �Ƿ�����ת����!='��'  AND ������ע not like '%��Ҫ%' and ������ע not like '%����Ҫ%' and ����״̬='������Ϣ���ʧ��'  then 1
when ������=0 and �Ƿ�����ת����!='��'  AND ������ע not like '%��Ҫ%' and ������ע not like '%����Ҫ%' and ����״̬='�����ر�' and ��������ԭ��!='' then 1
when ������=0 and �Ƿ�����ת����!='��'  AND ������ע not like '%��Ҫ%' and ������ע not like '%����Ҫ%' and ����״̬='�����ر�' and ��������ԭ��='' and ������ע!='' and ������ע not like '%�·�%' then 1
when ������=0 and �Ƿ�����ת����!='��'  AND ������ע not like '%��Ҫ%' and ������ע not like '%����Ҫ%' and ����״̬='ϵͳ��˶���' and ��������ԭ��!='' then 1
else 0
end
/*��������*/

update dbo.[3.8]
set ��������=
case 
when ������=0 and ��������ԭ��='' and ����״̬='������Ϣ���ʧ��' then 1
when ������=0 and ��������ԭ��!='' then 1
when ������=0 and ��������ԭ��='' and ����״̬='��ݳ���ʧ��' then 1
else 0
end
/*��������*/

update dbo.[3.8]
set ����ʡ=SUBSTRING(���������,1,(CHARINDEX('/',���������)-1)) 
/*����ʡ*/
update dbo.[3.8]
set ������=SUBSTRING(���������,(CHARINDEX('/',���������)+1),100) 
/*������*/


update dbo.[2.1-2.15����-2.16ȡ]
set ��������='A'+�������
/*��������*/


update dbo.[3.8]
set ��Ʒ����=dbo.[�꿨��].���� from dbo.[�꿨��] where dbo.[�꿨��].����Ʒ���=dbo.[3.8].����Ʒ���
/*��Ʒ����*/




update dbo.[3.8]
set ���¼�����=
case 
when �Ƿ�����ģʽ='��' AND ����״̬='�������' AND �Ƿ�����ת����!='��' then 1
else 0
end
/*���¼�����*/

update dbo.[3.8]
set ���ϼ�����=
case 
when �Ƿ�����ģʽ='��' AND ����״̬='�������' AND �Ƿ�����ת����='��' then 1
WHEN �Ƿ�����ģʽ!='��' AND ����״̬='�������' then 1
else 0
end
/*���ϼ�����*/





update dbo.[3.8]
set ����ʱЧ=DATEDIFF(DD, ��������ʱ��, �������ʱ��)
/*����ʱЧ*/

update dbo.[3.8]
set ǩ��ʱЧ=DATEDIFF(DD, ��������ʱ��, ����ǩ��ʱ��)
/*ǩ��ʱЧ*/

update dbo.[3.8]
set ����ʱЧ=DATEDIFF(DD, ��������ʱ��,����ʱ��)
/*����ʱЧ*/

update dbo.[3.8]
set ����ʱЧ=DATEDIFF(DD, ����ʱ��, ����ǩ��ʱ��)
/*����ʱЧ*/


update dbo.[3.8]
set ������������=substring(��������ʱ��,1,10)
/*������������*/

update dbo.[3.8]
set ��������ʱ��=substring (��������ʱ��,12,2)
/*��������ʱ��*/

update dbo.[3.8]
set ���������·�=substring (��������ʱ��,6,2)
/*���������·�*/

update dbo.[3.8]
set �����������=substring (��������ʱ��,1,4)
/*�����������*/


update dbo.[7������-8��23��ȡ]
set ���Ա=dbo.[7�������켣].�ɼ������� from dbo.[7�������켣] where dbo.[7�������켣].�������=dbo.[7������-8��23��ȡ].�������
/*���Ա*/


update dbo.[7������-8��23��ȡ]
set ���Ա�绰=dbo.[7�������켣].�ɼ��˵绰 from dbo.[7�������켣] where dbo.[7�������켣].�������=dbo.[7������-8��23��ȡ].�������
/*���Ա�绰*/