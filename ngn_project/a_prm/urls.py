from django.conf.urls import include, url

from .views import (monitor_processing, load_dealers, load_deals, load_cib, load_rib, update_dealers, update_rech_event_dealers, purge_errors,
                    purge_dm73_by_msisdn, dms_detail_report, dm69_update, agent_details, delete_dealer, actv_detail_report,
                    prus_detail_report, aprm_error_count, detail_error_report, dm40_update, dm27_update,recycle_errors, daemon_status,
                    missing_offers_ids, activity_count, usage_report, report_server_jobs, msisdn_details, get_agent_id)

app_name = 'a_prm'

urlpatterns = [
    url(r'^daemon_status/$', daemon_status, name='daemon_status'),
    url(r'^monitor_processing/$', monitor_processing, name='monitor_processing'),
    url(r'^activity_count/$', activity_count, name='activity_count'),
    url(r'^report_server_jobs/$', report_server_jobs, name='report_server_jobs'),
    url(r'^aprm_error_count/$', aprm_error_count, name='aprm_error_count'),
    url(r'^detail_error_report/$', detail_error_report, name='detail_error_report'),
    url(r'^load_dealers/$', load_dealers, name='load_dealers'),
    url(r'^load_deals/$', load_deals, name='load_deals'),
    url(r'^load_cib/$', load_cib, name='load_cib'),
    url(r'^load_rib/$', load_rib, name='load_rib'),
    url(r'^update_dealers/$', update_dealers, name='update_dealers'),
    url(r'^update_rech_event_dealers/$', update_rech_event_dealers, name='update_rech_event_dealers'),
    url(r'^purge_errors/$', purge_errors, name='purge_errors'),
    url(r'^purge_dm73_by_msisdn/$', purge_dm73_by_msisdn, name='purge_dm73_by_msisdn'),
    url(r'^recycle_errors/$', recycle_errors, name='recycle_errors'),
    url(r'^dms_detail_report/$', dms_detail_report, name='dms_detail_report'),
    url(r'^dm40_update/$', dm40_update, name='dm40_update'),
    url(r'^dm27_update/$', dm27_update, name='dm27_update'),
    url(r'^actv_detail_report/$', actv_detail_report, name='actv_detail_report'),
    url(r'^prus_detail_report/$', prus_detail_report, name='prus_detail_report'),
    url(r'^usage_report/$', usage_report, name='usage_report'),
    url(r'^agent_details/$', agent_details, name='agent_details'),
    url(r'^get_agent_id/$', get_agent_id, name='get_agent_id'),
    url(r'^delete_dealer/$', delete_dealer, name='delete_dealer'),
    url(r'^missing_offers_ids/$', missing_offers_ids, name='missing_offers_ids'),
    url(r'^msisdn_details/$', msisdn_details, name='msisdn_details'),
]
