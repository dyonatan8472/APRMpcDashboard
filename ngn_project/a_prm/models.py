from django.db import models


# Create your models here.
class PrmDatErrMngr(models.Model):
    err_seq_num = models.IntegerField(primary_key=True)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    iecd = models.CharField(max_length=4, blank=True, null=True)
    ins_date = models.DateField(blank=True, null=True)
    err_severity = models.IntegerField(blank=True, null=True)
    recycle_cntr = models.IntegerField(blank=True, null=True)
    file_tp = models.CharField(max_length=30, blank=True, null=True)
    dominant_err_cd = models.CharField(max_length=4, blank=True, null=True)
    err_cd_2 = models.CharField(max_length=4, blank=True, null=True)
    err_cd_3 = models.CharField(max_length=4, blank=True, null=True)
    err_cd_4 = models.CharField(max_length=4, blank=True, null=True)
    phy_file_id = models.IntegerField(blank=True, null=True)
    originating_id = models.CharField(max_length=20, blank=True, null=True)
    terminating_id = models.CharField(max_length=20, blank=True, null=True)
    event_start_datetime = models.DateField(blank=True, null=True)
    event_direction = models.CharField(max_length=1, blank=True, null=True)
    ext_trunk = models.CharField(max_length=10, blank=True, null=True)
    carrier_cd = models.CharField(max_length=20, blank=True, null=True)
    elmnt_cd = models.CharField(max_length=8, blank=True, null=True)
    jurisdiction = models.CharField(max_length=1, blank=True, null=True)
    future_1 = models.CharField(max_length=20, blank=True, null=True)
    future_2 = models.CharField(max_length=20, blank=True, null=True)
    future_3 = models.CharField(max_length=20, blank=True, null=True)
    seq_label = models.CharField(max_length=2, blank=True, null=True)
    generated_rec = models.IntegerField()
    session_id = models.CharField(max_length=20, blank=True, null=True)
    prod_cat_id = models.CharField(max_length=2, blank=True, null=True)
    prod_id = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    chrg_param_1_val = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    chrg_param_2_val = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    chrg_param_3_val = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    uom_1 = models.CharField(max_length=2, blank=True, null=True)
    uom_2 = models.CharField(max_length=2, blank=True, null=True)
    uom_3 = models.CharField(max_length=2, blank=True, null=True)
    nr_param_1_val = models.CharField(max_length=20, blank=True, null=True)
    nr_param_2_val = models.CharField(max_length=20, blank=True, null=True)
    nr_param_3_val = models.CharField(max_length=20, blank=True, null=True)
    nr_param_4_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_1_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_2_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_3_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_4_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_5_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_6_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_7_val = models.CharField(max_length=20, blank=True, null=True)
    billing_pct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bill_in_advance = models.CharField(max_length=1, blank=True, null=True)
    total_bill_days = models.IntegerField(blank=True, null=True)
    daily_ind = models.CharField(max_length=1, blank=True, null=True)
    one_time_chrg_ind = models.CharField(max_length=1, blank=True, null=True)
    num_of_days = models.IntegerField(blank=True, null=True)
    chrg_direction = models.CharField(max_length=1, blank=True, null=True)
    rate_plan_cd = models.CharField(max_length=20, blank=True, null=True)
    destination_cd = models.CharField(max_length=5, blank=True, null=True)
    tax_set_cd = models.CharField(max_length=2, blank=True, null=True)
    rate_class_set_cd = models.CharField(max_length=4, blank=True, null=True)
    process_datetime = models.DateField(blank=True, null=True)
    agreement_id = models.IntegerField(blank=True, null=True)
    elmnt_cat_id = models.IntegerField(blank=True, null=True)
    undo_ind = models.CharField(max_length=1, blank=True, null=True)
    rerate_ind = models.CharField(max_length=1, blank=True, null=True)
    rerate_cnt = models.IntegerField(blank=True, null=True)
    rerate_invcn_cd = models.CharField(max_length=9, blank=True, null=True)
    event_chrg_tp = models.CharField(max_length=1, blank=True, null=True)
    qual_param_1_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_2_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_3_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_4_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_5_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_6_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_7_set_cd = models.CharField(max_length=4, blank=True, null=True)
    rpu_rate_cd_seq_1 = models.IntegerField(blank=True, null=True)
    rpu_rate_cd_seq_2 = models.IntegerField(blank=True, null=True)
    rpu_rate_cd_seq_3 = models.IntegerField(blank=True, null=True)
    ac_rate_cd_seq_1 = models.IntegerField(blank=True, null=True)
    ac_rate_cd_seq_2 = models.IntegerField(blank=True, null=True)
    ac_rate_cd_seq_3 = models.IntegerField(blank=True, null=True)
    orig_chrg_param_val_1 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_chrg_param_val_2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_chrg_param_val_3 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    acces_chrg_1 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    acces_chrg_2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    acces_chrg_3 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    usage_chrg_1 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    usage_chrg_2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    usage_chrg_3 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    num_of_rate_seg = models.NullBooleanField()
    num_of_orig_param = models.IntegerField(blank=True, null=True)
    num_of_adu_param = models.IntegerField(blank=True, null=True)
    size_of_orig_param = models.IntegerField(blank=True, null=True)
    size_of_adu = models.IntegerField(blank=True, null=True)
    rate_segments = models.CharField(max_length=2000, blank=True, null=True)
    orig_param = models.CharField(max_length=2000, blank=True, null=True)
    adu = models.CharField(max_length=4000, blank=True, null=True)
    rec_handle_ind = models.CharField(max_length=1)
    next_process_ind = models.CharField(max_length=1, blank=True, null=True)
    service_id = models.BigIntegerField(blank=True, null=True)
    content_grp_cd = models.CharField(max_length=20, blank=True, null=True)
    edr_id = models.IntegerField(blank=True, null=True)
    dup_pass_ind = models.CharField(max_length=1, blank=True, null=True)
    orig_event_start_datetime = models.DateField(blank=True, null=True)
    au_id_1 = models.IntegerField(blank=True, null=True)
    au_id_2 = models.IntegerField(blank=True, null=True)
    au_id_3 = models.IntegerField(blank=True, null=True)
    calc_acces_chrg = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    calc_usage_chrg = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_tot_acces_chrg_1 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_tot_acces_chrg_2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_tot_acces_chrg_3 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_tot_usage_chrg_1 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_tot_usage_chrg_2 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    orig_tot_usage_chrg_3 = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    commsn_sequences = models.CharField(max_length=4000, blank=True, null=True)
    accountable_values = models.CharField(max_length=4000, blank=True, null=True)
    eligible_values = models.CharField(max_length=4000, blank=True, null=True)
    orig_process_date = models.DateField(blank=True, null=True)
    upd_user_name = models.CharField(max_length=254, blank=True, null=True)
    future_4 = models.CharField(max_length=20, blank=True, null=True)
    future_5 = models.CharField(max_length=20, blank=True, null=True)
    future_6 = models.CharField(max_length=20, blank=True, null=True)
    future_7 = models.CharField(max_length=20, blank=True, null=True)
    future_8 = models.CharField(max_length=20, blank=True, null=True)
    future_9 = models.CharField(max_length=20, blank=True, null=True)
    future_10 = models.CharField(max_length=20, blank=True, null=True)
    future_11 = models.CharField(max_length=50, blank=True, null=True)
    future_12 = models.CharField(max_length=50, blank=True, null=True)
    future_13 = models.CharField(max_length=50, blank=True, null=True)
    future_14 = models.CharField(max_length=50, blank=True, null=True)
    future_15 = models.CharField(max_length=50, blank=True, null=True)
    qual_param_8_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_9_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_10_val = models.CharField(max_length=20, blank=True, null=True)
    qual_param_8_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_9_set_cd = models.CharField(max_length=4, blank=True, null=True)
    qual_param_10_set_cd = models.CharField(max_length=4, blank=True, null=True)
    account_cd = models.CharField(max_length=20, blank=True, null=True)
    rank1_account_cd = models.CharField(max_length=20, blank=True, null=True)
    account_type_cd = models.CharField(max_length=20, blank=True, null=True)
    business_unit_cd = models.CharField(max_length=20, blank=True, null=True)
    account_start_date = models.DateField(blank=True, null=True)
    account_end_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20, blank=True, null=True)
    core_reserved_1 = models.CharField(max_length=1, blank=True, null=True)
    core_reserved_2 = models.CharField(max_length=20, blank=True, null=True)
    core_reserved_3 = models.CharField(max_length=20, blank=True, null=True)
    asset_cd = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prm_dat_err_mngr'


