# Generated by Django 3.0.4 on 2020-03-22 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MysqlView',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='序号')),
                ('accountname', models.CharField(max_length=64, verbose_name='科目名')),
                ('amount', models.FloatField(verbose_name='实际金额')),
                ('amount_0', models.FloatField(verbose_name='预算金额')),
                ('companyname', models.CharField(max_length=64, verbose_name='公司名')),
                ('accountdate', models.DateField(verbose_name='会计日期')),
                ('versionname', models.CharField(max_length=64, verbose_name='版本号')),
                ('typename', models.CharField(max_length=30, verbose_name='科目类别')),
                ('currencyname', models.CharField(max_length=10, verbose_name='币种')),
                ('buname', models.CharField(max_length=30, verbose_name='板块')),
                ('companycode', models.CharField(max_length=10, verbose_name='公司编码')),
                ('submittdate', models.DateTimeField(verbose_name='提报日期')),
                ('ytdactual', models.FloatField(verbose_name='实际累计')),
                ('ytdbudget', models.FloatField(verbose_name='预算累计')),
            ],
            options={
                'verbose_name_plural': '经营分析主要指标表',
                'db_table': 'mysqlview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=64, unique=True, verbose_name='科目类别')),
            ],
            options={
                'verbose_name_plural': '科目类别维护',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buname', models.CharField(max_length=64, unique=True, verbose_name='板块')),
            ],
            options={
                'verbose_name_plural': '板块维护',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('companycode', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='公司编码')),
                ('companyname', models.CharField(max_length=64, verbose_name='公司名')),
                ('parentcompany', models.BooleanField(default=True, verbose_name='父级公司')),
                ('isvalid', models.BooleanField(default=True, verbose_name='有效标记')),
                ('bu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='collector.BusinessUnit')),
            ],
            options={
                'verbose_name_plural': '公司维护',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currencyname', models.CharField(max_length=10, unique=True, verbose_name='记账币')),
            ],
            options={
                'verbose_name_plural': '币种维护',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('submittdate', models.DateTimeField(auto_now_add=True, verbose_name='提交日期')),
                ('accountdate', models.DateField(verbose_name='会计期间')),
                ('isvalid', models.BooleanField(default=True, verbose_name='有效标记')),
                ('versionname', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='版本ID')),
                ('vaild', models.BooleanField(verbose_name='**')),
                ('companycode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.Company')),
            ],
            options={
                'verbose_name_plural': '版本管理',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('userid', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='员工号')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='电子邮件')),
                ('companycode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.Company')),
            ],
            options={
                'verbose_name_plural': '用户维护',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodrate', models.FloatField(verbose_name='期间汇率')),
                ('pointrate', models.FloatField(verbose_name='即时汇率')),
                ('currencydate', models.DateField(verbose_name='汇率日期')),
                ('aftercur', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aft_cur', to='collector.Currency')),
                ('originalcur', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ori_cur', to='collector.Currency')),
            ],
            options={
                'verbose_name_plural': '汇率维护',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='com_cur', to='collector.Currency'),
        ),
        migrations.CreateModel(
            name='AccountBg',
            fields=[
                ('accountid', models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='科目编码')),
                ('accountname', models.CharField(max_length=128, verbose_name='科目名称')),
                ('displayname', models.CharField(max_length=128, null=True, verbose_name='显示名称')),
                ('parentaccount', models.BooleanField(default=False, verbose_name='父级科目')),
                ('isvalid', models.BooleanField(default=True, verbose_name='有效标记')),
                ('accounttypeid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.AccountType')),
            ],
            options={
                'verbose_name_plural': '科目维护',
            },
        ),
        migrations.CreateModel(
            name='YtdData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ytdactual', models.FloatField(default=0, verbose_name='实际累计')),
                ('ytdbudget', models.FloatField(default=0, verbose_name='预算累计')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.Version')),
                ('ytdaccount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.AccountBg')),
            ],
            options={
                'verbose_name_plural': '累计数',
                'unique_together': {('version', 'ytdaccount')},
            },
        ),
        migrations.CreateModel(
            name='BudgetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=0, verbose_name='预算数')),
                ('accountid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.AccountBg')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Version')),
            ],
            options={
                'verbose_name_plural': '预算数',
                'unique_together': {('version', 'accountid')},
            },
        ),
        migrations.CreateModel(
            name='ActualData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0, verbose_name='实际数')),
                ('accountid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collector.AccountBg')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Version')),
            ],
            options={
                'verbose_name_plural': '实际发生数',
                'unique_together': {('version', 'accountid')},
            },
        ),
    ]