class DmsDealDtl(models.Model):
    deal_id = models.CharField(primary_key=True, max_length=20)
    offer_code = models.CharField(max_length=20)
    service_type = models.CharField(max_length=3)
    deal_start_date = models.DateField()
    deal_type = models.CharField(max_length=1)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    contract_period = models.CharField(max_length=2, blank=True, null=True)
    customer_cib = models.DecimalField(
        max_digits=18, decimal_places=5, blank=True, null=True)
    component_cost = models.DecimalField(
        max_digits=18, decimal_places=5, blank=True, null=True)
    deal_end_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_deal_dtl'
        unique_together = (('deal_id', 'offer_code', 'service_type',
                            'deal_start_date', 'deal_type', 'tenant_cd'),)


class DmsActvDtl(models.Model):
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    dealer_code = models.CharField(max_length=20)
    msisdn = models.CharField(primary_key=True, max_length=20)
    offer_code = models.CharField(max_length=20)
    ser_type = models.CharField(max_length=3)
    trans_type = models.CharField(max_length=1)
    actv_date = models.DateField()
    new_ret_date = models.DateField()
    effective_date = models.DateField()
    contract_dur = models.CharField(max_length=2, blank=True, null=True)
    last_ret_date = models.DateField(blank=True, null=True)
    imie_number = models.CharField(max_length=20, blank=True, null=True)
    sim_seq_num = models.CharField(max_length=20, blank=True, null=True)
    sub_dealer_code = models.CharField(max_length=20, blank=True, null=True)
    commsn_paid_ind = models.CharField(max_length=1, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    edr_id = models.IntegerField()
    partition_id = models.IntegerField()
    deal_id = models.CharField(max_length=20)
    onceoff_dealer_cd = models.CharField(max_length=20, blank=True, null=True)
    old_ser_type = models.CharField(max_length=3, blank=True, null=True)
    old_offer_cd = models.CharField(max_length=20, blank=True, null=True)
    old_dealer_cd = models.CharField(max_length=20, blank=True, null=True)
    billing_period = models.DateField(blank=True, null=True)
    comm_mdcode = models.CharField(max_length=20, blank=True, null=True)
    comm_sdcode = models.CharField(max_length=20, blank=True, null=True)
    comm_rocode = models.CharField(max_length=20, blank=True, null=True)
    old_msisdn = models.CharField(max_length=20, blank=True, null=True)
    old_iccid = models.CharField(max_length=20, blank=True, null=True)
    order_id = models.CharField(max_length=20, blank=True, null=True)
    order_action_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dms_actv_dtl'
        unique_together = (('msisdn', 'effective_date',
                            'partition_id', 'trans_type'),)


class DmsPrepAccUsg(models.Model):
    msisdn = models.CharField(primary_key=True, max_length=20)
    bp_start_date = models.DateField()
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    acc_usage = models.DecimalField(
        max_digits=18, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dms_prep_acc_usg'
        unique_together = (('msisdn', 'bp_start_date'),)


class PrmAccounts(models.Model):
    account_cd = models.CharField(primary_key=True, max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    opt_lock = models.IntegerField()
    description = models.CharField(max_length=400, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    user_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'prm_accounts'


class PrmAccBusinessDtls(models.Model):
    account_cd = models.CharField(primary_key=True, max_length=20)
    effective_date = models.DateField()
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    status_cd = models.CharField(max_length=4)
    opt_lock = models.IntegerField()
    business_unit_cd = models.CharField(max_length=20)
    account_type_cd = models.CharField(max_length=20, blank=True, null=True)
    rank1_account_cd = models.CharField(max_length=20)
    parent_account_cd = models.CharField(max_length=20, blank=True, null=True)
    performance_type = models.CharField(max_length=20, blank=True, null=True)
    manager_account_cd = models.CharField(max_length=20, blank=True, null=True)
    status_ind = models.CharField(max_length=1)
    expiration_date = models.DateField()
    reason_cd = models.CharField(max_length=20, blank=True, null=True)
    reason_desc = models.CharField(max_length=1000, blank=True, null=True)
    partner_profile_cd = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=1, blank=True, null=True)
    payment_id = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prm_acc_business_dtls'
        unique_together = (('account_cd', 'effective_date'),)


class PrmUsers(models.Model):
    user_cd = models.CharField(primary_key=True, max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    opt_lock = models.IntegerField()
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    e_mail = models.CharField(max_length=400)
    primary_phone_no = models.CharField(max_length=150)
    tenant_cd = models.CharField(max_length=20)
    org_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prm_users'


class PrmAccFinancialDtls(models.Model):
    account_cd = models.CharField(primary_key=True, max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    opt_lock = models.IntegerField()
    bank_account_no = models.CharField(max_length=300, blank=True, null=True)
    bank_account_name = models.CharField(max_length=400, blank=True, null=True)
    bank_code = models.CharField(max_length=40, blank=True, null=True)
    bank_name = models.CharField(max_length=400, blank=True, null=True)
    bank_branch = models.CharField(max_length=150, blank=True, null=True)
    tax_registration_no = models.CharField(max_length=150, blank=True, null=True)
    gl_cr_cd = models.CharField(max_length=20, blank=True, null=True)
    gl_dr_cd = models.CharField(max_length=20, blank=True, null=True)
    deposit_value = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    deposit_threshold = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    bp_set_cd = models.CharField(max_length=4, blank=True, null=True)
    billing_cycle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prm_acc_financial_dtls'


class PrmAccContactDtls(models.Model):
    account_cd = models.CharField(primary_key=True, max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    opt_lock = models.IntegerField()
    secondary_phone_no = models.CharField(max_length=150, blank=True, null=True)
    fax = models.CharField(max_length=150, blank=True, null=True)
    address_line_1 = models.CharField(max_length=300, blank=True, null=True)
    address_line_2 = models.CharField(max_length=300, blank=True, null=True)
    address_line_3 = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=300, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    zip = models.CharField(max_length=150, blank=True, null=True)
    po_box = models.CharField(max_length=150, blank=True, null=True)
    web_site = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prm_acc_contact_dtls'


class DmsDealComm(models.Model):
    deal_id = models.CharField(primary_key=True, max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    dealr_cib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    dlr_addl_cib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    dlr_sales_agr = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    ata_reward_card = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    discount = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    special_deal = models.CharField(max_length=1, blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_deal_comm'
        unique_together = (('deal_id', 'tenant_cd'),)


class DmsDealCommRib(models.Model):
    deal_id = models.CharField(primary_key=True, max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    dealer_rib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    dlr_addl_rib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    dlr_sales_agr_rib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    ata_reward_card_rib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    discount_rib = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    special_deal = models.CharField(max_length=1, blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_deal_comm_rib'
        unique_together = (('deal_id', 'tenant_cd'),)


class DmsDealMap(models.Model):
    dealer_cd = models.CharField(primary_key=True, max_length=20)
    deal_id = models.CharField(max_length=20)
    effective_date = models.DateField()
    deal_type = models.CharField(max_length=1)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1)
    account_status = models.CharField(max_length=1)
    expiration_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_deal_map'
        unique_together = (('dealer_cd', 'deal_id', 'effective_date', 'deal_type', 'tenant_cd'),)


class DmsHybridRates(models.Model):
    effective_date = models.DateField(primary_key=True)
    commsn_cd = models.CharField(max_length=20)
    dealer_cd = models.CharField(max_length=20)
    deal_id = models.CharField(max_length=20)
    charge_cd = models.CharField(max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    commsn_rate = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_hybrid_rates'
        unique_together = (('effective_date', 'commsn_cd', 'dealer_cd', 'deal_id', 'charge_cd', 'tenant_cd'),)


class DmsPostpaidRates(models.Model):
    effective_date = models.DateField(primary_key=True)
    commsn_cd = models.CharField(max_length=20)
    dealer_cd = models.CharField(max_length=20)
    deal_id = models.CharField(max_length=20)
    charge_cd = models.CharField(max_length=20)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    commsn_rate = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_postpaid_rates'
        unique_together = (('effective_date', 'commsn_cd', 'dealer_cd', 'deal_id', 'charge_cd', 'tenant_cd'),)


class DmsPreHybRates(models.Model):
    effective_date = models.DateField(primary_key=True)
    commsn_cd = models.CharField(max_length=20)
    dealer_cd = models.CharField(max_length=20)
    deal_id = models.CharField(max_length=20)
    from_slab = models.DecimalField(max_digits=18, decimal_places=5)
    to_slab = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    commsn_rate = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dms_pre_hyb_rates'
        unique_together = (('effective_date', 'commsn_cd', 'dealer_cd', 'deal_id', 'from_slab', 'tenant_cd'),)


class IcSubjectVersions(models.Model):
    subject = models.CharField(primary_key=True, max_length=400)
    code = models.CharField(max_length=400)
    effective_date = models.DateField()
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    remark_seq_no = models.IntegerField(blank=True, null=True)
    status_cd = models.CharField(max_length=4, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    tenant_cd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ic_subject_versions'
        unique_together = (('subject', 'code', 'effective_date'),)


class SecUser(models.Model):
    user_id = models.CharField(primary_key=True, max_length=120)
    cf_creation_date = models.DateField(blank=True, null=True)
    cf_update_date = models.DateField(blank=True, null=True)
    cf_update_principal_name = models.CharField(max_length=120, blank=True, null=True)
    cf_application_id = models.CharField(max_length=120, blank=True, null=True)
    cf_host = models.CharField(max_length=120, blank=True, null=True)
    cf_additional_info = models.CharField(max_length=32, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField(blank=True, null=True)
    last_login_date = models.DateField(blank=True, null=True)
    last_bad_login_date = models.DateField(blank=True, null=True)
    bad_login_counter = models.BigIntegerField(blank=True, null=True)
    user_flags = models.BigIntegerField(blank=True, null=True)
    cred_expiration_date = models.DateField(blank=True, null=True)
    user_locked = models.NullBooleanField()
    user_disabled = models.NullBooleanField()
    user_active = models.NullBooleanField()
    parent_user_id = models.CharField(max_length=120, blank=True, null=True)
    ser_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sec_user'


class PrmFlexReportsStatus(models.Model):
    job_rec = models.IntegerField(primary_key=True)
    flx_rep_cd = models.CharField(primary_key=True, max_length=16)
    generation_date = models.DateField(primary_key=True)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=256)
    pdf_status = models.CharField(max_length=2, blank=True, null=True)
    xml_status = models.CharField(max_length=2, blank=True, null=True)
    csv_status = models.CharField(max_length=2, blank=True, null=True)
    job_status = models.CharField(max_length=2, blank=True, null=True)
    auto_run_ind = models.CharField(max_length=1, blank=True, null=True)
    multi_files_ind = models.CharField(max_length=1, blank=True, null=True)
    row_data_count = models.IntegerField(blank=True, null=True)
    report_seq = models.IntegerField(blank=True, null=True)
    report_arguments = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=True, null=True)
    tenant_cd = models.CharField(max_length=20, blank=True, null=True)
    target_report_server = models.CharField(max_length=50, blank=True, null=True)
    report_mode = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prm_flex_reports_status'
        unique_together = (('job_rec', 'flx_rep_cd', 'generation_date'),)

    list_display = ('job_rec', 'flx_rep_cd', 'generation_date', 'sys_update_date', 'file_name', 'job_status',)


class DmsDealerUpload(models.Model):
    sim_seq_num = models.CharField(primary_key=True, max_length=20)
    ship_ind = models.CharField(primary_key=True, max_length=1)
    ship_date = models.DateField(primary_key=True)
    partition_id = models.IntegerField(primary_key=True)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    actv_dealer_id = models.CharField(max_length=20, blank=True, null=True)
    return_dealer_id = models.CharField(max_length=20, blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    src_ind = models.CharField(max_length=2, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'prm_flex_reports_status'
        unique_together = (('sim_seq_num', 'ship_ind', 'ship_date', 'partition_id'),)


class DmsRechEvtDtl(models.Model):
    msisdn = models.CharField(primary_key=True, max_length=20)
    service_type = models.CharField(max_length=3)
    dealer_cd = models.CharField(max_length=20)
    event_start_date = models.DateField()
    rech_unique_no = models.CharField(max_length=20)
    balance_amount = models.DecimalField(max_digits=18, decimal_places=5)
    sys_creation_date = models.DateField()
    sys_update_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    application_id = models.CharField(max_length=6, blank=True, null=True)
    dl_service_code = models.CharField(max_length=5)
    dl_update_stamp = models.IntegerField(blank=True, null=True)
    iccid = models.CharField(max_length=20, blank=True, null=True)
    rech_amount = models.DecimalField(max_digits=18, decimal_places=5, blank=True, null=True)
    imei = models.CharField(max_length=20, blank=True, null=True)
    offer_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dms_rech_evt_dtl'
        unique_together = (('msisdn', 'event_start_date', 'service_type', 'dealer_cd', 'rech_unique_no', 'balance_amount'),)
