--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8
-- Dumped by pg_dump version 12.8

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account_emailaddress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailaddress (
    id integer NOT NULL,
    email character varying(254) NOT NULL,
    verified boolean NOT NULL,
    "primary" boolean NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.account_emailaddress OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailaddress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailaddress_id_seq OWNER TO postgres;

--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailaddress_id_seq OWNED BY public.account_emailaddress.id;


--
-- Name: account_emailconfirmation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account_emailconfirmation (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    sent timestamp with time zone,
    key character varying(64) NOT NULL,
    email_address_id integer NOT NULL
);


ALTER TABLE public.account_emailconfirmation OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_emailconfirmation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_emailconfirmation_id_seq OWNER TO postgres;

--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_emailconfirmation_id_seq OWNED BY public.account_emailconfirmation.id;


--
-- Name: application_application; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application_application (
    id integer NOT NULL,
    person_type integer NOT NULL,
    process integer NOT NULL,
    is_payment boolean NOT NULL,
    file_name character varying(64),
    password integer,
    given_date date,
    given_time character varying(10),
    is_active boolean NOT NULL,
    is_block boolean NOT NULL,
    cron character varying(15) NOT NULL,
    created_date timestamp with time zone,
    updated_date timestamp with time zone,
    canceled_date timestamp with time zone,
    confirmed_date timestamp with time zone,
    car_id integer,
    created_user_id integer,
    inspector_id integer,
    organization_id integer,
    section_id integer,
    service_id integer
);


ALTER TABLE public.application_application OWNER TO postgres;

--
-- Name: application_application_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.application_application_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.application_application_id_seq OWNER TO postgres;

--
-- Name: application_application_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.application_application_id_seq OWNED BY public.application_application.id;


--
-- Name: application_applicationcashbymoderator; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application_applicationcashbymoderator (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    status integer NOT NULL,
    application_id integer,
    moderator_id integer,
    paid_state_duty_id integer,
    CONSTRAINT application_applicationcashbymoderator_status_check CHECK ((status >= 0))
);


ALTER TABLE public.application_applicationcashbymoderator OWNER TO postgres;

--
-- Name: application_applicationcashbymoderator_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.application_applicationcashbymoderator_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.application_applicationcashbymoderator_id_seq OWNER TO postgres;

--
-- Name: application_applicationcashbymoderator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.application_applicationcashbymoderator_id_seq OWNED BY public.application_applicationcashbymoderator.id;


--
-- Name: application_applicationdocument; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application_applicationdocument (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    seriya character varying(50),
    contract_date date,
    application_id integer NOT NULL,
    example_document_id integer
);


ALTER TABLE public.application_applicationdocument OWNER TO postgres;

--
-- Name: application_applicationdocument_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.application_applicationdocument_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.application_applicationdocument_id_seq OWNER TO postgres;

--
-- Name: application_applicationdocument_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.application_applicationdocument_id_seq OWNED BY public.application_applicationdocument.id;


--
-- Name: application_applicationdocumentattachment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.application_applicationdocumentattachment (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    attachment character varying(100) NOT NULL,
    application_document_id integer NOT NULL
);


ALTER TABLE public.application_applicationdocumentattachment OWNER TO postgres;

--
-- Name: application_applicationdocumentattachment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.application_applicationdocumentattachment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.application_applicationdocumentattachment_id_seq OWNER TO postgres;

--
-- Name: application_applicationdocumentattachment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.application_applicationdocumentattachment_id_seq OWNED BY public.application_applicationdocumentattachment.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO postgres;

--
-- Name: click_order; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.click_order (
    id integer NOT NULL,
    created_date timestamp with time zone,
    is_paid boolean NOT NULL,
    type character varying(10) NOT NULL,
    amount character varying(20) NOT NULL,
    service_id integer,
    user_id integer NOT NULL
);


ALTER TABLE public.click_order OWNER TO postgres;

--
-- Name: click_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.click_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.click_order_id_seq OWNER TO postgres;

--
-- Name: click_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.click_order_id_seq OWNED BY public.click_order.id;


--
-- Name: clickuz_transaction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clickuz_transaction (
    id integer NOT NULL,
    click_trans_id character varying(255) NOT NULL,
    merchant_trans_id character varying(255) NOT NULL,
    amount character varying(255) NOT NULL,
    action character varying(255) NOT NULL,
    sign_string character varying(255) NOT NULL,
    sign_datetime timestamp with time zone NOT NULL,
    status character varying(25) NOT NULL
);


ALTER TABLE public.clickuz_transaction OWNER TO postgres;

--
-- Name: clickuz_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.clickuz_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.clickuz_transaction_id_seq OWNER TO postgres;

--
-- Name: clickuz_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.clickuz_transaction_id_seq OWNED BY public.clickuz_transaction.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO postgres;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;


--
-- Name: paycom_paycomtransaction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paycom_paycomtransaction (
    id integer NOT NULL,
    _id character varying(255) NOT NULL,
    request_id integer NOT NULL,
    order_key character varying(255),
    amount numeric(10,2) NOT NULL,
    state integer,
    status character varying(55) NOT NULL,
    perform_datetime character varying(255),
    cancel_datetime character varying(255),
    created_datetime character varying(255),
    reason integer
);


ALTER TABLE public.paycom_paycomtransaction OWNER TO postgres;

--
-- Name: paycom_paycomtransaction_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paycom_paycomtransaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paycom_paycomtransaction_id_seq OWNER TO postgres;

--
-- Name: paycom_paycomtransaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paycom_paycomtransaction_id_seq OWNED BY public.paycom_paycomtransaction.id;


--
-- Name: service_amountbasecalculation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_amountbasecalculation (
    id integer NOT NULL,
    amount integer NOT NULL,
    start date,
    stop date,
    is_active boolean NOT NULL
);


ALTER TABLE public.service_amountbasecalculation OWNER TO postgres;

--
-- Name: service_amountbasecalculation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_amountbasecalculation_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_amountbasecalculation_id_seq OWNER TO postgres;

--
-- Name: service_amountbasecalculation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_amountbasecalculation_id_seq OWNED BY public.service_amountbasecalculation.id;


--
-- Name: service_exampledocument; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_exampledocument (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    title character varying(200) NOT NULL,
    key character varying(100) NOT NULL
);


ALTER TABLE public.service_exampledocument OWNER TO postgres;

--
-- Name: service_exampledocument_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_exampledocument_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_exampledocument_id_seq OWNER TO postgres;

--
-- Name: service_exampledocument_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_exampledocument_id_seq OWNED BY public.service_exampledocument.id;


--
-- Name: service_paidstateduty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_paidstateduty (
    id integer NOT NULL,
    is_return boolean NOT NULL,
    created_date date NOT NULL,
    application_id integer NOT NULL,
    percent_id integer NOT NULL,
    score_id integer NOT NULL
);


ALTER TABLE public.service_paidstateduty OWNER TO postgres;

--
-- Name: service_paidstateduty_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_paidstateduty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_paidstateduty_id_seq OWNER TO postgres;

--
-- Name: service_paidstateduty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_paidstateduty_id_seq OWNED BY public.service_paidstateduty.id;


--
-- Name: service_service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_service (
    id integer NOT NULL,
    short_title character varying(40) NOT NULL,
    long_title character varying(200) NOT NULL,
    key character varying(50) NOT NULL,
    is_active boolean NOT NULL,
    "desc" text NOT NULL,
    photo character varying(255) NOT NULL,
    deadline character varying(20) NOT NULL,
    instruction text NOT NULL,
    created_date timestamp with time zone,
    sort integer NOT NULL
);


ALTER TABLE public.service_service OWNER TO postgres;

--
-- Name: service_service_document; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_service_document (
    id integer NOT NULL,
    service_id integer NOT NULL,
    exampledocument_id integer NOT NULL
);


ALTER TABLE public.service_service_document OWNER TO postgres;

--
-- Name: service_service_document_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_service_document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_service_document_id_seq OWNER TO postgres;

--
-- Name: service_service_document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_service_document_id_seq OWNED BY public.service_service_document.id;


--
-- Name: service_service_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_service_id_seq OWNER TO postgres;

--
-- Name: service_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_service_id_seq OWNED BY public.service_service.id;


--
-- Name: service_stateduty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_stateduty (
    id integer NOT NULL,
    created_date date NOT NULL,
    application_id integer NOT NULL,
    percent_id integer NOT NULL,
    score_id integer NOT NULL,
    is_return boolean NOT NULL
);


ALTER TABLE public.service_stateduty OWNER TO postgres;

--
-- Name: service_stateduty_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_stateduty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_stateduty_id_seq OWNER TO postgres;

--
-- Name: service_stateduty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_stateduty_id_seq OWNED BY public.service_stateduty.id;


--
-- Name: service_statedutypercent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_statedutypercent (
    id integer NOT NULL,
    title character varying(255),
    state_duty integer,
    person_type integer,
    car_is_new boolean NOT NULL,
    is_old_number boolean NOT NULL,
    lost_number boolean NOT NULL,
    lost_technical_passport boolean NOT NULL,
    is_auction boolean NOT NULL,
    start integer NOT NULL,
    stop integer NOT NULL,
    percent double precision NOT NULL
);


ALTER TABLE public.service_statedutypercent OWNER TO postgres;

--
-- Name: service_statedutypercent_car_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_statedutypercent_car_type (
    id integer NOT NULL,
    statedutypercent_id integer NOT NULL,
    cartype_id integer NOT NULL
);


ALTER TABLE public.service_statedutypercent_car_type OWNER TO postgres;

--
-- Name: service_statedutypercent_car_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_statedutypercent_car_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_statedutypercent_car_type_id_seq OWNER TO postgres;

--
-- Name: service_statedutypercent_car_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_statedutypercent_car_type_id_seq OWNED BY public.service_statedutypercent_car_type.id;


--
-- Name: service_statedutypercent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_statedutypercent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_statedutypercent_id_seq OWNER TO postgres;

--
-- Name: service_statedutypercent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_statedutypercent_id_seq OWNED BY public.service_statedutypercent.id;


--
-- Name: service_statedutypercent_service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_statedutypercent_service (
    id integer NOT NULL,
    statedutypercent_id integer NOT NULL,
    service_id integer NOT NULL
);


ALTER TABLE public.service_statedutypercent_service OWNER TO postgres;

--
-- Name: service_statedutypercent_service_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_statedutypercent_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_statedutypercent_service_id_seq OWNER TO postgres;

--
-- Name: service_statedutypercent_service_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_statedutypercent_service_id_seq OWNED BY public.service_statedutypercent_service.id;


--
-- Name: service_statedutyscore; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service_statedutyscore (
    id integer NOT NULL,
    state_duty character varying(20) NOT NULL,
    score character varying(30) NOT NULL,
    created_date timestamp with time zone NOT NULL,
    updated_date timestamp with time zone NOT NULL,
    district_id integer,
    region_id integer
);


ALTER TABLE public.service_statedutyscore OWNER TO postgres;

--
-- Name: service_statedutyscore_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.service_statedutyscore_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.service_statedutyscore_id_seq OWNER TO postgres;

--
-- Name: service_statedutyscore_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.service_statedutyscore_id_seq OWNED BY public.service_statedutyscore.id;


--
-- Name: socialaccount_socialaccount; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialaccount (
    id integer NOT NULL,
    provider character varying(30) NOT NULL,
    uid character varying(191) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    extra_data text NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialaccount OWNER TO postgres;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialaccount_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialaccount_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialaccount_id_seq OWNED BY public.socialaccount_socialaccount.id;


--
-- Name: socialaccount_socialapp; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialapp (
    id integer NOT NULL,
    provider character varying(30) NOT NULL,
    name character varying(40) NOT NULL,
    client_id character varying(191) NOT NULL,
    secret character varying(191) NOT NULL,
    key character varying(191) NOT NULL
);


ALTER TABLE public.socialaccount_socialapp OWNER TO postgres;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialapp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialapp_id_seq OWNED BY public.socialaccount_socialapp.id;


--
-- Name: socialaccount_socialapp_sites; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialapp_sites (
    id integer NOT NULL,
    socialapp_id integer NOT NULL,
    site_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialapp_sites OWNER TO postgres;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialapp_sites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialapp_sites_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialapp_sites_id_seq OWNED BY public.socialaccount_socialapp_sites.id;


--
-- Name: socialaccount_socialtoken; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.socialaccount_socialtoken (
    id integer NOT NULL,
    token text NOT NULL,
    token_secret text NOT NULL,
    expires_at timestamp with time zone,
    account_id integer NOT NULL,
    app_id integer NOT NULL
);


ALTER TABLE public.socialaccount_socialtoken OWNER TO postgres;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.socialaccount_socialtoken_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialaccount_socialtoken_id_seq OWNER TO postgres;

--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.socialaccount_socialtoken_id_seq OWNED BY public.socialaccount_socialtoken.id;


--
-- Name: user_bodytype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_bodytype (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    is_active boolean NOT NULL,
    created_date timestamp with time zone NOT NULL
);


ALTER TABLE public.user_bodytype OWNER TO postgres;

--
-- Name: user_bodytype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_bodytype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_bodytype_id_seq OWNER TO postgres;

--
-- Name: user_bodytype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_bodytype_id_seq OWNED BY public.user_bodytype.id;


--
-- Name: user_car; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_car (
    id integer NOT NULL,
    full_weight character varying(10),
    empty_weight character varying(10),
    body_number character varying(50) NOT NULL,
    chassis_number character varying(255),
    engine_number character varying(50) NOT NULL,
    made_year date,
    engine_power integer,
    old_number character varying(15),
    old_technical_passport character varying(30) NOT NULL,
    is_old_number boolean NOT NULL,
    given_technical_passport character varying(30) NOT NULL,
    created_date timestamp with time zone NOT NULL,
    lost_technical_passport boolean NOT NULL,
    lost_number boolean NOT NULL,
    is_confirm boolean NOT NULL,
    confirm_date timestamp with time zone,
    is_technical_confirm boolean NOT NULL,
    technical_confirm_date timestamp with time zone,
    is_new boolean NOT NULL,
    price bigint NOT NULL,
    is_auction boolean NOT NULL,
    given_number character varying(15),
    is_replace_number boolean NOT NULL,
    body_type_id integer,
    color_id integer,
    history_id integer,
    model_id integer,
    re_color_id integer,
    type_id integer
);


ALTER TABLE public.user_car OWNER TO postgres;

--
-- Name: user_car_device; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_car_device (
    id integer NOT NULL,
    car_id integer NOT NULL,
    device_id integer NOT NULL
);


ALTER TABLE public.user_car_device OWNER TO postgres;

--
-- Name: user_car_device_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_car_device_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_car_device_id_seq OWNER TO postgres;

--
-- Name: user_car_device_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_car_device_id_seq OWNED BY public.user_car_device.id;


--
-- Name: user_car_fuel_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_car_fuel_type (
    id integer NOT NULL,
    car_id integer NOT NULL,
    fueltype_id integer NOT NULL
);


ALTER TABLE public.user_car_fuel_type OWNER TO postgres;

--
-- Name: user_car_fuel_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_car_fuel_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_car_fuel_type_id_seq OWNER TO postgres;

--
-- Name: user_car_fuel_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_car_fuel_type_id_seq OWNED BY public.user_car_fuel_type.id;


--
-- Name: user_car_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_car_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_car_id_seq OWNER TO postgres;

--
-- Name: user_car_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_car_id_seq OWNED BY public.user_car.id;


--
-- Name: user_car_re_fuel_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_car_re_fuel_type (
    id integer NOT NULL,
    car_id integer NOT NULL,
    fueltype_id integer NOT NULL
);


ALTER TABLE public.user_car_re_fuel_type OWNER TO postgres;

--
-- Name: user_car_re_fuel_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_car_re_fuel_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_car_re_fuel_type_id_seq OWNER TO postgres;

--
-- Name: user_car_re_fuel_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_car_re_fuel_type_id_seq OWNED BY public.user_car_re_fuel_type.id;


--
-- Name: user_carmodel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_carmodel (
    id integer NOT NULL,
    title character varying(50) NOT NULL,
    creator character varying(100),
    is_local boolean NOT NULL,
    is_truck boolean NOT NULL,
    is_active boolean NOT NULL,
    created_date timestamp with time zone NOT NULL,
    created_user_id integer
);


ALTER TABLE public.user_carmodel OWNER TO postgres;

--
-- Name: user_carmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_carmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_carmodel_id_seq OWNER TO postgres;

--
-- Name: user_carmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_carmodel_id_seq OWNED BY public.user_carmodel.id;


--
-- Name: user_cartype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_cartype (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    is_active boolean NOT NULL,
    created_date timestamp with time zone NOT NULL
);


ALTER TABLE public.user_cartype OWNER TO postgres;

--
-- Name: user_cartype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_cartype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_cartype_id_seq OWNER TO postgres;

--
-- Name: user_cartype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_cartype_id_seq OWNED BY public.user_cartype.id;


--
-- Name: user_color; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_color (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    is_active boolean NOT NULL,
    created_date timestamp with time zone NOT NULL,
    created_user_id integer
);


ALTER TABLE public.user_color OWNER TO postgres;

--
-- Name: user_color_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_color_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_color_id_seq OWNER TO postgres;

--
-- Name: user_color_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_color_id_seq OWNED BY public.user_color.id;


--
-- Name: user_constant; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_constant (
    id integer NOT NULL,
    key character varying(150) NOT NULL,
    value character varying(150) NOT NULL,
    info character varying(250) NOT NULL
);


ALTER TABLE public.user_constant OWNER TO postgres;

--
-- Name: user_constant_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_constant_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_constant_id_seq OWNER TO postgres;

--
-- Name: user_constant_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_constant_id_seq OWNED BY public.user_constant.id;


--
-- Name: user_device; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_device (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    is_active boolean NOT NULL,
    created_date timestamp with time zone NOT NULL
);


ALTER TABLE public.user_device OWNER TO postgres;

--
-- Name: user_device_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_device_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_device_id_seq OWNER TO postgres;

--
-- Name: user_device_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_device_id_seq OWNED BY public.user_device.id;


--
-- Name: user_district; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_district (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    sort integer NOT NULL,
    is_active boolean NOT NULL,
    region_id integer
);


ALTER TABLE public.user_district OWNER TO postgres;

--
-- Name: user_district_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_district_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_district_id_seq OWNER TO postgres;

--
-- Name: user_district_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_district_id_seq OWNED BY public.user_district.id;


--
-- Name: user_fueltype; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_fueltype (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    is_active boolean NOT NULL,
    created_date timestamp with time zone NOT NULL
);


ALTER TABLE public.user_fueltype OWNER TO postgres;

--
-- Name: user_fueltype_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_fueltype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_fueltype_id_seq OWNER TO postgres;

--
-- Name: user_fueltype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_fueltype_id_seq OWNED BY public.user_fueltype.id;


--
-- Name: user_notification; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_notification (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    text text NOT NULL,
    is_read boolean NOT NULL,
    application_id integer NOT NULL,
    receiver_id integer NOT NULL,
    sender_id integer NOT NULL
);


ALTER TABLE public.user_notification OWNER TO postgres;

--
-- Name: user_notification_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_notification_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_notification_id_seq OWNER TO postgres;

--
-- Name: user_notification_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_notification_id_seq OWNED BY public.user_notification.id;


--
-- Name: user_organization; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_organization (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    identification_number integer,
    address_of_garage character varying(255) NOT NULL,
    director character varying(50),
    created_date timestamp with time zone,
    updated_date timestamp with time zone,
    removed_date timestamp with time zone,
    is_active boolean NOT NULL,
    created_user_id integer,
    legal_address_district_id integer,
    legal_address_region_id integer
);


ALTER TABLE public.user_organization OWNER TO postgres;

--
-- Name: user_organization_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_organization_id_seq OWNER TO postgres;

--
-- Name: user_organization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_organization_id_seq OWNED BY public.user_organization.id;


--
-- Name: user_quarter; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_quarter (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    sort integer NOT NULL,
    is_active boolean NOT NULL,
    district_id integer
);


ALTER TABLE public.user_quarter OWNER TO postgres;

--
-- Name: user_quarter_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_quarter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_quarter_id_seq OWNER TO postgres;

--
-- Name: user_quarter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_quarter_id_seq OWNED BY public.user_quarter.id;


--
-- Name: user_region; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_region (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    sort integer NOT NULL,
    is_active boolean NOT NULL
);


ALTER TABLE public.user_region OWNER TO postgres;

--
-- Name: user_region_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_region_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_region_id_seq OWNER TO postgres;

--
-- Name: user_region_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_region_id_seq OWNED BY public.user_region.id;


--
-- Name: user_section; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_section (
    id integer NOT NULL,
    title character varying(300),
    is_active boolean NOT NULL,
    pay_for_service boolean NOT NULL,
    address character varying(100) NOT NULL,
    parent_id integer,
    region_id integer
);


ALTER TABLE public.user_section OWNER TO postgres;

--
-- Name: user_section_district; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_section_district (
    id integer NOT NULL,
    section_id integer NOT NULL,
    district_id integer NOT NULL
);


ALTER TABLE public.user_section_district OWNER TO postgres;

--
-- Name: user_section_district_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_section_district_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_section_district_id_seq OWNER TO postgres;

--
-- Name: user_section_district_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_section_district_id_seq OWNED BY public.user_section_district.id;


--
-- Name: user_section_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_section_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_section_id_seq OWNER TO postgres;

--
-- Name: user_section_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_section_id_seq OWNED BY public.user_section.id;


--
-- Name: user_sms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_sms (
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    sms_count integer,
    text text NOT NULL,
    sms_id bigint NOT NULL,
    status integer NOT NULL,
    phone integer NOT NULL
);


ALTER TABLE public.user_sms OWNER TO postgres;

--
-- Name: user_sms_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_sms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_sms_id_seq OWNER TO postgres;

--
-- Name: user_sms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_sms_id_seq OWNED BY public.user_sms.id;


--
-- Name: user_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_name character varying(255) NOT NULL,
    first_name character varying(255) NOT NULL,
    middle_name character varying(255) NOT NULL,
    role integer NOT NULL,
    address character varying(255),
    email character varying(254) NOT NULL,
    birthday date,
    username character varying(30) NOT NULL,
    phone integer,
    passport_seriya character varying(10),
    passport_number bigint,
    person_id bigint,
    issue_by_whom character varying(30),
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    is_active boolean NOT NULL,
    last_login timestamp with time zone,
    date_joined timestamp with time zone NOT NULL,
    gender integer NOT NULL,
    turbo character varying(200),
    secret_key uuid NOT NULL,
    district_id integer,
    quarter_id integer,
    region_id integer,
    section_id integer
);


ALTER TABLE public.user_user OWNER TO postgres;

--
-- Name: user_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.user_user_groups OWNER TO postgres;

--
-- Name: user_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_groups_id_seq OWNER TO postgres;

--
-- Name: user_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_groups_id_seq OWNED BY public.user_user_groups.id;


--
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_id_seq OWNER TO postgres;

--
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_id_seq OWNED BY public.user_user.id;


--
-- Name: user_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.user_user_user_permissions OWNER TO postgres;

--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_user_user_permissions_id_seq OWNED BY public.user_user_user_permissions.id;


--
-- Name: account_emailaddress id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress ALTER COLUMN id SET DEFAULT nextval('public.account_emailaddress_id_seq'::regclass);


--
-- Name: account_emailconfirmation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation ALTER COLUMN id SET DEFAULT nextval('public.account_emailconfirmation_id_seq'::regclass);


--
-- Name: application_application id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application ALTER COLUMN id SET DEFAULT nextval('public.application_application_id_seq'::regclass);


--
-- Name: application_applicationcashbymoderator id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationcashbymoderator ALTER COLUMN id SET DEFAULT nextval('public.application_applicationcashbymoderator_id_seq'::regclass);


--
-- Name: application_applicationdocument id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocument ALTER COLUMN id SET DEFAULT nextval('public.application_applicationdocument_id_seq'::regclass);


--
-- Name: application_applicationdocumentattachment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocumentattachment ALTER COLUMN id SET DEFAULT nextval('public.application_applicationdocumentattachment_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: click_order id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.click_order ALTER COLUMN id SET DEFAULT nextval('public.click_order_id_seq'::regclass);


--
-- Name: clickuz_transaction id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clickuz_transaction ALTER COLUMN id SET DEFAULT nextval('public.clickuz_transaction_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: django_site id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);


--
-- Name: paycom_paycomtransaction id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paycom_paycomtransaction ALTER COLUMN id SET DEFAULT nextval('public.paycom_paycomtransaction_id_seq'::regclass);


--
-- Name: service_amountbasecalculation id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_amountbasecalculation ALTER COLUMN id SET DEFAULT nextval('public.service_amountbasecalculation_id_seq'::regclass);


--
-- Name: service_exampledocument id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_exampledocument ALTER COLUMN id SET DEFAULT nextval('public.service_exampledocument_id_seq'::regclass);


--
-- Name: service_paidstateduty id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_paidstateduty ALTER COLUMN id SET DEFAULT nextval('public.service_paidstateduty_id_seq'::regclass);


--
-- Name: service_service id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service ALTER COLUMN id SET DEFAULT nextval('public.service_service_id_seq'::regclass);


--
-- Name: service_service_document id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service_document ALTER COLUMN id SET DEFAULT nextval('public.service_service_document_id_seq'::regclass);


--
-- Name: service_stateduty id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_stateduty ALTER COLUMN id SET DEFAULT nextval('public.service_stateduty_id_seq'::regclass);


--
-- Name: service_statedutypercent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent ALTER COLUMN id SET DEFAULT nextval('public.service_statedutypercent_id_seq'::regclass);


--
-- Name: service_statedutypercent_car_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_car_type ALTER COLUMN id SET DEFAULT nextval('public.service_statedutypercent_car_type_id_seq'::regclass);


--
-- Name: service_statedutypercent_service id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_service ALTER COLUMN id SET DEFAULT nextval('public.service_statedutypercent_service_id_seq'::regclass);


--
-- Name: service_statedutyscore id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutyscore ALTER COLUMN id SET DEFAULT nextval('public.service_statedutyscore_id_seq'::regclass);


--
-- Name: socialaccount_socialaccount id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialaccount_id_seq'::regclass);


--
-- Name: socialaccount_socialapp id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_id_seq'::regclass);


--
-- Name: socialaccount_socialapp_sites id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialapp_sites_id_seq'::regclass);


--
-- Name: socialaccount_socialtoken id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken ALTER COLUMN id SET DEFAULT nextval('public.socialaccount_socialtoken_id_seq'::regclass);


--
-- Name: user_bodytype id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_bodytype ALTER COLUMN id SET DEFAULT nextval('public.user_bodytype_id_seq'::regclass);


--
-- Name: user_car id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car ALTER COLUMN id SET DEFAULT nextval('public.user_car_id_seq'::regclass);


--
-- Name: user_car_device id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_device ALTER COLUMN id SET DEFAULT nextval('public.user_car_device_id_seq'::regclass);


--
-- Name: user_car_fuel_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_fuel_type ALTER COLUMN id SET DEFAULT nextval('public.user_car_fuel_type_id_seq'::regclass);


--
-- Name: user_car_re_fuel_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_re_fuel_type ALTER COLUMN id SET DEFAULT nextval('public.user_car_re_fuel_type_id_seq'::regclass);


--
-- Name: user_carmodel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_carmodel ALTER COLUMN id SET DEFAULT nextval('public.user_carmodel_id_seq'::regclass);


--
-- Name: user_cartype id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_cartype ALTER COLUMN id SET DEFAULT nextval('public.user_cartype_id_seq'::regclass);


--
-- Name: user_color id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_color ALTER COLUMN id SET DEFAULT nextval('public.user_color_id_seq'::regclass);


--
-- Name: user_constant id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_constant ALTER COLUMN id SET DEFAULT nextval('public.user_constant_id_seq'::regclass);


--
-- Name: user_device id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_device ALTER COLUMN id SET DEFAULT nextval('public.user_device_id_seq'::regclass);


--
-- Name: user_district id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_district ALTER COLUMN id SET DEFAULT nextval('public.user_district_id_seq'::regclass);


--
-- Name: user_fueltype id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_fueltype ALTER COLUMN id SET DEFAULT nextval('public.user_fueltype_id_seq'::regclass);


--
-- Name: user_notification id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification ALTER COLUMN id SET DEFAULT nextval('public.user_notification_id_seq'::regclass);


--
-- Name: user_organization id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_organization ALTER COLUMN id SET DEFAULT nextval('public.user_organization_id_seq'::regclass);


--
-- Name: user_quarter id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_quarter ALTER COLUMN id SET DEFAULT nextval('public.user_quarter_id_seq'::regclass);


--
-- Name: user_region id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_region ALTER COLUMN id SET DEFAULT nextval('public.user_region_id_seq'::regclass);


--
-- Name: user_section id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section ALTER COLUMN id SET DEFAULT nextval('public.user_section_id_seq'::regclass);


--
-- Name: user_section_district id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section_district ALTER COLUMN id SET DEFAULT nextval('public.user_section_district_id_seq'::regclass);


--
-- Name: user_sms id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_sms ALTER COLUMN id SET DEFAULT nextval('public.user_sms_id_seq'::regclass);


--
-- Name: user_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user ALTER COLUMN id SET DEFAULT nextval('public.user_user_id_seq'::regclass);


--
-- Name: user_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups ALTER COLUMN id SET DEFAULT nextval('public.user_user_groups_id_seq'::regclass);


--
-- Name: user_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.user_user_user_permissions_id_seq'::regclass);


--
-- Data for Name: account_emailaddress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailaddress (id, email, verified, "primary", user_id) FROM stdin;
\.


--
-- Data for Name: account_emailconfirmation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account_emailconfirmation (id, created, sent, key, email_address_id) FROM stdin;
\.


--
-- Data for Name: application_application; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.application_application (id, person_type, process, is_payment, file_name, password, given_date, given_time, is_active, is_block, cron, created_date, updated_date, canceled_date, confirmed_date, car_id, created_user_id, inspector_id, organization_id, section_id, service_id) FROM stdin;
19	0	0	f	f3ba33913d90f81	4597	\N	\N	t	t	1	2021-10-17 09:57:59.680901+05	2021-10-17 09:58:04.907202+05	\N	\N	34	9	\N	\N	2	2
20	0	0	f	37641bcef390441	4737	\N	\N	t	t	1	2021-10-17 10:22:51.610562+05	2021-10-17 10:22:55.077377+05	\N	\N	35	9	\N	\N	2	2
15	0	0	f	d45f271e290c03d	3857	\N	\N	f	t	1	2021-10-17 09:43:17.279914+05	2021-10-17 09:43:17.28955+05	\N	\N	30	9	\N	\N	\N	2
16	0	0	f	90170d5b4dcf67e	3279	\N	\N	t	t	1	2021-10-17 09:45:25.260944+05	2021-10-17 09:45:32.805117+05	\N	\N	31	9	\N	\N	2	5
17	0	0	t	6fd73969443aedb	7283	\N	\N	t	t	1	2021-10-17 09:51:30.534665+05	2021-10-17 12:15:40.76313+05	\N	\N	32	9	\N	\N	2	1
18	0	0	t	b09287cf9a566b1	1630	\N	\N	t	t	1	2021-10-17 09:53:16.545032+05	2021-10-17 13:12:30.073336+05	\N	\N	33	9	\N	\N	2	1
21	0	0	f	0b7b72b0486ed74	4464	\N	\N	t	t	1	2021-10-17 14:41:53.38259+05	2021-10-17 14:41:59.180145+05	\N	\N	36	9	\N	\N	3	1
\.


--
-- Data for Name: application_applicationcashbymoderator; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.application_applicationcashbymoderator (id, created_at, updated_at, is_active, status, application_id, moderator_id, paid_state_duty_id) FROM stdin;
8	2021-10-17 16:25:47.6465+05	2021-10-17 16:25:47.6465+05	t	1	17	3	7
9	2021-10-17 16:33:03.360446+05	2021-10-17 16:33:03.360446+05	t	1	17	3	8
\.


--
-- Data for Name: application_applicationdocument; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.application_applicationdocument (id, created_at, updated_at, is_active, seriya, contract_date, application_id, example_document_id) FROM stdin;
10	2021-10-17 09:43:17.287772+05	2021-10-17 09:43:17.287797+05	t	AAC9565975	2021-10-04	15	3
11	2021-10-17 09:51:30.543518+05	2021-10-17 09:51:30.543542+05	t	AAC9565061	2021-10-04	17	2
12	2021-10-17 09:53:16.550054+05	2021-10-17 09:53:16.55008+05	t	AAX9459988	2021-10-04	18	2
13	2021-10-17 09:57:59.687538+05	2021-10-17 09:57:59.687565+05	t	AAC9564952	2021-10-04	19	3
14	2021-10-17 10:22:51.617469+05	2021-10-17 10:22:51.617497+05	t	AAC569595	2021-10-04	20	3
15	2021-10-17 14:41:53.39459+05	2021-10-17 14:41:53.39459+05	t	ACC455645	2021-10-15	21	2
\.


--
-- Data for Name: application_applicationdocumentattachment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.application_applicationdocumentattachment (id, created_at, updated_at, is_active, attachment, application_document_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add user	6	add_user
22	Can change user	6	change_user
23	Can delete user	6	delete_user
24	Can view user	6	view_user
25	Can add Kuzov turi	7	add_bodytype
26	Can change Kuzov turi	7	change_bodytype
27	Can delete Kuzov turi	7	delete_bodytype
28	Can view Kuzov turi	7	view_bodytype
29	Can add Transport vositasi turi	8	add_cartype
30	Can change Transport vositasi turi	8	change_cartype
31	Can delete Transport vositasi turi	8	delete_cartype
32	Can view Transport vositasi turi	8	view_cartype
33	Can add Constant	9	add_constant
34	Can change Constant	9	change_constant
35	Can delete Constant	9	delete_constant
36	Can view Constant	9	view_constant
37	Can add Qo'shimcha qurilma	10	add_device
38	Can change Qo'shimcha qurilma	10	change_device
39	Can delete Qo'shimcha qurilma	10	delete_device
40	Can view Qo'shimcha qurilma	10	view_device
41	Can add Tuman/Shahar	11	add_district
42	Can change Tuman/Shahar	11	change_district
43	Can delete Tuman/Shahar	11	delete_district
44	Can view Tuman/Shahar	11	view_district
45	Can add Yoqilg'i turi	12	add_fueltype
46	Can change Yoqilg'i turi	12	change_fueltype
47	Can delete Yoqilg'i turi	12	delete_fueltype
48	Can view Yoqilg'i turi	12	view_fueltype
49	Can add Viloyat	13	add_region
50	Can change Viloyat	13	change_region
51	Can delete Viloyat	13	delete_region
52	Can view Viloyat	13	view_region
53	Can add Jo'natilgan sms	14	add_sms
54	Can change Jo'natilgan sms	14	change_sms
55	Can delete Jo'natilgan sms	14	delete_sms
56	Can view Jo'natilgan sms	14	view_sms
57	Can add Bo'lim	15	add_section
58	Can change Bo'lim	15	change_section
59	Can delete Bo'lim	15	delete_section
60	Can view Bo'lim	15	view_section
61	Can add Mahalla	16	add_quarter
62	Can change Mahalla	16	change_quarter
63	Can delete Mahalla	16	delete_quarter
64	Can view Mahalla	16	view_quarter
65	Can add Tashkilot	17	add_organization
66	Can change Tashkilot	17	change_organization
67	Can delete Tashkilot	17	delete_organization
68	Can view Tashkilot	17	view_organization
69	Can add notification	18	add_notification
70	Can change notification	18	change_notification
71	Can delete notification	18	delete_notification
72	Can view notification	18	view_notification
73	Can add Rang	19	add_color
74	Can change Rang	19	change_color
75	Can delete Rang	19	delete_color
76	Can view Rang	19	view_color
77	Can add Avtomobil rusumi	20	add_carmodel
78	Can change Avtomobil rusumi	20	change_carmodel
79	Can delete Avtomobil rusumi	20	delete_carmodel
80	Can view Avtomobil rusumi	20	view_carmodel
81	Can add Avtomobil	21	add_car
82	Can change Avtomobil	21	change_car
83	Can delete Avtomobil	21	delete_car
84	Can view Avtomobil	21	view_car
85	Can add site	22	add_site
86	Can change site	22	change_site
87	Can delete site	22	delete_site
88	Can view site	22	view_site
89	Can add Bazaviy hisoblash miqdori	23	add_amountbasecalculation
90	Can change Bazaviy hisoblash miqdori	23	change_amountbasecalculation
91	Can delete Bazaviy hisoblash miqdori	23	delete_amountbasecalculation
92	Can view Bazaviy hisoblash miqdori	23	view_amountbasecalculation
93	Can add Hujjat	24	add_exampledocument
94	Can change Hujjat	24	change_exampledocument
95	Can delete Hujjat	24	delete_exampledocument
96	Can view Hujjat	24	view_exampledocument
97	Can add Servis	25	add_service
98	Can change Servis	25	change_service
99	Can delete Servis	25	delete_service
100	Can view Servis	25	view_service
101	Can add To'lanishi kerak bo'lgan bojlar	26	add_stateduty
102	Can change To'lanishi kerak bo'lgan bojlar	26	change_stateduty
103	Can delete To'lanishi kerak bo'lgan bojlar	26	delete_stateduty
104	Can view To'lanishi kerak bo'lgan bojlar	26	view_stateduty
105	Can add Davlat boji foizlari	27	add_statedutypercent
106	Can change Davlat boji foizlari	27	change_statedutypercent
107	Can delete Davlat boji foizlari	27	delete_statedutypercent
108	Can view Davlat boji foizlari	27	view_statedutypercent
109	Can add Davlat boji hisob raqami	28	add_statedutyscore
110	Can change Davlat boji hisob raqami	28	change_statedutyscore
111	Can delete Davlat boji hisob raqami	28	delete_statedutyscore
112	Can view Davlat boji hisob raqami	28	view_statedutyscore
113	Can add email address	29	add_emailaddress
114	Can change email address	29	change_emailaddress
115	Can delete email address	29	delete_emailaddress
116	Can view email address	29	view_emailaddress
117	Can add email confirmation	30	add_emailconfirmation
118	Can change email confirmation	30	change_emailconfirmation
119	Can delete email confirmation	30	delete_emailconfirmation
120	Can view email confirmation	30	view_emailconfirmation
121	Can add social account	31	add_socialaccount
122	Can change social account	31	change_socialaccount
123	Can delete social account	31	delete_socialaccount
124	Can view social account	31	view_socialaccount
125	Can add social application	32	add_socialapp
126	Can change social application	32	change_socialapp
127	Can delete social application	32	delete_socialapp
128	Can view social application	32	view_socialapp
129	Can add social application token	33	add_socialtoken
130	Can change social application token	33	change_socialtoken
131	Can delete social application token	33	delete_socialtoken
132	Can view social application token	33	view_socialtoken
133	Can add Ariza	34	add_application
134	Can change Ariza	34	change_application
135	Can delete Ariza	34	delete_application
136	Can view Ariza	34	view_application
137	Can add application cash by moderator	35	add_applicationcashbymoderator
138	Can change application cash by moderator	35	change_applicationcashbymoderator
139	Can delete application cash by moderator	35	delete_applicationcashbymoderator
140	Can view application cash by moderator	35	view_applicationcashbymoderator
141	Can add application document	36	add_applicationdocument
142	Can change application document	36	change_applicationdocument
143	Can delete application document	36	delete_applicationdocument
144	Can view application document	36	view_applicationdocument
145	Can add application document attachment	37	add_applicationdocumentattachment
146	Can change application document attachment	37	change_applicationdocumentattachment
147	Can delete application document attachment	37	delete_applicationdocumentattachment
148	Can view application document attachment	37	view_applicationdocumentattachment
149	Can add Token	38	add_token
150	Can change Token	38	change_token
151	Can delete Token	38	delete_token
152	Can view Token	38	view_token
153	Can add token	39	add_tokenproxy
154	Can change token	39	change_tokenproxy
155	Can delete token	39	delete_tokenproxy
156	Can view token	39	view_tokenproxy
157	Can add Paycom Transaction	40	add_paycomtransaction
158	Can change Paycom Transaction	40	change_paycomtransaction
159	Can delete Paycom Transaction	40	delete_paycomtransaction
160	Can view Paycom Transaction	40	view_paycomtransaction
161	Can add order	41	add_order
162	Can change order	41	change_order
163	Can delete order	41	delete_order
164	Can view order	41	view_order
165	Can add transaction	42	add_transaction
166	Can change transaction	42	change_transaction
167	Can delete transaction	42	delete_transaction
168	Can view transaction	42	view_transaction
169	Can add Hujjat	43	add_document
170	Can change Hujjat	43	change_document
171	Can delete Hujjat	43	delete_document
172	Can view Hujjat	43	view_document
173	Can add To'lanishi kerak bo'lgan bojlar	44	add_paidstateduty
174	Can change To'lanishi kerak bo'lgan bojlar	44	change_paidstateduty
175	Can delete To'lanishi kerak bo'lgan bojlar	44	delete_paidstateduty
176	Can view To'lanishi kerak bo'lgan bojlar	44	view_paidstateduty
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
d5d4e0a3921db77fa4f338284bf6711019f6b9a8	2021-10-15 19:55:51.251277+05	7
932fbaece098db8d80c6dc950f03a5713817eb8b	2021-10-16 09:21:21.01487+05	5
76c1b16e14412fa8fa57c35f3bbe647b50ceb876	2021-10-16 11:52:30.423544+05	3
a98538464432ee9256837e6f11c194cccd49a6e1	2021-10-16 14:43:13.490744+05	9
\.


--
-- Data for Name: click_order; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.click_order (id, created_date, is_paid, type, amount, service_id, user_id) FROM stdin;
\.


--
-- Data for Name: clickuz_transaction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.clickuz_transaction (id, click_trans_id, merchant_trans_id, amount, action, sign_string, sign_datetime, status) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2021-10-15 19:57:44.524749+05	1	270000	1	[{"added": {}}]	23	1
2	2021-10-15 20:53:40.424645+05	5	TP almashtirish	2	[{"changed": {"fields": ["Short title", "Long title"]}}]	25	1
3	2021-10-15 20:54:49.425532+05	6	DRB almashtirish	1	[{"added": {}}]	25	1
4	2021-10-15 20:55:25.918018+05	5	TP almashtirish	2	[{"changed": {"fields": ["Sort"]}}]	25	1
5	2021-10-15 20:55:44.820096+05	6	DRB almashtirish	2	[{"changed": {"fields": ["Sort"]}}]	25	1
6	2021-10-15 20:55:58.888345+05	6	DRB almashtirish	2	[]	25	1
7	2021-10-15 20:56:43.525534+05	6	DRB almashtirish	2	[{"changed": {"fields": ["Long title"]}}]	25	1
8	2021-10-15 21:04:08.552105+05	4	Qayta jihozlash	2	[{"changed": {"fields": ["Is active"]}}]	25	1
9	2021-10-16 11:51:32.300335+05	3	Yoqubov Salohiddin	2	[{"changed": {"fields": ["Tel raqam"]}}]	6	1
10	2021-10-16 11:51:44.452205+05	2	Najbiyev Azizbek	2	[{"changed": {"fields": ["Tel raqam"]}}]	6	1
11	2021-10-16 11:52:54.588253+05	3	Yoqubov Salohiddin	2	[{"changed": {"fields": ["Bo'lim"]}}]	6	1
12	2021-10-16 14:40:28.134463+05	1	Buxoro viloyat IIB YHXB: Buxoro viloyati	2	[{"changed": {"fields": ["Bo'lim nomi"]}}]	15	1
13	2021-10-16 14:40:32.508998+05	1	Buxoro viloyat IIB YHXB: Buxoro viloyati	2	[{"changed": {"fields": ["Pay for service"]}}]	15	1
14	2021-10-16 14:40:51.43368+05	2	1-son RO' va IOB: Buxoro viloyati	2	[{"changed": {"fields": ["Bo'lim nomi"]}}]	15	1
15	2021-10-16 14:41:31.999573+05	3	3-son RO' va IOB: Buxoro viloyati	1	[{"added": {}}]	15	1
16	2021-10-16 14:42:00.660553+05	4	2-son RO' va IOB: Buxoro viloyati	1	[{"added": {}}]	15	1
17	2021-10-16 14:42:44.617109+05	2	Najbiyev Azizbek	3		6	1
18	2021-10-16 18:18:33.978957+05	17	Ro'yhatlash(17) : 300.0%	3		27	1
19	2021-10-16 18:18:33.983016+05	16	Ro'yhatlash(16) : 450.0%	3		27	1
20	2021-10-16 18:18:33.984989+05	15	Ro'yhatlash(15) : 150.0%	3		27	1
21	2021-10-16 18:18:33.986743+05	14	Ro'yhatlash(14) : 160.0%	3		27	1
22	2021-10-16 19:14:35.47231+05	14	Application: replace_number_and_tp	3		34	1
23	2021-10-16 19:14:35.475717+05	13	Application: contract_of_sale	3		34	1
24	2021-10-16 19:14:35.477437+05	12	Application: contract_of_sale	3		34	1
25	2021-10-16 19:14:35.479355+05	11	Application: replace_tp	3		34	1
26	2021-10-16 19:14:35.481189+05	10	Application: contract_of_sale	3		34	1
27	2021-10-16 19:14:35.483128+05	9	Application: account_statement	3		34	1
28	2021-10-16 19:14:35.484971+05	8	Application: replace_number_and_tp	3		34	1
29	2021-10-16 19:14:35.486548+05	7	Application: replace_number_and_tp	3		34	1
30	2021-10-16 19:14:35.488085+05	6	Application: replace_number_and_tp	3		34	1
31	2021-10-16 19:14:35.489609+05	5	Application: contract_of_sale	3		34	1
32	2021-10-16 19:14:35.491211+05	4	Application: contract_of_sale	3		34	1
33	2021-10-16 19:14:35.492765+05	3	Application: contract_of_sale	3		34	1
34	2021-10-16 19:14:35.494342+05	2	Application: contract_of_sale	3		34	1
35	2021-10-16 19:14:35.496061+05	1	Application: account_statement	3		34	1
36	2021-10-16 19:14:51.247605+05	4	ApplicationCashByModerator object (4)	3		35	1
37	2021-10-16 19:14:51.250954+05	3	ApplicationCashByModerator object (3)	3		35	1
38	2021-10-16 19:14:51.252903+05	2	ApplicationCashByModerator object (2)	3		35	1
39	2021-10-16 19:14:51.254889+05	1	ApplicationCashByModerator object (1)	3		35	1
40	2021-10-16 19:15:13.35218+05	20	Lacetti SX CNG L3-15G (1 позиция с ГБО)	3		21	1
41	2021-10-16 19:15:13.355139+05	19	Chevrolet Tracker Turbo 1.0 LT A/T (2-я позиция)	3		21	1
42	2021-10-16 19:15:13.357117+05	18	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
43	2021-10-16 19:15:13.359154+05	17	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
44	2021-10-16 19:15:13.36083+05	16	Chevrolet Tracker Redline A/T (3-я позиция)	3		21	1
45	2021-10-16 19:15:13.362431+05	15	Chevrolet Tracker Redline A/T (3-я позиция)	3		21	1
46	2021-10-16 19:15:13.36396+05	14	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
47	2021-10-16 19:15:13.365401+05	13	Chevrolet Tracker Redline A/T (3-я позиция)	3		21	1
48	2021-10-16 19:15:13.366845+05	12	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
49	2021-10-16 19:15:13.368432+05	11	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
50	2021-10-16 19:15:13.369988+05	10	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
51	2021-10-16 19:15:13.371611+05	9	Cobalt LT GS/16MTB-PLUS (2 позиция) улучшенная ком	3		21	1
52	2021-10-16 19:15:13.373171+05	8	Kia Ceed SW	3		21	1
53	2021-10-16 19:15:13.374845+05	7	Kia Ceed SW	3		21	1
54	2021-10-16 19:15:13.376457+05	6	Kia Ceed SW	3		21	1
55	2021-10-16 19:15:13.378178+05	5	COBALT LTZ/AT GX16/ATB-PLUS (4 позиция) улучшенная	3		21	1
56	2021-10-16 19:15:13.379869+05	4	Damas D11 (грузовой)	3		21	1
57	2021-10-16 19:15:13.38161+05	3	Damas D11 (грузовой)	3		21	1
58	2021-10-16 19:15:13.383315+05	2	Damas D11 (грузовой)	3		21	1
59	2021-10-16 19:15:13.385045+05	1	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	3		21	1
60	2021-10-17 11:37:14.460239+05	1	Yo'l fondi(1) : 3.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
61	2021-10-17 11:37:25.087351+05	27	Yo'l fondi ot kuchi(27) : 5.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
62	2021-10-17 11:37:31.097518+05	26	Yo'l fondi ot kuchi(26) : 7.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
63	2021-10-17 11:37:36.841416+05	25	Yo'l fondi ot kuchi(25) : 10.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
64	2021-10-17 11:37:41.820931+05	7	Yo'l fondi ot kuchi(7) : 11.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
65	2021-10-17 11:37:46.604226+05	6	Yo'l fondi ot kuchi(6) : 9.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
66	2021-10-17 11:37:52.42632+05	5	Yo'l fondi ot kuchi(5) : 6.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
67	2021-10-17 11:37:57.352494+05	4	Yo'l fondi ot kuchi(4) : 16.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
68	2021-10-17 11:38:02.751904+05	3	Yo'l fondi ot kuchi(3) : 13.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
69	2021-10-17 11:38:07.737086+05	2	Yo'l fondi ot kuchi(2) : 9.0%	2	[{"changed": {"fields": ["Service"]}}]	27	1
70	2021-10-17 12:15:25.89711+05	3	Yoqubov Salohiddin	2	[{"changed": {"fields": ["Foydalanuvchi roli"]}}]	6	1
71	2021-10-17 14:45:08.991598+05	29	Ro'yhatlash(29) : 10.0%	2	[{"changed": {"fields": ["Avtomobil yangi"]}}]	27	1
72	2021-10-17 14:45:13.623792+05	28	Ro'yhatlash(28) : 10.0%	2	[{"changed": {"fields": ["Avtomobil yangi"]}}]	27	1
73	2021-10-17 14:50:12.50226+05	29	Ro'yhatlash(29) : 10.0%	2	[{"changed": {"fields": ["Auktsiondan oligan"]}}]	27	1
74	2021-10-17 14:50:17.340881+05	28	Ro'yhatlash(28) : 10.0%	2	[{"changed": {"fields": ["Auktsiondan oligan"]}}]	27	1
75	2021-10-17 14:51:26.909303+05	29	Ro'yhatlash(29) : 10.0%	2	[{"changed": {"fields": ["Avtomobil turi"]}}]	27	1
76	2021-10-17 14:51:32.055315+05	28	Ro'yhatlash(28) : 10.0%	2	[{"changed": {"fields": ["Avtomobil turi"]}}]	27	1
77	2021-10-17 16:23:00.769685+05	7	ApplicationCashByModerator object (7)	3		35	1
78	2021-10-17 16:23:00.772399+05	6	ApplicationCashByModerator object (6)	3		35	1
79	2021-10-17 16:23:00.7744+05	5	ApplicationCashByModerator object (5)	3		35	1
80	2021-10-17 16:23:11.815027+05	5	Application(17): account_statement so'm	3		44	1
81	2021-10-17 16:23:11.818042+05	4	Application(17): account_statement so'm	3		44	1
82	2021-10-17 16:23:11.819032+05	3	Application(18): account_statement so'm	3		44	1
83	2021-10-17 16:23:11.820037+05	1	Application(18): account_statement so'm	3		44	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	user	user
7	user	bodytype
8	user	cartype
9	user	constant
10	user	device
11	user	district
12	user	fueltype
13	user	region
14	user	sms
15	user	section
16	user	quarter
17	user	organization
18	user	notification
19	user	color
20	user	carmodel
21	user	car
22	sites	site
23	service	amountbasecalculation
24	service	exampledocument
25	service	service
26	service	stateduty
27	service	statedutypercent
28	service	statedutyscore
29	account	emailaddress
30	account	emailconfirmation
31	socialaccount	socialaccount
32	socialaccount	socialapp
33	socialaccount	socialtoken
34	application	application
35	application	applicationcashbymoderator
36	application	applicationdocument
37	application	applicationdocumentattachment
38	authtoken	token
39	authtoken	tokenproxy
40	paycom	paycomtransaction
41	click	order
42	clickuz	transaction
43	service	document
44	service	paidstateduty
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
85	contenttypes	0001_initial	2021-10-17 12:53:06.27284+05
86	contenttypes	0002_remove_content_type_name	2021-10-17 12:53:06.27784+05
87	auth	0001_initial	2021-10-17 12:53:06.27984+05
88	auth	0002_alter_permission_name_max_length	2021-10-17 12:53:06.281841+05
89	auth	0003_alter_user_email_max_length	2021-10-17 12:53:06.283957+05
90	auth	0004_alter_user_username_opts	2021-10-17 12:53:06.284956+05
91	auth	0005_alter_user_last_login_null	2021-10-17 12:53:06.286957+05
92	auth	0006_require_contenttypes_0002	2021-10-17 12:53:06.289038+05
93	auth	0007_alter_validators_add_error_messages	2021-10-17 12:53:06.290038+05
94	auth	0008_alter_user_username_max_length	2021-10-17 12:53:06.292039+05
95	auth	0009_alter_user_last_name_max_length	2021-10-17 12:53:06.294038+05
96	auth	0010_alter_group_name_max_length	2021-10-17 12:53:06.296038+05
97	auth	0011_update_proxy_permissions	2021-10-17 12:53:06.300041+05
98	auth	0012_alter_user_first_name_max_length	2021-10-17 12:53:06.305043+05
99	service	0001_initial	2021-10-17 12:53:06.308038+05
100	application	0001_initial	2021-10-17 12:53:06.309833+05
101	application	0002_auto_20211017_1248	2021-10-17 12:53:06.311834+05
102	user	0001_initial	2021-10-17 12:53:06.313832+05
103	account	0001_initial	2021-10-17 12:53:06.315832+05
104	account	0002_email_max_length	2021-10-17 12:53:06.316599+05
105	admin	0001_initial	2021-10-17 12:53:06.319041+05
106	admin	0002_logentry_remove_auto_add	2021-10-17 12:53:06.320045+05
107	admin	0003_logentry_add_action_flag_choices	2021-10-17 12:53:06.322044+05
108	application	0003_auto_20211017_1248	2021-10-17 12:53:06.322927+05
109	authtoken	0001_initial	2021-10-17 12:53:06.32532+05
110	authtoken	0002_auto_20160226_1747	2021-10-17 12:53:06.327319+05
111	authtoken	0003_tokenproxy	2021-10-17 12:53:06.329319+05
112	click	0001_initial	2021-10-17 12:53:06.331319+05
113	click	0002_order_service	2021-10-17 12:53:06.334321+05
114	click	0003_order_user	2021-10-17 12:53:06.336319+05
115	clickuz	0001_initial	2021-10-17 12:53:06.338528+05
116	paycom	0001_initial	2021-10-17 12:53:06.339528+05
117	service	0002_auto_20211017_1248	2021-10-17 12:53:06.341527+05
118	sessions	0001_initial	2021-10-17 12:53:06.345527+05
119	sites	0001_initial	2021-10-17 12:53:06.347527+05
120	sites	0002_alter_domain_unique	2021-10-17 12:53:06.351528+05
121	socialaccount	0001_initial	2021-10-17 12:53:06.354528+05
122	socialaccount	0002_token_max_lengths	2021-10-17 12:53:06.356527+05
123	socialaccount	0003_extra_data_default_dict	2021-10-17 12:53:06.358527+05
124	service	0003_delete_paidstateduty	2021-10-17 12:56:11.817566+05
125	service	0004_paidstateduty	2021-10-17 12:56:34.861008+05
126	service	0005_auto_20211017_1307	2021-10-17 13:07:44.530724+05
127	service	0006_auto_20211017_1314	2021-10-17 13:14:08.14027+05
128	application	0004_applicationcashbymoderator_paid_state_duty	2021-10-17 16:22:26.60836+05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
xtun9kb9b8gpgjz2suzfxnyxet0wgfp4	.eJxVjEEOwiAQRe_C2pBCKVNcuvcMZGYYpGpoUtqV8e7apAvd_vfef6mI21ri1mSJU1JnZdTpdyPkh9QdpDvW26x5rusykd4VfdCmr3OS5-Vw_w4KtvKtBYwQIYHJBGSY2WemkFzwOcHI0o2DAyCxEvrOou8H4ywLeSche6veHx7hOMw:1mbOYC:BjKSzlzPA8Fc2mUHkFL-gaKpn2SC4vP7tXnygn14UmU	2021-10-29 19:51:12.808542+05
9qidv8jx25p2u1qw3sudz63hxow37d77	eyJsYW5nIjoidXoifQ:1mbP4B:DzyQkvqXM3FaAT6OVT03vbdA8_BH70FnkS5C7D6j5aE	2021-10-29 20:24:15.262769+05
i0a5uhpqz1fvettox70najegf2eqcx8x	eyJsYW5nIjoidXoifQ:1mbPl1:vsMi6dxZrCHf90c_nc5Z1eLYa_YY-1G1ZlShrybk8y0	2021-10-29 21:08:31.433541+05
5xdymnecfgjekn1dqheno6n92py8jw38	eyJsYW5nIjoidXoifQ:1mbQ0i:Muk3VAlyh4H-m-WgdzhAjbYlByHwKmK2ZeXyw8a_YDY	2021-10-29 21:24:44.768214+05
64a6zo0weddc26s8xzebcc35cusu9w7i	eyJsYW5nIjoidXoifQ:1mbTxj:uqHdTqcN4X9P9K0Pp60HcSbR_zlPrAwhFo5ow_5AoA8	2021-10-30 01:37:55.33222+05
yvpm32gls8yee2yhggev8zwuy72f9vo7	eyJsYW5nIjoidXoifQ:1mbU9Q:rMzjjgQriGTTGId8wJ03rcwPy0vAGp3UNyPEQhYo7Xo	2021-10-30 01:50:00.710837+05
av0v87f2fo7cs8yyqx010cbwoh3b40ui	eyJsYW5nIjoidXoifQ:1mbUbK:d_JX_2t-AyGwBGWCY1Rnhhyll_HXAZ_zgHCGz07JRj8	2021-10-30 02:18:50.814291+05
4dqbwacttz43fac4slfyok8wupqaroyi	eyJsYW5nIjoidXoifQ:1mbUgR:Tvt7sEkNPieh6ihbt6QcAgmg9jv5f5hHJrPEaFLgOLw	2021-10-30 02:24:07.180845+05
lr6loqgz2j4251o4esoz4g7312urr2k8	eyJsYW5nIjoidXoifQ:1mbUxR:gUKjauW7Tu5nzqRPG-L-PNsL1HL4jNjEznacqyDV2G0	2021-10-30 02:41:41.031423+05
ez3d02q3ipbsqiipk6aro3jkdg4ggoia	eyJsYW5nIjoidXoifQ:1mbWpJ:8bcz9JQTT8L8C2ecIjaONcyrTkwMK31FcQ02jMCj1iY	2021-10-30 04:41:25.753363+05
th2vn3b4jra9g18o1nshfpa7xd67agwd	eyJsYW5nIjoidXoifQ:1mbXMS:DNROjuxPu4edNxZBOX9NLDZvBWiAsUlO-mDJgiHDoJ0	2021-10-30 05:15:40.96442+05
sbgmrhq8i9o012tqq5946dtyv6isbd3b	eyJsYW5nIjoidXoifQ:1mbaSs:Xdjl8O25yMfK1mi4-DwxIOOHA9AhJdad9cZxV-wEclY	2021-10-30 08:34:30.950998+05
ev1tjdbvlq81d5fvo72v855v1j6htp0p	eyJsYW5nIjoiZW4ifQ:1mbb52:duHyZQUACKzghbNoePKTQfVAIdmZxNh4AWyON1x5V8Y	2021-10-30 09:13:56.553802+05
8titd6vaozwtitihjupj5h2w3mgte6in	.eJxVjEEOwiAQRe_C2pBCKVNcuvcMZGYYpGpoUtqV8e7apAvd_vfef6mI21ri1mSJU1JnZdTpdyPkh9QdpDvW26x5rusykd4VfdCmr3OS5-Vw_w4KtvKtBYwQIYHJBGSY2WemkFzwOcHI0o2DAyCxEvrOou8H4ywLeSche6veHx7hOMw:1mbb6x:iHu2WMPcrAsM41QKBqoKwVmg5Nc--4YcyrKUBc0ofsk	2021-10-30 09:15:55.856034+05
oyti4f31hp59obq0csaw1bcc9rw9hrgc	eyJsYW5nIjoidXoifQ:1mbbCT:Aoy9Yzroi2-YXnCTTZsRQ-OqebMR0-1lY_L9hi0MMd4	2021-10-30 09:21:37.789268+05
8e7a3i5ok01mgfpky0xwrqn2vvf68zki	eyJsYW5nIjoidXoifQ:1mbcqF:g3AcynLEmtCFQKsFHfD0hM_PeQNjJ3wvUtFQJsJ33AQ	2021-10-30 11:06:47.148659+05
zb9p0n3nh5dw5st91bufcb4gedlvj7s9	eyJsYW5nIjoidXoifQ:1mbdeO:6ln-lnKuWEhYnVO6FLpS988rg2sEmH1bC9qDJ-MK_Q0	2021-10-30 11:58:36.103295+05
jyqhx4l770ikllt7pfasg0e668p3k95k	eyJsYW5nIjoidXoifQ:1mbeBk:07wlI9xXNJ52ZcwU5xiThbDZ5dVuqxZT8bWH_FGI0AY	2021-10-30 12:33:04.094559+05
48cwv3njypv48bwo2skn1hw1hjadbjqh	.eJxVjDEOwyAQBP9CHSHACELK9HkDOrgjOLFAMqay8vdgyY3bmZ3d2QLlzR5s7ezGPPQt-95o9TMOOF1ZgPilcgj8jKryWMu2zoEfE37axl8VaXme28tBhpZHbZ2QKclokg4WiIwKEoXU0d5TQBxCTGKiGAxpZchpBQJBWaeTQqOQ_f5i_jvK:1mbgQI:ErfUkUGiLiatjDY8hJWMbNth2eAWvk8OERXc4B5_3Wo	2021-10-30 14:56:14.7743+05
3s87war36yijyz31yin39rwur1p1c7qb	eyJsYW5nIjoiZW4ifQ:1mbgpP:-Yk3IIX8DQusVz4xQDBFknSuKS_kge1wviwLxndwwWo	2021-10-30 15:22:11.251304+05
wgraephbmd7p9ti7qdsstw6zsk027ntu	eyJsYW5nIjoidXoifQ:1mbhhr:eXXr1_1Pl2cjpm_9dGhiEoqCqDdxAn6zo5pgNGtNIsc	2021-10-30 16:18:27.206629+05
x28xzoybdemwqn8zyopxfv3z7u8utj53	eyJsYW5nIjoidXoifQ:1mbi08:EVfWNncmJ1A2jV5v8CYqPHkeJP9BQ4j2nFtk0bwRMtc	2021-10-30 16:37:20.065056+05
ez31p5073x8xf7dv12pjaqknayf0uw0l	.eJxVjcEOgyAQRP-Fc0MEEaTH3vsNZHdZiq3BRPTU9N8riRev897MfMUM5SXugou4iQD7lsNeeQ1TPEJ1zRDow6WB-D5ai6SlbOuEsinypFU-l8jz43QvAxlqbl9OMSKgUwkdKiKyidBH422KbiTuxsE4h6zZ950G2w_KaGK0hn2yWvz-e-s8Lw:1mbjYR:1oOtcTrkpLWNizOYziMOLVadu6fcgQzDmdFXeVOLJ_U	2021-10-30 18:16:51.948095+05
dmflrhl3jve1tb8qd4z1a4tgv6jo0wtp	.eJxVjEEOwiAQRe_C2pBCKVNcuvcMZGYYpGpoUtqV8e7apAvd_vfef6mI21ri1mSJU1JnZdTpdyPkh9QdpDvW26x5rusykd4VfdCmr3OS5-Vw_w4KtvKtBYwQIYHJBGSY2WemkFzwOcHI0o2DAyCxEvrOou8H4ywLeSche6veHx7hOMw:1mbkS6:z1j77o432mPkvinSIs1tUBz-sduNKH7GGelRqcMJm64	2021-10-30 19:14:22.993135+05
skwfmlccdnjql3pv4c33o7n3ur175j6e	eyJsYW5nIjoidXoifQ:1mbkXs:RNJXP8l49stFh54iHzRWYZYtqlKMG9pLuGaApAw4_6Q	2021-10-30 19:20:20.656252+05
j9pm1o6sfc3zmb8bclobtn6npjnczauj	.eJxVjEEOwiAQRe_C2pBCKVNcuvcMZGYYpGpoUtqV8e7apAvd_vfef6mI21ri1mSJU1JnZdTpdyPkh9QdpDvW26x5rusykd4VfdCmr3OS5-Vw_w4KtvKtBYwQIYHJBGSY2WemkFzwOcHI0o2DAyCxEvrOou8H4ywLeSche6veHx7hOMw:1mblWJ:kgI9O_C-orh7P6ds-YMirIRv0M_9ycyWBy1VuaRzoUg	2021-10-30 20:22:47.148338+05
aac0041w4vylnt63vwldfnydmg5gek8s	eyJsYW5nIjoidXoifQ:1mbm3F:Xb4uYwaeNIQDc6kUimCJghp4ZMfBpt8Wlh8gbDEOn2c	2021-10-30 20:56:49.498299+05
yp5upl51mlgvcpwhl7ov33mvfyj4my2d	eyJsYW5nIjoidXoifQ:1mbmx8:q2DlpAGUDFw229-KJb-anBfzYNx3oqfkppIP6bMsdpw	2021-10-30 21:54:34.241071+05
3hgtmrgeyutvca896ijsignerssuc6dt	eyJsYW5nIjoidXoifQ:1mbn4s:f932sBTTmdjou-3er7iHOpXk0Cfs7Vg63B-TQn95BeU	2021-10-30 22:02:34.535318+05
l68ciprdf0ulpvodilmatn3p48uivcri	eyJsYW5nIjoidXoifQ:1mbpAN:R5NNPscE8bEC9IDOCixA2fuEfFtBTOux4XHiqqDW_00	2021-10-31 00:16:23.680779+05
pmzge4rymnqe0dz1y0b2hgs01j2t4iox	eyJsYW5nIjoidXoifQ:1mbqK3:_DePFIrxtDUTCmimwEA30yw9hW3V9iQ2QfORXXxpylc	2021-10-31 01:30:27.349058+05
mka09ys3hd79ptndtsfovczck20j6lyw	eyJsYW5nIjoidXoifQ:1mbrwY:ZkubJ6FquyA5PVPwB8Pejm_sUd4fnCuuYp8X-NJMBQc	2021-10-31 03:14:18.292296+05
a9lgm1fsudad4vqdhk84q2des77klgt5	eyJsYW5nIjoidXoifQ:1mbxY7:Jgxl4Eg1GX8l9CatDLO4rGc_uQhuMV8dmqunzWhqQ4c	2021-10-31 09:13:27.91669+05
ewzgxeicmaqow64q7un5apksoyjvjyak	.eJxVjEEOwiAQRe_C2pBCKVNcuvcMZGYYpGpoUtqV8e7apAvd_vfef6mI21ri1mSJU1JnZdTpdyPkh9QdpDvW26x5rusykd4VfdCmr3OS5-Vw_w4KtvKtBYwQIYHJBGSY2WemkFzwOcHI0o2DAyCxEvrOou8H4ywLeSche6veHx7hOMw:1mbxsS:13hZ6qnaqF0PSA0MC8QvkhtI3I1zPr8JULRXugAolMk	2021-10-31 09:34:28.270818+05
gq3f6d7ztc7x7zg9zniywgfcmfwqvhr1	eyJsYW5nIjoicnUifQ:1mbxzk:d9_KluEbM4FuHDf3WMvuRZNPl0Nsfu-qSwFcA-fWiQ4	2021-10-31 09:42:00.536414+05
6c5toran89nip7rtwphoixnnpd29o3c4	.eJxVjcsOwiAQRf-FtSE4LYO4dO83EB4zUm1oAu3K-O_SpAvd3dzHuW_h_LZmtzWqbkriKqw4_XrBxxeVPUhPXx6LjEtZ6xTkXpFH2uR9STTfju4fIPuW-5qRWBMQe0MjcwCTAHnEQZ0j6hEjoDas6EJdgiJEVoMGa402EK3u0Ln_d1LdxOcLr4w7Dw:1mbyUY:axoPHr4E8LN2AxoRKh-E_uluxF7sF3cXiNti5JTssH8	2021-10-31 10:13:50.444809+05
y1ggueognfhzvpri0sv2w72q9f96ti3r	.eJxVjcEOgyAQRP-Fc0MEEaTH3vsNZHdZiq3BRPTU9N8riRev897MfMUM5SXugou4iQD7lsNeeQ1TPEJ1zRDow6WB-D5ai6SlbOuEsinypFU-l8jz43QvAxlqbl9OMSKgUwkdKiKyidBH422KbiTuxsE4h6zZ950G2w_KaGK0hn2yWvz-e-s8Lw:1mbyiY:5qj_6JSo8JnV1Uk_XyDDnN71WPdfpDFsJybdohLs-fM	2021-10-31 10:28:18.958088+05
7a2bmh3j6tact6gliewzuq2ukjtx3w9i	.eJxVjM0OwiAQhN-FsyG4hUU8eu8zEH52pWogKe3J-O62SQ96m8z3zbyFD-tS_Npp9lMWV-HE6beLIT2p7iA_Qr03mVpd5inKXZEH7XJsmV63w_07KKGXbc1IbAiIgyXNHMFmQNY4qHNCozEBGsuKLrRFUITIajDgnDUWkjPi8wUAczeY:1mbyj0:2A7aZ4IE8uNJU32Y91aMXJsZVN6m84xQgdWkJnoNzwI	2021-10-31 10:28:46.847275+05
l9y10z5gkipufirwxb22ktyjqzpxvgyz	.eJxVjEEOwiAQRe_C2hBgKBSX7j0DYZhBqoYmpV0Z765NutDtf-_9l4hpW2vcOi9xInEWWpx-N0z5wW0HdE_tNss8t3WZUO6KPGiX15n4eTncv4Oaev3WRYFhnSGgBtIWOVh0BrwaR-09EYHJTIYSDuBKUNYV1C4FZQB5yCjeH9opN-8:1mbzmk:L6E9W2Rj3r0DkTq73i9eWROgAcZv6MdmJCvnlCTVjeA	2021-10-31 11:36:42.562857+05
dhxf11eb4m3vmdcdbunir8ul9u3aaghu	.eJxVjMsOgjAURP-la9O0QF8u3fMNpPdRQU2bUFgZ_92SsNDdZM6ZeYsp7ts87ZXXaSFxFUFcfjuI-OR8AHrEfC8SS97WBeShyJNWORbi1-10_w7mWOe2ZsNKD4NJqFKvybouGN1RgmAVmEFRwNgB9pERvG-Gp2TZELiWnUXx-QLq4zhk:1mc49u:kE1x4OtRIB6_pG3dLlaOs-qJ7o_Scs4YrV7g_opi2xU	2021-10-31 16:16:54.903366+05
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: paycom_paycomtransaction; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paycom_paycomtransaction (id, _id, request_id, order_key, amount, state, status, perform_datetime, cancel_datetime, created_datetime, reason) FROM stdin;
\.


--
-- Data for Name: service_amountbasecalculation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_amountbasecalculation (id, amount, start, stop, is_active) FROM stdin;
1	270000	2020-10-14	\N	t
\.


--
-- Data for Name: service_exampledocument; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_exampledocument (id, created_at, updated_at, is_active, title, key) FROM stdin;
1	2021-10-05 09:50:34.988+05	2021-10-05 10:28:12.568+05	t	Shaxsni tasdiqlovchi hujjat	passport
2	2021-10-05 09:50:46.953+05	2021-10-05 10:28:06.095+05	t	Hisob ma'lumotnomasi	account_statement
3	2021-10-05 09:50:58.906+05	2021-10-05 10:27:56.944+05	t	Oldi sotdi shartnomasi	contract_of_sale
4	2021-10-05 09:51:08.114+05	2021-10-05 10:27:42.25+05	t	Hadya shartnomasi	gift_agreement
\.


--
-- Data for Name: service_paidstateduty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_paidstateduty (id, is_return, created_date, application_id, percent_id, score_id) FROM stdin;
6	f	2021-10-17	17	20	29
7	f	2021-10-17	17	13	7
8	f	2021-10-17	17	24	37
\.


--
-- Data for Name: service_service; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_service (id, short_title, long_title, key, is_active, "desc", photo, deadline, instruction, created_date, sort) FROM stdin;
1	Hisob ma'lumotnomasi	Hisob ma'lumotnomasiga asosan ro'yhatga qo'yish	account_statement	t	Avtotransport vositasi avtosalondan xarid qilingan holatda, unga hisob ma'lumotnomasi taqdim etiladi. Ushbu hisob ma'lumotnomasiga asosan avtotransport vositasi ro'yhatdan o'tkaziladi.	https://www.freeiconspng.com/uploads/contract-icon-0.png	1 kundan 10 kungacha	Ariza jo'natish uchun Ariza topshirish formasiga kirib, ushbu formada so'ralgan barcha ma'lumotlarni kiritish yoki YHXB RIB yoki TRIB'lar huzuridagi maxsus operatorlar yordamidan foydalanishingiz mumkin.	2021-10-03 17:05:24+05	1
2	Oldi sotdi shartnomasi	Oldi sotdi shartnomasi	contract_of_sale	t	It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).	https://www.pngkit.com/png/full/312-3127999_sell-your-junk-car-to-us-sale-car.png	1-10	Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).	2021-10-03 17:05:24+05	2
3	Hadya shartnomasi	Hadya shartnomasiga asosan transport vositasiga davlat raqam belgisi olish	gift_agreement	t	Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.	https://www.freeiconspng.com/uploads/contract-icon-0.png	1-10	Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.	2021-10-05 09:44:53+05	3
4	Qayta jihozlash	Qayta jihozlash	re_equipment	f	There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.	https://www.freeiconspng.com/uploads/contract-icon-0.png	10-15	There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text.	2021-10-05 14:01:19+05	4
5	TP almashtirish	Qayd etish guvohnomasini almashtirish	replace_tp	t	Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words	https://www.freeiconspng.com/uploads/contract-icon-0.png	1-10	Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words	2021-10-06 08:33:39+05	4
6	DRB almashtirish	Davlat raqam belgisi va qayd etish guvohnomasini almshtirish	replace_number_and_tp	t	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fdriver&psig=AOvVaw3Erus_7XdKXh9yTo4ghUpB&ust=1633588020254000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCNiX9d6TtfMCFQAAAAAdAAAAABAD	5-10	Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.	2021-10-15 20:53:42+05	5
\.


--
-- Data for Name: service_service_document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_service_document (id, service_id, exampledocument_id) FROM stdin;
1	1	1
2	1	2
3	2	1
4	2	3
5	3	1
6	3	4
7	4	1
8	5	1
9	6	1
\.


--
-- Data for Name: service_stateduty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_stateduty (id, created_date, application_id, percent_id, score_id, is_return) FROM stdin;
\.


--
-- Data for Name: service_statedutypercent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_statedutypercent (id, title, state_duty, person_type, car_is_new, is_old_number, lost_number, lost_technical_passport, is_auction, start, stop, percent) FROM stdin;
8	Yuridik shaxslarning yuk avtomobillarini texnik ko'rikdan o'tkazish uchun	3	1	f	f	f	f	f	0	0	40
9	Yuridik shaxslarning yengil avtomobillarini texnik ko'rikdan o'tkazish uchun	3	1	f	f	f	f	f	0	0	10
10	Jismony shaxslarning avtobus va mikroavtobus avtomobillarini texnik ko'rikdan o'tkazish uchun	3	1	f	f	f	f	f	0	0	20
11	Jismony shaxslarning yuk avtomobillarini texnik ko'rikdan o'tkazish uchun	3	0	f	f	f	f	f	0	0	10
12	Jismony shaxslarning yengil avtomobillarini texnik ko'rikdan o'tkazish uchun	3	0	f	f	f	f	f	0	0	10
13	Yangi qayd etish guvohnomasi uchun	4	0	f	f	f	f	f	0	0	70
18	Davlat raqam belgisi uchun to'lov	5	0	f	t	t	f	f	0	0	300
19	Davlat raqam belgisi uchun to'lov	5	0	f	f	t	f	f	0	0	450
20	Davlat raqam belgisi uchun to'lov	5	0	t	f	f	f	f	0	0	160
21	Davlat raqam belgisi uchun to'lov	5	0	f	f	f	f	f	0	0	150
22	Qayta ro'yhatlash uchun to'lov	6	0	f	f	f	f	f	0	0	10
23	Yo'qolgan qayd etish guvohnomasi uchun jarima	7	0	f	f	f	t	f	0	0	30
24	Shartnoma tuzilgan sana 10 kundan kechikganligi uchun jarima	7	0	f	f	f	f	f	0	0	50
1	Yo'l fondi uchun to'lov	1	0	f	f	f	f	f	0	0	3
27	Moto transport vositasi yo'l fondi uchun to'lov	2	0	f	f	f	f	f	7	0	5
26	Moto transport vositasi yo'l fondi uchun to'lov	2	0	f	f	f	f	f	3	7	7
25	Moto transport vositasi yo'l fondi uchun to'lov	2	0	f	f	f	f	f	0	3	10
7	Yengil avtomobil yo'l fondi uchun to'lov	2	0	f	f	f	f	f	0	3	11
6	Yengil avtomobil yo'l fondi uchun to'lov	2	0	f	f	f	f	f	3	7	9
5	Yengil avtomobil yo'l fondi uchun to'lov	2	0	f	f	f	f	f	7	0	6
4	Yuk avtomobil yo'l fondi uchun to'lov	2	0	f	f	f	f	f	0	3	16
3	Yuk avtomobil yo'l fondi uchun to'lov	2	0	f	f	f	f	f	3	7	13
2	Yuk avtomobil yo'l fondi uchun to'lov	2	0	f	f	f	f	f	7	0	9
29	YHXB noziri ko'rigidan o'tkazish uchun	5	1	t	f	f	f	t	0	0	10
28	YHXB noziri ko'rigidan o'tkazish uchun	5	0	t	f	f	f	t	0	0	10
\.


--
-- Data for Name: service_statedutypercent_car_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_statedutypercent_car_type (id, statedutypercent_id, cartype_id) FROM stdin;
1	2	1
2	3	1
3	4	1
4	5	2
5	6	2
6	7	2
7	8	1
8	9	2
9	10	3
10	10	7
11	11	1
12	12	2
13	25	5
14	26	5
15	27	5
16	18	1
17	18	2
18	19	1
19	19	2
20	20	1
21	20	2
22	21	1
23	21	2
24	28	2
25	29	2
26	29	1
27	28	1
\.


--
-- Data for Name: service_statedutypercent_service; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_statedutypercent_service (id, statedutypercent_id, service_id) FROM stdin;
1	18	1
2	18	2
3	18	3
4	18	6
5	19	1
6	19	2
7	19	3
8	19	6
9	20	1
10	20	2
11	20	3
12	20	6
13	21	1
14	21	2
15	21	3
16	21	6
17	22	2
18	22	3
19	22	4
20	22	5
21	22	6
22	28	1
23	29	1
24	1	1
25	1	2
26	1	3
27	27	1
28	27	2
29	27	3
30	26	1
31	26	2
32	26	3
33	25	1
34	25	2
35	25	3
36	7	1
37	7	2
38	7	3
39	6	1
40	6	2
41	6	3
42	5	1
43	5	2
44	5	3
45	4	1
46	4	2
47	4	3
48	3	1
49	3	2
50	3	3
51	2	1
52	2	2
53	2	3
\.


--
-- Data for Name: service_statedutyscore; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service_statedutyscore (id, state_duty, score, created_date, updated_date, district_id, region_id) FROM stdin;
1	4	4014228600062403422232179	2021-03-25 08:08:05.724+05	2021-03-25 08:08:05.724+05	57	3
2	4	4014228605062323422232179	2021-03-25 08:08:27.69+05	2021-03-25 08:08:27.69+05	55	3
3	4	4014228608062423422232179	2021-03-25 08:08:42.435+05	2021-03-25 08:08:42.435+05	58	3
4	4	4014228604064033422231279	2021-03-25 08:08:59.663+05	2021-03-25 08:08:59.663+05	53	3
5	4	4014228605062073422232179	2021-03-25 08:09:18.034+05	2021-03-25 08:09:18.034+05	48	3
6	4	4014228607064013422232179	2021-03-25 08:09:36.361+05	2021-03-25 08:09:36.361+05	47	3
7	4	4014228605062193422232179	2021-03-25 08:09:50.917+05	2021-03-25 08:09:50.917+05	52	3
8	2	4014228603062403422204179	2021-03-25 08:10:15.843+05	2021-03-25 08:10:15.843+05	57	3
9	2	4014228607064033422204179	2021-03-25 08:10:35.352+05	2021-03-25 08:10:35.352+05	53	3
10	2	4014228608062193422204179	2021-03-25 08:10:50.061+05	2021-03-25 08:10:50.061+05	52	3
11	2	4014228608062323422204179	2021-03-25 08:11:03.593+05	2021-03-25 08:11:03.593+05	55	3
12	2	4014228608062073422204179	2021-03-25 08:11:17.931+05	2021-03-25 08:11:17.931+05	48	3
13	2	4014228604064013422204179	2021-03-25 08:11:30.075+05	2021-03-25 08:11:30.075+05	47	3
14	2	4014228600062423422204179	2021-03-25 08:11:47.835+05	2021-03-25 08:11:47.835+05	58	3
15	3	4014228602062403422210179	2021-03-25 08:12:28.737+05	2021-03-25 08:12:28.737+05	57	3
16	3	4014228606064033422210179	2021-03-25 08:12:45.394+05	2021-03-25 08:12:45.394+05	53	3
17	3	4014228607062073422210179	2021-03-25 08:12:59.599+05	2021-03-25 08:12:59.599+05	48	3
18	3	4014228607062323422210179	2021-03-25 08:13:13.454+05	2021-03-25 08:13:13.454+05	55	3
19	3	4014228609064013422210179	2021-03-25 08:13:27.335+05	2021-03-25 08:13:27.335+05	47	3
20	3	4014228604062423422210179	2021-03-25 08:13:41.394+05	2021-03-25 08:13:41.394+05	58	3
21	3	4014228607062193422210179	2021-03-25 08:13:55.085+05	2021-03-25 08:13:55.085+05	52	3
22	1	1000108602062403422221093	2021-03-25 08:14:14.839+05	2021-03-25 08:14:14.839+05	57	3
23	1	1000108606064033422221093	2021-03-25 08:14:33.761+05	2021-03-25 08:14:33.761+05	53	3
24	1	1000108607062193422221093	2021-03-25 08:14:48.294+05	2021-03-25 08:14:48.294+05	52	3
25	1	1000108607062323422221093	2021-03-25 08:15:02.679+05	2021-03-25 08:15:02.679+05	55	3
26	1	1000108607062073422221093	2021-03-25 08:15:15.397+05	2021-03-25 08:15:15.397+05	48	3
27	1	1000108609064013422221093	2021-03-25 08:15:28.134+05	2021-03-25 08:15:28.134+05	47	3
28	1	1000108604062423422221093	2021-03-25 08:15:40.693+05	2021-03-25 08:15:40.693+05	58	3
29	5	4014228603064013422948179	2021-03-25 08:16:26.175+05	2021-03-25 08:16:26.175+05	\N	\N
36	6	4014228603064013422947179	2021-03-25 08:18:05.703+05	2021-03-25 08:18:05.703+05	\N	\N
37	7	4014228603064013430105179	2021-03-25 08:18:16.182+05	2021-03-25 08:18:16.182+05	\N	\N
\.


--
-- Data for Name: socialaccount_socialaccount; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialaccount (id, provider, uid, last_login, date_joined, extra_data, user_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialapp (id, provider, name, client_id, secret, key) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialapp_sites; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialapp_sites (id, socialapp_id, site_id) FROM stdin;
\.


--
-- Data for Name: socialaccount_socialtoken; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.socialaccount_socialtoken (id, token, token_secret, expires_at, account_id, app_id) FROM stdin;
\.


--
-- Data for Name: user_bodytype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_bodytype (id, title, is_active, created_date) FROM stdin;
1	SEDAN	t	2021-10-03 18:30:28.36+05
2	Belgilanmagan	t	2021-10-11 09:10:54.86+05
\.


--
-- Data for Name: user_car; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_car (id, full_weight, empty_weight, body_number, chassis_number, engine_number, made_year, engine_power, old_number, old_technical_passport, is_old_number, given_technical_passport, created_date, lost_technical_passport, lost_number, is_confirm, confirm_date, is_technical_confirm, technical_confirm_date, is_new, price, is_auction, given_number, is_replace_number, body_type_id, color_id, history_id, model_id, re_color_id, type_id) FROM stdin;
30	25	25	AX9595XA95X9A	\N	AX5959XA	2021-10-04	38	80H956AB	AF9565629	f		2021-10-17 09:43:17.266384+05	f	f	f	\N	f	\N	f	0	f	\N	t	1	81	\N	35	\N	2
31	0.00	0.00	X959SA5S9AS9	\N	X8959ASD	2021-10-04	59	\N	AF9565945	f		2021-10-17 09:45:25.247703+05	f	f	f	\N	f	\N	f	0	f	\N	f	1	81	\N	9	\N	1
32	00.0	00.0	95A9X59AS9X	\N	AXAS995	2021-10-04	56	\N		f		2021-10-17 09:51:30.522122+05	f	f	f	\N	f	\N	t	78238000	f	\N	t	1	81	\N	10	\N	2
33	0.00	0.00	959XASASX95A9	\N	XX95A9S5D	2021-10-04	106	\N		f		2021-10-17 09:53:16.537285+05	f	f	f	\N	f	\N	t	78238000	f	\N	t	1	81	\N	62	\N	2
34	0.00	0.00	9X5A9X5A9X59A5X9	\N	X5A95A9S5D9	2021-10-04	95	80H95ABC	AF956505054	f		2021-10-17 09:57:59.66853+05	f	f	f	\N	f	\N	f	0	f	\N	t	1	81	\N	31	\N	2
35	3800	3200	95XA95S9XA59	\N	X9595ASDX	2021-10-04	388	80H956AA	AF9506568	f		2021-10-17 10:22:51.598969+05	f	f	f	\N	f	\N	f	0	f	\N	t	1	81	\N	31	\N	2
36	2000	1950	AZX54654654654	\N	AZX56456465465	2021-10-13	80	\N		f		2021-10-17 14:41:53.370853+05	f	f	f	\N	f	\N	t	90000000	t	80979HBA	t	1	81	\N	33	\N	1
\.


--
-- Data for Name: user_car_device; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_car_device (id, car_id, device_id) FROM stdin;
\.


--
-- Data for Name: user_car_fuel_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_car_fuel_type (id, car_id, fueltype_id) FROM stdin;
22	30	2
23	31	2
24	32	2
25	33	2
26	34	2
27	35	2
28	36	1
\.


--
-- Data for Name: user_car_re_fuel_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_car_re_fuel_type (id, car_id, fueltype_id) FROM stdin;
\.


--
-- Data for Name: user_carmodel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_carmodel (id, title, creator, is_local, is_truck, is_active, created_date, created_user_id) FROM stdin;
6	Chevrolet Tracker Turbo 1.0 LS MT (z-я позиция)	GM Uzbekistan	t	f	t	2021-10-15 09:16:16+05	1
7	Chevrolet Tracker Turbo 1.0 LT A/T (2-я позиция)	GM Uzbekistan	t	f	t	2021-10-15 09:18:23+05	1
8	Chevrolet Tracker Redline A/T (3-я позиция)	GM Uzbekistan	t	f	t	2021-10-15 09:18:32+05	1
9	Damas D11 (грузовой)	GM Uzbekistan	t	f	t	2021-10-15 09:18:42+05	1
10	Damas D2 DLX B6O А90 (Deluxe пассажирский)	GM Uzbekistan	t	f	t	2021-10-15 09:18:52+05	1
11	Damas LABO MXH T79 (пикап)	GM Uzbekistan	t	f	t	2021-10-15 09:19:00+05	1
12	SPARK LS M300M-125(2 позиция МКПП)	GM Uzbekistan	t	f	t	2021-10-15 09:19:08+05	1
13	SPARK LT/АТ M300M/GC/-A125 (3 позиция АКПП)	GM Uzbekistan	t	f	t	2021-10-15 09:19:16+05	1
14	Ravon R2 LS M/T Optimum Plus	GM Uzbekistan	t	f	t	2021-10-15 09:19:24+05	1
15	Ravon R2 LT A/T Elegant Plus	GM Uzbekistan	t	f	t	2021-10-15 09:19:33+05	1
16	NEXIA 3 LT AV-GS16 (2 позиция)	GM Uzbekistan	t	f	t	2021-10-15 09:19:40+05	1
17	NEXIA 3 LTZ/AT AV-GX16AT	GM Uzbekistan	t	f	t	2021-10-15 09:19:49+05	1
18	Cobalt LT GS/16MTB-PLUS (2 позиция) улучшенная ком	GM Uzbekistan	t	f	t	2021-10-15 09:19:57+05	1
19	COBALT LTZ/AT GX16/ATB-PLUS (4 позиция) улучшенная	GM Uzbekistan	t	f	t	2021-10-15 09:20:06+05	1
20	Lacetti SX L3-15 (1 позиция)	GM Uzbekistan	t	f	t	2021-10-15 09:20:14+05	1
21	Lacetti SX CNG L3-15G (1 позиция с ГБО)	GM Uzbekistan	t	f	t	2021-10-15 09:20:22+05	1
22	Lacetti CDX/AT L15-15(3 позиция)	GM Uzbekistan	t	f	t	2021-10-15 09:20:29+05	1
23	Lacetti L-ELEGANT/AT PLUS (Топовая комплектация по	GM Uzbekistan	t	f	t	2021-10-15 09:20:37+05	1
24	CAPTIVA 5T Premier	GM Uzbekistan	t	f	t	2021-10-15 09:22:59+05	1
25	CAPTIVA 5 LT	GM Uzbekistan	t	f	t	2021-10-15 09:23:04+05	1
26	MALIBU LT/АТ 1,5 Turbo Facelift 2019	GM Uzbekistan	t	f	t	2021-10-15 09:23:11+05	1
27	MALIBU LT/АТ 2,0 Turbo Facelift 2019	GM Uzbekistan	t	f	t	2021-10-15 09:23:22+05	1
28	MALIBU LTZ/АТ 2,0 Turbo Premier	GM Uzbekistan	t	f	t	2021-10-15 09:23:29+05	1
29	Chevrolet Tahoe (минимальная комплектация)	GM Uzbekistan	t	f	t	2021-10-15 09:23:38+05	1
30	Chevrolet Tahoe Premier (максимальная комплектация	GM Uzbekistan	t	f	t	2021-10-15 09:23:54+05	1
31	Chevrolet Traverse (минимальная комплектация)	GM Uzbekistan	t	f	t	2021-10-15 09:24:04+05	1
32	Chevrolet Traverse Premier (максимальная комплекта	GM Uzbekistan	t	f	t	2021-10-15 09:24:11+05	1
33	Chevrolet Trailblazer(минимальная комплектация)	GM Uzbekistan	t	f	t	2021-10-15 09:24:50+05	1
34	Chevrolet Trailblazer LTZ 6АT (максимальная)	GM Uzbekistan	t	f	t	2021-10-15 09:25:03+05	1
35	Chevrolet Equinox (минимальная комплектация)	GM Uzbekistan	t	f	t	2021-10-15 09:25:21+05	1
36	Chevrolet Equinox RS (максимальная комплектация)	GM Uzbekistan	t	f	t	2021-10-15 09:25:32+05	1
37	Vesta SW Cross	Lada	f	f	t	2021-10-15 09:25:44+05	1
38	XRAY Cross	Lada	f	f	t	2021-10-15 09:28:09+05	1
39	Niva Travel	Lada	f	f	t	2021-10-15 09:28:31+05	1
40	Largus Cross	Lada	f	f	t	2021-10-15 09:29:57+05	1
41	Kia K5	Kia Uzbekistan	f	f	t	2021-10-15 09:34:45+05	1
42	Kia Stinger	Kia Uzbekistan	f	f	t	2021-10-15 09:35:03+05	1
43	Kia K8	Kia	f	f	t	2021-10-15 09:39:48+05	1
44	Kia Sorento	Kia	f	f	t	2021-10-15 09:41:19+05	1
45	Kia Seltos	Kia	f	f	t	2021-10-15 09:42:09+05	1
46	Kia Soul	Kia	f	f	t	2021-10-15 09:42:23+05	1
47	Kia Carnival	Kia	f	f	t	2021-10-15 09:42:31+05	1
48	Kia Ceed	Kia	f	f	t	2021-10-15 09:42:42+05	1
49	Kia Ceed SW	Kia	f	f	t	2021-10-15 09:43:55+05	1
50	Kia Cerato	\N	f	f	t	2021-10-15 09:44:09+05	1
51	Kia K900	\N	f	f	t	2021-10-15 09:44:15+05	1
52	Kia Mohave	Kia	f	f	t	2021-10-15 09:45:01+05	1
53	Kia Optima	Kia	f	f	t	2021-10-15 09:45:13+05	1
54	Kia Picanto	Kia	f	f	t	2021-10-15 09:45:23+05	1
55	Kia ProCeed	Kia	f	f	t	2021-10-15 09:45:33+05	1
56	Kia Rio	Kia	f	f	t	2021-10-15 09:45:43+05	1
57	Kia Rio X-line	Kia	f	f	t	2021-10-15 09:45:55+05	1
58	Kia Sorento Prime	Kia	f	f	t	2021-10-15 09:46:05+05	1
59	Kia Sportage	Kia	f	f	t	2021-10-15 09:46:24+05	1
60	Kia XCeed	Kia	f	f	t	2021-10-15 09:46:37+05	1
61	Kia Avella	Kia	f	f	t	2021-10-15 09:46:47+05	1
62	Kia Avella Delta	Kia	f	f	t	2021-10-15 09:47:00+05	1
63	Kia Bongo	Kia	f	f	t	2021-10-15 09:47:10+05	1
64	Kia Cadenza	Kia	f	f	t	2021-10-15 09:47:21+05	1
65	Kia Capital	Kia	f	f	t	2021-10-15 09:47:32+05	1
66	Kia Carens	Kia	f	f	t	2021-10-15 09:47:45+05	1
67	Kia Carnival	Kia	f	f	t	2021-10-15 09:47:56+05	1
68	Kia Ceed GT	Kia	f	f	t	2021-10-15 10:33:58+05	1
69	Kia Ceed I	Kia	f	f	t	2021-10-15 10:34:10+05	1
70	Kia Ceed II	Kia	f	f	t	2021-10-15 10:34:21+05	1
71	Kia Ceed SW I	Kia	f	f	t	2021-10-15 10:34:29+05	1
72	Kia Ceed SW II	Kia	f	f	t	2021-10-15 10:34:37+05	1
73	Kia Cerato I	Kia	f	f	t	2021-10-15 10:34:49+05	1
74	Kia Cerato II	Kia	f	f	t	2021-10-15 10:35:02+05	1
\.


--
-- Data for Name: user_cartype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_cartype (id, title, is_active, created_date) FROM stdin;
1	YUK	t	2021-03-24 20:04:51.625+05
2	YENGIL	t	2021-03-24 20:04:57.925+05
3	AVTOBUS	t	2021-03-25 08:03:33.102+05
4	TIRKAMA	t	2021-03-25 08:03:39.74+05
5	MOTONAKLIYOT	t	2021-03-25 08:03:49.775+05
6	ELEKTRONAKLIYOT	t	2021-03-25 08:03:59.882+05
7	MIKROAVTOBUS	t	2021-03-25 08:04:11.36+05
8	MAXSUS	t	2021-03-25 08:04:18.122+05
9	BOSHQA	t	2021-03-25 08:04:28.921+05
10	YUK-YO'LOVCHI TASHUVCHI	t	2021-03-25 08:04:41.37+05
11	YARIM TIRKAMA	t	2021-03-25 08:05:34.841+05
\.


--
-- Data for Name: user_color; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_color (id, title, is_active, created_date, created_user_id) FROM stdin;
81	GAZ (Summit white)	t	2021-10-11 09:11:19.152+05	6
82	YASHIL	t	2021-10-15 18:44:44.94+05	7
83	sd	t	2021-10-15 18:45:00.485+05	\N
\.


--
-- Data for Name: user_constant; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_constant (id, key, value, info) FROM stdin;
\.


--
-- Data for Name: user_device; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_device (id, title, is_active, created_date) FROM stdin;
1	Ambulance	t	2021-10-05 11:20:10.793+05
2	Migalka	t	2021-10-05 11:20:14.807+05
3	O'rgatuvchi	t	2021-10-05 11:20:20.413+05
4	Evakuator	t	2021-10-05 11:20:27.737+05
\.


--
-- Data for Name: user_district; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_district (id, title, sort, is_active, region_id) FROM stdin;
15	Amudaryo tumani	1	t	1
16	Beruniy tumani	1	t	1
17	Kegayli tumani	1	t	1
18	Qonliko'l tumani	1	t	1
19	Qorao'zak tumani	1	t	1
20	Qo'ng'irot tumani	1	t	1
21	Mo'ynoq tumani	1	t	1
22	Nukus tumani	1	t	1
23	Nukus shahri	1	t	1
24	Taxtako'pir tumani	1	t	1
25	To'rtko'l tumani	1	t	1
26	Xo'jayli tumani	1	t	1
27	Chimboy tumani	1	t	1
28	Shumanay tumani	1	t	1
29	Ellikqal'a tumani	1	t	1
30	Andijon shahri	1	t	2
31	Andijon tumani	1	t	2
32	Asaka tumani	1	t	2
33	Baliqchi tumani	1	t	2
34	Buloqboshi tumani	1	t	2
35	Bo'z tumani	1	t	2
36	Jalaquduq tumani	1	t	2
37	Izbosgan tumani	1	t	2
38	Qorasuv shahri	1	t	2
39	Qo'rg'ontepa tumani	1	t	2
40	Marhamat tumani	1	t	2
41	Oltinko'l tumani	1	t	2
42	Paxtaobod tumani	1	t	2
43	Ulug'nor tumani	1	t	2
44	Xonabod tumani	1	t	2
45	Xo'jaobod shahri	1	t	2
46	Shaxrixon tumani	1	t	2
47	Buxoro shahri	1	t	3
48	Buxoro tumani	1	t	3
49	Vobkent tumani	1	t	3
50	G├жijduvon tumani	1	t	3
51	Jondor tumani	1	t	3
52	Kogon tumani	1	t	3
53	Kogon shahri	1	t	3
54	Qorako├жl tumani	1	t	3
55	Qorovulbozor tumani	1	t	3
56	Olot tumani	1	t	3
57	Peshku tumani	1	t	3
58	Romitan tumani	1	t	3
59	Shofirkon tumani	1	t	3
60	Arnasoy tumani	1	t	4
61	Baxmal tumani	1	t	4
62	G├жallaorol tumani	1	t	4
63	Do├жstlik tumani	1	t	4
64	Sh.Rashidov tumani	1	t	4
65	Jizzax shahri	1	t	4
66	Zarbdor tumani	1	t	4
67	Zafarobod tumani	1	t	4
68	Zomin tumani	1	t	4
69	Mirzacho├жl tumani	1	t	4
70	Paxtakor tumani	1	t	4
71	Forish tumani	1	t	4
72	Yangiobod tumani	1	t	4
73	G├жuzor tumani	1	t	5
74	Dehqonobod tumani	1	t	5
75	Qamashi tumani	1	t	5
76	Qarshi tumani	1	t	5
77	Qarshi shahri	1	t	5
78	Kasbi tumani	1	t	5
79	Kitob tumani	1	t	5
80	Koson tumani	1	t	5
81	Mirishkor tumani	1	t	5
82	Muborak tumani	1	t	5
83	Nishon tumani	1	t	5
84	Chiroqchi tumani	1	t	5
85	Shahrisabz tumani	1	t	5
86	Yakkabog├ж tumani	1	t	5
87	Zarafshon shahri	1	t	6
88	Karmana tumani	1	t	6
89	Qiziltepa tumani	1	t	6
90	Konimex tumani	1	t	6
91	Navbahor tumani	1	t	6
92	Navoiy shahri	1	t	6
93	Nurota tumani	1	t	6
94	Tomdi tumani	1	t	6
95	Uchquduq tumani	1	t	6
96	Xatirchi tumani	1	t	6
97	Kosonsoy tumani	1	t	7
98	Mingbuloq tumani	1	t	7
99	Namangan tumani	1	t	7
100	Namangan shahri	1	t	7
101	Norin tumani	1	t	7
102	Pop tumani	1	t	7
103	To├жraqo├жrg├жon tumani	1	t	7
104	Uychi tumani	1	t	7
105	Uchqo├жrg├жon tumani	1	t	7
106	Chortoq tumani	1	t	7
107	Chust tumani	1	t	7
108	Yangiqo├жrg├жon tumani	1	t	7
109	Bulung├жur tumani	1	t	8
110	Jomboy tumani	1	t	8
111	Ishtixon tumani	1	t	8
112	Kattaqo├жrg├жon tumani	1	t	8
113	Kattaqo├жrg├жon shahri	1	t	8
114	Qo├жshrabot tumani	1	t	8
115	Narpay tumani	1	t	8
116	Nurabod tumani	1	t	8
117	Oqdaryo tumani	1	t	8
118	Payariq tumani	1	t	8
119	Pastarg├жom tumani	1	t	8
120	Paxtachi tumani	1	t	8
121	Samarqand tumani	1	t	8
122	Samarqand shahri	1	t	8
123	Toyloq tumani	1	t	8
124	Urgut tumani	1	t	8
125	Angor tumani	1	t	9
126	Boysun tumani	1	t	9
127	Denov tumani	1	t	9
128	Jarqo'rg'on tumani	1	t	9
129	Qiziriq tumani	1	t	9
130	Qo'mqo'rg'on tumani	1	t	9
131	Muzrabot tumani	1	t	9
132	Oltinsoy tumani	1	t	9
133	Sariosiy tumani	1	t	9
134	Termiz tumani	1	t	9
135	Termiz shahri	1	t	9
136	Uzun tumani	1	t	9
137	Sherobod tumani	1	t	9
138	Sho'rchi tumani	1	t	9
139	Boyovut tumani	1	t	10
140	Guliston tumani	1	t	10
141	Guliston shahri	1	t	10
142	Mirzaobod tumani	1	t	10
143	Oqoltin tumani	1	t	10
144	Sayxunobod tumani	1	t	10
145	Sardoba tumani	1	t	10
146	Sirdaryo tumani	1	t	10
147	Xavos tumani	1	t	10
148	Shirin shahri	1	t	10
149	Yangiyer shahri	1	t	10
150	Angiren shahri	1	t	11
151	Bekabod tumani	1	t	11
152	Bekabod shahri	1	t	11
153	Bo'ka tumani	1	t	11
154	Bo'stonliq tumani	1	t	11
155	Zangiota tumani	1	t	11
156	Qibray tumani	1	t	11
157	Quyichirchiq tumani	1	t	11
158	Oqqo'rg'on tumani	1	t	11
159	Olmaliq shahri	1	t	11
160	Ohangaron tumani	1	t	11
161	Parkent tumani	1	t	11
162	Piskent tumani	1	t	11
163	O'rtachirchiq tumani	1	t	11
164	Chinoz tumani	1	t	11
165	Chirchiq shahri	1	t	11
166	Yuqorichirchiq tumani	1	t	11
167	Yangiyo'l tumani	1	t	11
168	Beshariq tumani	1	t	12
169	Bog'dod tumani	1	t	12
170	Buvayda tumani	1	t	12
171	Dang'ara tumani	1	t	12
172	Yozyovon tumani	1	t	12
173	Quva tumani	1	t	12
174	Quvasoy shahri	1	t	12
175	Qo'qon shahri	1	t	12
176	Qo'shtepa tumani	1	t	12
177	Marg'ilon shahri	1	t	12
178	Oltiariq tumani	1	t	12
179	Rishton tumani	1	t	12
180	So'x tumani	1	t	12
181	Toshloq tumani	1	t	12
182	Uchko'prik tumani	1	t	12
183	O'zbekiston tumani	1	t	12
184	Farg'ona tumani	1	t	12
185	Farg'ona shahri	1	t	12
186	Furqat tumani	1	t	12
187	Bog'ot tumani	1	t	13
188	Gurlan tumani	1	t	13
189	Qo'shko'pir tumani	1	t	13
190	Urganch tumani	1	t	13
191	Urganch shahri	1	t	13
192	Xiva tumani	1	t	13
193	Xazarasp tumani	1	t	13
194	Xonqa tumani	1	t	13
195	Shavot tumani	1	t	13
196	Yangiariq tumani	1	t	13
197	Yangibozor tumani	1	t	13
198	Bektimer tumani	1	t	14
199	M.Ulug'bek tumani	1	t	14
200	Mirobod tumani	1	t	14
201	Olmazor tumani	1	t	14
202	Sergeli tumani	1	t	14
203	Uchtepa tumani	1	t	14
204	Yashnobod tumani	1	t	14
205	Chilonzor tumani	1	t	14
206	Shayxontohur tumani	1	t	14
207	Yunusobod tumani	1	t	14
208	Yakkasaroy tumani	1	t	14
209	Taxiatosh shahri	1	t	1
210	Asaka shahri	1	t	2
211	Bandixon tumani	1	t	9
212	Ohangaron shahri	1	t	11
213	Yangiyo'l shahri	1	t	11
215	Toshkent tumani	1	t	11
\.


--
-- Data for Name: user_fueltype; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_fueltype (id, title, is_active, created_date) FROM stdin;
1	BENZIN	t	2021-10-03 18:30:17.465+05
2	GBA STG	t	2021-10-11 09:04:51.676+05
\.


--
-- Data for Name: user_notification; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_notification (id, created_at, updated_at, is_active, text, is_read, application_id, receiver_id, sender_id) FROM stdin;
\.


--
-- Data for Name: user_organization; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_organization (id, title, identification_number, address_of_garage, director, created_date, updated_date, removed_date, is_active, created_user_id, legal_address_district_id, legal_address_region_id) FROM stdin;
1	"BUXORO RAVON AVTOMAKTABI" MCHJ	305578956	Buxoro shahri, Suvchilar ko'chasi 24/7	Yoqubov Salohiddin	2021-10-16 15:00:16.257072+05	2021-10-16 15:00:16.257086+05	\N	t	9	52	3
\.


--
-- Data for Name: user_quarter; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_quarter (id, title, sort, is_active, district_id) FROM stdin;
1	Amir Temur nomli ovul fuqarolar yig`ini	1	t	15
2	Tosh Yop ovul fuqarolar yig`ini	1	t	15
3	O`rta qal`a ovul fuqarolar yig`ini	1	t	15
4	O`rta qal`a ovul fuqarolar yig`ini tarkibidagi "Arna bo`yi" MFY	1	t	15
5	O`rta qal`a ovul fuqarolar yig`ini tarkibidagi "Bog`" MFY	1	t	15
6	Qilichboy ovul fuqarolar yig`ini	1	t	15
7	Qilichboy ovul fuqarolar yig`ini tarkibidagi "Xizr eli" MFY	1	t	15
8	Qilichboy ovul fuqarolar yig`ini tarkibidagi "Besh ovul" MFY	1	t	15
9	Qilichboy ovul fuqarolar yig`ini tarkibidagi "Tosh qal`a" MFY	1	t	15
10	Qilichboy ovul fuqarolar yig`ini tarkibidagi "Yuqori qishloq" MFY	1	t	15
11	Xalimbeg ovul fuqarolar yig`ini	1	t	15
12	Xalimbeg ovul fuqarolar yig`ini tarkibidagi "AYoqchi" MFY	1	t	15
13	Do`rman ovul fuqarolar yig`ini	1	t	15
14	Do`rman ovul fuqarolar yig`ini tarkibidagi "Qoramon" MFY	1	t	15
15	Do`rman ovul fuqarolar yig`ini tarkibidagi "Bo`z solma" MFY	1	t	15
16	Bo`z Yop ovul fuqarolar yig`ini	1	t	15
17	Xitoy ovul fuqarolar yig`ini	1	t	15
18	Xitoy ovul fuqarolar yig`ini tarkibidagi "Tor Yop" MFY	1	t	15
19	Xitoy ovul fuqarolar yig`ini tarkibidagi "Namuna" MFY	1	t	15
20	Kuyuk ko`pir ovul fuqarolar yig`ini	1	t	15
21	Kuyuk ko`pir ovul fuqarolar yig`ini tarkibidagi "O`zbekiston" MFY	1	t	15
22	Kuyuk ko`pir ovul fuqarolar yig`ini tarkibidagi "Qizilcholi" MFY	1	t	15
23	Jumurtov shaharcha fuqarolar yig`ini	1	t	15
24	Z.M.Bobur nomli ovul fuqarolar yig`ini	1	t	15
25	Z.M.Bobur nomli ovul fuqarolar yig`ini tarkibidagi "Jumur ovul" MFY	1	t	15
26	Oq oltin ovul fuqarolar yig`ini	1	t	15
27	To`lqin ovul fuqarolar yig`ini	1	t	15
28	Choyko`l ovul fuqarolar yig`ini	1	t	15
29	Choyko`l ovul fuqarolar yig`ini tarkibidagi "Bosuv" MFY	1	t	15
30	Qipchoq ovul fuqarolar yig`ini	1	t	15
31	Qipchoq ovul fuqarolar yig`ini tarkibidagi "Daryo bo`yi" MFY	1	t	15
32	Qipchoq ovul fuqarolar yig`ini tarkibidagi "Uyshin" MFY	1	t	15
33	Qipchoq ovul fuqarolar yig`ini tarkibidagi "Besh tom" MFY	1	t	15
34	Qangli ovul fuqarolar yig`ini	1	t	15
35	Qangli ovul fuqarolar yig`ini tarkibidagi "Qum Yop" MFY	1	t	15
36	Nazarxon ovul fuqarolar yig`ini	1	t	15
37	A.Navoiy nomli MFY	1	t	15
38	Chordara MFY	1	t	15
39	Boy ovul MFY	1	t	15
40	Durunki MFY	1	t	15
41	Do`stlik MFY	1	t	15
42	Yangiobod MFY	1	t	15
43	Beruniy nomli MFY	1	t	15
44	Olmazor MFY	1	t	15
45	Gulzor MFY	1	t	15
46	Oybek nomli MFY	1	t	15
47	Bo`ston MFY	1	t	15
85	Kegeyli shaharchasi fuqarolar yig`ini	1	t	17
86	Kegeyli shaharchasi 1-sonli MFY	1	t	17
87	Kegeyli shaharchasi 2-sonli MFY	1	t	17
88	Kegeyli shaharchasi 3-sonli MFY	1	t	17
89	Kegeyli shaharchasi 4-sonli MFY	1	t	17
90	Xalaqabad shaharchasi fuqarolar yig`ini	1	t	17
91	Xalaqabad shaharchasi 1-sonli MFY	1	t	17
92	Xalaqabad shaharchasi 2-sonli MFY	1	t	17
93	Xalaqabad shaharchasi 3-sonli MFY	1	t	17
94	Xalaqabad shaharchasi 4-sonli MFY	1	t	17
95	Aktuba ovul fuqarolar yig`ini	1	t	17
96	Abat ovul fuqarolar yig`ini	1	t	17
97	Janabazar ovul fuqarolar yig`ini	1	t	17
98	Juzim bag ovul fuqarolar yig`ini	1	t	17
99	Jalpak jap ovul fuqarolar yig`ini	1	t	17
100	Kumshungil ovul fuqarolar yig`ini	1	t	17
101	Yerkindarya ovul fuqarolar yig`ini	1	t	17
102	Kazanketken SHFY	1	t	17
103	Kusxanatau ovul fuqarolar yig`ini	1	t	17
104	Aspantay ovul fuqarolar yig`ini	1	t	17
117	Qorao`zak shaharcha fuqarolai yig`ini	1	t	19
118	1-sonli MFY	1	t	19
119	2-sonli MFY	1	t	19
120	3-sonli MFY	1	t	19
121	4-sonli MFY	1	t	19
122	Berdax ovul fuqarolar yig`ini	1	t	19
123	Qorako`l ovul fuqarolar yig`ini	1	t	19
124	Qorabug`a ovul fuqarolar yig`ini	1	t	19
125	Qoybaq ovul fuqarolar yig`ini	1	t	19
126	Madeniyat ovul fuqarolar yig`ini	1	t	19
127	Alg`abas ovul fuqarolar yig`ini	1	t	19
128	Qorao`zak ovul fuqarolar yig`ini	1	t	19
129	Yesimo`zak ovul fuqarolar yig`ini	1	t	19
167	1 sonli MFY	1	t	21
168	2 sonli MFY	1	t	21
169	3 sonli MFY	1	t	21
170	4 sonli MFY	1	t	21
171	5 sonli MFY	1	t	21
172	Uchsay ovul fuqarolar yig`ini 	1	t	21
173	Tikuzyak ovul fuqarolar yig`ini 	1	t	21
174	Bozatoo` ovul fuqarolar yig`ini 	1	t	21
175	Madeli ovul fuqarolar yig`ini 	1	t	21
176	Hakim-ota ovul fuqarolar yig`ini 	1	t	21
177	Qazaxdarya ovul fuqarolar yig`ini 	1	t	21
187	Botanika bog`i MFY	1	t	23
188	Havo Yo`li MFY	1	t	23
189	Aydin Yo`l MFY	1	t	23
190	Chimboy choyxona MFY	1	t	23
191	Xalqlar do`stligi MFY	1	t	23
192	Shig`is MFY	1	t	23
193	Shoirlar ovuli MFY	1	t	23
194	Tinchlik MFY	1	t	23
195	Do`stlik MFY	1	t	23
196	Sarbinoz MFY	1	t	23
197	Tung`ish ko`nis MFY	1	t	23
198	Qurilishchi MFY	1	t	23
199	13-sonli Qoskol-2 MFY	1	t	23
200	14-sonli Almazar MFY	1	t	23
201	15-sonli Yeli abat MFY	1	t	23
202	16-sonli Darbent MFY	1	t	23
203	17-sonli Bayterek MFY	1	t	23
204	18-sonli Kebir ovul MFY	1	t	23
205	19-sonli Kattagar MFY	1	t	23
206	20-sonli Gone qala MFY	1	t	23
207	21-sonli Taslaq-1 MFY	1	t	23
208	22-sonli Taslaq-2 MFY	1	t	23
209	23-sonli Qum ovul MFY	1	t	23
210	24-sonli Jeke terek MFY	1	t	23
211	25-sonli Turan MFY	1	t	23
212	26-sonli Ko`k o`zak MFY	1	t	23
213	27-sonli Temir jol MFY	1	t	23
214	28-sonli Ornek MFY	1	t	23
215	29-sonli Nur MFY	1	t	23
216	30-sonli Qoskol-1 MFY	1	t	23
217	31-sonli Qoskol-3 MFY	1	t	23
218	32-sonli May ovul MFY	1	t	23
219	33-conli Qizil qum MFY	1	t	23
220	34-sonli Jayhun MFY	1	t	23
221	35-sonli Navro`z MFY	1	t	23
222	36-sonli Nao`qan bag` MFY	1	t	23
223	37-sonli Juvozchi MFY	1	t	23
224	38-conliBes pobe MFY	1	t	23
225	39-sonli Jiydeli boysin-1 MFY	1	t	23
226	40-sonli Jiydeli baysin-2 MFY	1	t	23
227	41-sonli Aq jag`is MFY	1	t	23
228	42-sonli Samanbay-1 MFY	1	t	23
229	43-sonli Samanbay-2 MFY	1	t	23
230	44-sonli Qoratov MFY	1	t	23
231	45-sonli Boz ovul MFY	1	t	23
232	46-sonli Qutli qonis MFY	1	t	23
233	47-sonli Qumbiz ovul MFY	1	t	23
234	48-sonli Aq otao` MFY	1	t	23
235	49-sonli Guzar MFY	1	t	23
236	50-sonli Beket MFY	1	t	23
237	51-sonli G`arezsizlik MFY	1	t	23
238	52-sonli Nao`bahar MFY	1	t	23
239	53-sonli AllaniYaz Qaharman MFY	1	t	23
240	54-sonli Xojan ovul MFY	1	t	23
241	55-sonli MFY	1	t	23
242	56-sonli MFY	1	t	23
243	57-sonli MFY	1	t	23
244	58-sonli MFY	1	t	23
262	Aviatsiya MFY	1	t	25
263	Guliston MFY	1	t	25
264	Yangiobod MFY	1	t	25
265	Beruniy MFY	1	t	25
266	Ibn-Sino MFY	1	t	25
267	To`rtko`l MFY	1	t	25
268	Turkiston MFY	1	t	25
269	Markazobod MFY	1	t	25
270	Toshkent MFY	1	t	25
271	G`alaba MFY	1	t	25
272	Mustaqillik MFY	1	t	25
273	Bog`Yop MFY	1	t	25
274	Navoiy MFY	1	t	25
275	O`zbekiston MFY	1	t	25
276	Istiqlol MFY	1	t	25
277	Xamza MFY	1	t	25
278	Gagarin MFY	1	t	25
279	Navro`z MFY	1	t	25
280	Do`stlik MFY	1	t	25
281	Yoshlik MFY	1	t	25
282	Oqqamish ovul fuqarolar yig`ini	1	t	25
283	Oqboshli ovul fuqarolar yig`ini	1	t	25
284	O`zbekiston ovul fuqarolar yig`ini	1	t	25
285	Sho`raxon ovul fuqarolar yig`ini	1	t	25
286	Ko`na-To`rtko`l ovul fuqarolar yig`ini	1	t	25
287	Paxtachi ovul fuqarolar yig`ini	1	t	25
288	Ullubog` ovul fuqarolar yig`ini	1	t	25
289	Tozabog`Yop ovul fuqarolar yig`ini	1	t	25
290	A.Durdiev nomli ovul fuqarolar yig`ini	1	t	25
291	Kelteminor ovul fuqarolar yig`ini	1	t	25
292	Yonboshqal`a ovul fuqarolar yig`ini	1	t	25
293	Ko`kcha ovul fuqarolar yig`ini	1	t	25
294	Paxtaobod ovul fuqarolar yig`ini	1	t	25
295	Qumbasqan ovul fuqarolar yig`ini	1	t	25
296	Atauba ovul fuqarolar yig`ini	1	t	25
297	O`zbekiston ovul fuqarolar yig`ini tasarrufidagi Do`stlik MFY	1	t	25
298	Ko`na-To`rtko`l ovul fuqarolar yig`ini tasarrufidagi Anxorli MFY	1	t	25
338	1-sonli MFY	1	t	27
339	2-sonli MFY	1	t	27
340	3-sonli MFY	1	t	27
341	4-sonli MFY	1	t	27
342	5-sonli MFY	1	t	27
343	6-sonli MFY	1	t	27
344	7-sonli MFY	1	t	27
345	8-sonli MFY	1	t	27
346	9-sonli MFY	1	t	27
347	10-sonli MFY	1	t	27
348	11-sonli MFY	1	t	27
349	Tazg`ara ovul fuqarolar yig`ini	1	t	27
350	Tag`jap ovul fuqarolar yig`ini	1	t	27
351	Tazajol ovul fukarolar yig`ini	1	t	27
352	Kenes ovul fuqarolar yig`ini	1	t	27
353	Qosterek ovul fuqarolar yig`ini	1	t	27
354	Mayjap ovul fuqarolar yig`ini	1	t	27
355	Baxitli ovul fuqarolar yig`ini	1	t	27
356	Qamis-arik ovul fuqarolar yig`ini	1	t	27
357	Qizil-uzak ovul fuqarolar yig`ini	1	t	27
358	Pashenttao` ovul fuqarolar yig`ini	1	t	27
359	Kok-su ovul fuqarolar yig`ini	1	t	27
372	Do`stlik ovul fuqarolar yig`ini	1	t	29
373	Amirobod ovul fuqarolar yig`ini	1	t	29
374	Toza-bog` ovul fuqarolar yig`ini	1	t	29
375	Guldursun ovul fuqarolar yig`ini	1	t	29
376	Qirqqiz ovul fuqarolar yig`ini	1	t	29
377	QiliChinoq ovul fuqarolar yig`ini	1	t	29
378	Saribiy ovul fuqarolar yig`ini	1	t	29
379	Guliston ovul fuqarolar yig`ini	1	t	29
380	Navoiy ovul fuqarolar yig`ini	1	t	29
381	Ellikqal`a ovul fuqarolar yig`ini	1	t	29
382	AqChako`l ovul fuqarolar yig`ini	1	t	29
383	Sharq-Yulduzi ovul fuqarolar yig`ini	1	t	29
384	Qizil-Qum ovul fuqarolar yig`ini	1	t	29
385	Chuqurqoq MFY	1	t	29
386	Oq oltin MFY	1	t	29
387	Ixlos MFY	1	t	29
388	Koinot MFY	1	t	29
389	Dumanqal`a MFY	1	t	29
390	Paxtachi MFY	1	t	29
391	Cho`pon MFY	1	t	29
392	Usmon-Yusupov MFY	1	t	29
393	Chayka MFY	1	t	29
394	Tuproqal`a MFY	1	t	29
395	Bo`ston MFY	1	t	29
396	Ibn-Sino MFY	1	t	29
397	Abay MFY	1	t	29
398	Toshkent MFY	1	t	29
399	A.Navoiy MFY	1	t	29
400	Qavatqal`a MFY	1	t	29
401	SaxtiYon shaharcha fuqarolar yig`ini	1	t	29
402	1 son MFY	1	t	30
403	2 son MFY	1	t	30
404	3 son MFY	1	t	30
405	4 son MFY	1	t	30
406	5 son MFY	1	t	30
407	6 son MFY	1	t	30
408	7 son MFY	1	t	30
409	8 son MFY	1	t	30
410	9 son MFY	1	t	30
411	10 son MFY	1	t	30
412	A.Bakirov MFY	1	t	30
413	Al-Buxoriy MFY	1	t	30
414	Andijon MFY	1	t	30
415	Birlashgan MFY	1	t	30
416	Birlik MFY	1	t	30
417	Bobosaddin MFY	1	t	30
418	Bobur MFY	1	t	30
419	Bogishamol MFY	1	t	30
420	Buston MFY	1	t	30
421	Shurbulok MFY	1	t	30
422	Gayrat MFY	1	t	30
423	Guliston MFY	1	t	30
424	Gumbaz MFY	1	t	30
425	Dalvarzin MFY	1	t	30
426	Dexkonobod MFY	1	t	30
427	Dustlik MFY	1	t	30
428	Yorboshi MFY	1	t	30
429	Jumabozor MFY	1	t	30
430	Islomobod MFY	1	t	30
431	Ittifok MFY	1	t	30
432	Ishchilar MFY	1	t	30
433	Kayragochtagi MFY	1	t	30
434	Kalandarxona MFY	1	t	30
435	Kengash MFY	1	t	30
436	Madaniyat MFY	1	t	30
437	Maydonbozor MFY	1	t	30
438	Maorif MFY	1	t	30
439	Ma`rifat MFY	1	t	30
440	Mexnat MFY	1	t	30
441	Mirpustin MFY	1	t	30
442	Mustakillik MFY	1	t	30
443	M. Aliboy MFY	1	t	30
444	Navruz MFY	1	t	30
445	Namuna MFY	1	t	30
446	Obod MFY	1	t	30
447	Ozodlik MFY	1	t	30
448	Oxunboboev MFY	1	t	30
449	Paxtakor MFY	1	t	30
450	Pistamozor MFY	1	t	30
451	Sanoat MFY	1	t	30
452	Sa`diy MFY	1	t	30
453	Soy MFY	1	t	30
454	Sulton Jura MFY	1	t	30
455	Taxtakuprik MFY	1	t	30
456	Tojik MFY	1	t	30
457	Tukkizarik MFY	1	t	30
458	Uzbekiston MFY	1	t	30
459	Uzgarish MFY	1	t	30
460	Uygurobod MFY	1	t	30
461	Farobiy MFY	1	t	30
462	X.Kodirov MFY	1	t	30
463	Xabibiy MFY	1	t	30
464	Xakikat MFY	1	t	30
465	Xursandlik MFY	1	t	30
466	Xutanarik MFY	1	t	30
467	Cho`lpon 100 yilligi MFY	1	t	30
468	Shifokor MFY	1	t	30
469	Shodlik MFY	1	t	30
470	Erkin MFY	1	t	30
471	Yangi Turmush MFY	1	t	30
472	Yangi Xayot MFY	1	t	30
473	Yaxshi MFY	1	t	30
474	X. Axmedov MFY	1	t	30
475	Buyuk Turon MFY	1	t	30
476	Oyjamol MFY	1	t	31
477	Daryobo`yi MFY	1	t	31
478	Sanoat MFY	1	t	31
479	BFK-Baxt MFY	1	t	31
480	Kuyganyor SHFY	1	t	31
481	Istiqlol MFY	1	t	31
482	No`xatak MFY	1	t	31
483	Qo`shariq MFY	1	t	31
484	M.Soliev MFY	1	t	31
485	Tolmozor MFY	1	t	31
486	Nayman MFY	1	t	31
487	Poloson MFY	1	t	31
488	Mirobod MFY	1	t	31
489	Xo`ja tojik MFY	1	t	31
490	Oqyor QFY	1	t	31
491	Orol MFY	1	t	31
492	Guliston MFY	1	t	31
493	Maorif MFY	1	t	31
494	Orol QFY	1	t	31
495	Pistamozor MFY	1	t	31
496	Bo`riboy MFY	1	t	31
497	Gumbaz MFY	1	t	31
498	Zangibobo MFY	1	t	31
499	Qurama MFY	1	t	31
500	Og`ullik MFY	1	t	31
501	Darxon MFY	1	t	31
502	Chem MFY	1	t	31
503	Madraximxoji MFY	1	t	31
504	Abduraxmonmingboshi MFY	1	t	31
505	Qum ko`chasi MFY	1	t	31
506	Qoratut MFY	1	t	31
507	Xokan QFY	1	t	31
508	Ayrilish MFY	1	t	31
509	Damariq MFY	1	t	31
510	Beshbo`ynoq MFY	1	t	31
511	Ekin- tikin MFY	1	t	31
512	Guliston MFY	1	t	31
513	Chorbog` MFY	1	t	31
514	Yorboshi QFY	1	t	31
515	Mart MFY	1	t	31
516	Mustaqillik MFY	1	t	31
517	Navro`z MFY	1	t	31
518	Rovvot MFY	1	t	31
519	Istiqlol MFY	1	t	31
520	Maorif MFY	1	t	31
521	Dexqon MFY	1	t	31
522	Namuna MFY	1	t	31
523	To`pabjuvoz MFY	1	t	31
524	Bo`taqora QFY	1	t	31
525	Do`stlik MFY	1	t	31
526	Toshloq MFY	1	t	31
527	Terak tagi MFY	1	t	31
528	J.Saidov MFY	1	t	31
529	Jaxarmasjid MFY	1	t	31
530	Mingo`rik MFY	1	t	31
531	Rovvot MFY	1	t	31
532	Qo`nji QFY	1	t	31
533	O`rikzor MFY	1	t	31
534	Islomobod MFY	1	t	31
535	Yangi to`lqin MFY	1	t	31
536	Jevachi MFY	1	t	31
537	Guzar MFY	1	t	31
538	Yu.Mamajonov MFY	1	t	31
539	Teraktagi MFY	1	t	31
540	Afg`on MFY	1	t	31
541	Joxonobod MFY	1	t	31
542	Xortum QFY	1	t	31
543	Yangiobod MFY	1	t	31
544	Gulobod MFY	1	t	31
545	Qo`qonlik MFY	1	t	31
546	Bobog`ozi MFY	1	t	31
547	Aylanpa MFY	1	t	31
548	Do`dir MFY	1	t	31
549	Cho`ngbog`iCh MFY	1	t	31
550	Chavkandaryo MFY	1	t	31
551	Bekobod MFY	1	t	31
552	Qoraqolpoq MFY	1	t	31
553	Nayman QFY	1	t	31
554	Kengash MFY	1	t	31
555	Saddatagi MFY	1	t	31
556	Guliston MFY	1	t	31
557	Xaqiqat MFY	1	t	31
558	Otchopar MFY	1	t	31
559	Do`ng qishloq MFY	1	t	31
560	Kattaguzar MFY	1	t	31
561	Sharq Yulduzi MFY	1	t	31
562	Chilon MFY	1	t	31
563	Xrabek QFY	1	t	31
564	Zarbdor KFY	1	t	32
565	Saidobod MFY	1	t	32
566	Ne`matobod MFY	1	t	32
567	Ergashobod MFY	1	t	32
568	Dung MFY	1	t	32
569	Yangisor MFY	1	t	32
570	Fayziobod MFY	1	t	32
571	Ilgor KFY	1	t	32
572	Kashkar MFY	1	t	32
573	Olakanot MFY	1	t	32
574	Zankan MFY	1	t	32
575	Axtachi MFY	1	t	32
576	Devatagi MFY	1	t	32
577	Korakiy MFY	1	t	32
578	Otish MFY	1	t	32
579	Obod MFY	1	t	32
580	Kadim KFY	1	t	32
581	Tajriba MFY	1	t	32
582	Labgardon MFY	1	t	32
583	Kovok tupi MFY	1	t	32
584	Dasturxonchi MFY	1	t	32
585	Uchtosh MFY	1	t	32
586	Kadim MFY	1	t	32
587	Kipchok MFY	1	t	32
588	Shurkishlok MFY	1	t	32
589	Mustaxkam KFY	1	t	32
590	Okbuyra MFY	1	t	32
591	Namuna Buston MFY	1	t	32
592	Elas kipchak MFY	1	t	32
593	Xonaka MFY	1	t	32
594	Mirzaobod MFY	1	t	32
595	Katta tojik MFY	1	t	32
596	Uzbekiston KFY	1	t	32
597	Toshtepa MFY	1	t	32
598	Durman MFY	1	t	32
599	Argin MFY	1	t	32
600	Tuvadak MFY	1	t	32
601	T.Aliev MFY	1	t	32
602	Navkan MFY	1	t	32
603	Kujgan KFY	1	t	32
604	Navoiy MFY	1	t	32
605	Chuntak MFY	1	t	32
606	Chek MFY	1	t	32
607	Kujgan MFY	1	t	32
608	Ozod MFY	1	t	32
609	Markayuz MFY	1	t	32
610	Ungut MFY	1	t	32
611	Kayragoch MFY	1	t	32
612	Kungirot MFY	1	t	32
613	Buzarik MFY	1	t	32
614	Yukori buz MFY	1	t	32
615	Koratepa KFY	1	t	32
616	Kurama MFY	1	t	32
617	Gancha yuz	1	t	32
618	Koratepa MFY	1	t	32
619	Bexabar MFY	1	t	32
620	Katagon MFY	1	t	32
621	Bozorboshi MFY	1	t	32
622	Niyozbotir KFY	1	t	32
623	Niyozbotir MFY	1	t	32
624	Baxrin MFY	1	t	32
625	YangiObod MFY	1	t	32
626	Mexnatobod MFY	1	t	32
627	Asaka MFY	1	t	32
628	Ittifoq MFY	1	t	32
629	Amir Temur MFY	1	t	32
630	Baynalminal MFY	1	t	32
631	Bobur MFY	1	t	32
632	Birlik MFY	1	t	32
633	Do`stlik MFY	1	t	32
634	Xamdo`stlik MFY	1	t	32
635	Nurafshon MFY	1	t	32
636	Qadiryat MFY	1	t	32
637	Istiqlol MFY	1	t	32
638	Navoiy MFY	1	t	32
639	Muqumiy MFY	1	t	32
640	T.Matyoqubov MFY	1	t	32
641	Shodlik MFY	1	t	32
642	Ibn-Sino MFY	1	t	32
643	O`zbekiston MFY	1	t	32
644	Ulug`bek MFY	1	t	32
645	Siza QFY	1	t	33
646	Oq-tepa MFY	1	t	33
647	Siza MFY	1	t	33
648	Yangi qishloq MFY	1	t	33
649	Mallachek MFY	1	t	33
650	Nasriddinobod MFY	1	t	33
651	Eskihaqulobod QFY	1	t	33
652	Yettiqashqa MFY	1	t	33
653	O`lmas MFY	1	t	33
654	Eskihaqulobod MFY	1	t	33
655	Dog`iston MFY	1	t	33
656	Yangi hayot MFY	1	t	33
657	Mustaqillik MFY	1	t	33
658	Tulkiobod MFY	1	t	33
659	Tovuldi MFY	1	t	33
660	Yangiqishloq MFY	1	t	33
661	Xo`jaobod QFY	1	t	33
662	Madaminov MFY	1	t	33
663	Guzar MFY	1	t	33
664	Qahramon MFY	1	t	33
665	Buloqboshi MFY	1	t	33
666	Qo`rg`oncha MFY	1	t	33
667	Fayzobod MFY	1	t	33
668	A`lam MFY	1	t	33
669	Oxunboboev QFY	1	t	33
670	Omonariq MFY	1	t	33
671	Chinobod MFY	1	t	33
672	Sho`r MFY	1	t	33
673	Tumor MFY	1	t	33
674	Botir MFY	1	t	33
675	Baliqchi MFY	1	t	33
676	Zaxkash MFY	1	t	33
677	To`da MFY	1	t	33
678	Qiyali MFY	1	t	33
679	Qumtepa MFY	1	t	33
680	Sarnavul MFY	1	t	33
681	Qo`rg`oncha MFY	1	t	33
682	Olimbek QFY	1	t	33
683	Olimbek MFY	1	t	33
684	Do`stlik MFY	1	t	33
685	Fayzaobod MFY	1	t	33
686	Polvonko`l MFY	1	t	33
687	Do`ngsaroy MFY	1	t	33
688	Eshonchek MFY	1	t	33
689	Zulfiqor MFY	1	t	33
690	Xalfachek MFY	1	t	33
691	O`rmonbek QFY	1	t	33
692	O`rmonbek MFY	1	t	33
693	Bo`z MFY	1	t	33
694	Xolmurod MFY	1	t	33
695	Buston QFY	1	t	33
696	Alchazor MFY	1	t	33
697	Bo`ston MFY	1	t	33
698	Jartepa MFY	1	t	33
699	Eshonqishloq MFY	1	t	33
700	Aralxon MFY	1	t	33
701	Guliston QFY	1	t	33
702	Ko`lbo`yi MFY	1	t	33
703	Guliston MFY	1	t	33
704	Oqqo`rg`on MFY	1	t	33
705	Sheralichek MFY	1	t	33
706	Mirzaboshichek MFY	1	t	33
707	Balikchi QFY	1	t	33
708	Qo`rg`oncha MFY	1	t	33
709	O`rtaqo`rg`on MFY	1	t	33
710	Go`rovon MFY	1	t	33
711	Yakkatol MFY	1	t	33
712	Baliqchi MFY	1	t	33
713	Kattabuloq MFY	1	t	33
714	Markaz MFY	1	t	33
715	Islomobod MFY	1	t	33
716	Oqqo`rg`on MFY	1	t	33
717	Ko`l MFY	1	t	33
718	Bulokboshi QFY	1	t	34
719	Toshkechik MFY	1	t	34
720	Guliston MFY	1	t	34
721	Ittifok MFY	1	t	34
722	M.Ismoiliy MFY	1	t	34
723	T.Raximov MFY	1	t	34
724	Kumguzar MFY	1	t	34
725	Chakar MFY	1	t	34
726	Bulokboshi MFY	1	t	34
727	Mayarik QFY	1	t	34
728	Andijon MFY	1	t	34
729	Boymaxalla MFY	1	t	34
730	Uchkucha MFY	1	t	34
731	Eshonxujaev MFY	1	t	34
732	Dulana MFY	1	t	34
733	Madraximova MFY	1	t	34
734	Mayarik MFY	1	t	34
735	Nayman QFY	1	t	34
736	Nayman MFY	1	t	34
737	Shark yulduzi MFY	1	t	34
738	Baynalminal MFY	1	t	34
739	Oxunboboev MFY	1	t	34
740	Kashkar MFY	1	t	34
741	Sarvontepa MFY	1	t	34
742	Shirmonbulok QFY	1	t	34
743	Shirmonbulok MFY	1	t	34
744	Kakir MFY	1	t	34
745	Navoiy MFY	1	t	34
746	Tinchlik MFY	1	t	34
747	Zargaldok MFY	1	t	34
748	Uchtepa MFY	1	t	34
749	Kulla QFY	1	t	34
750	Raish MFY	1	t	34
751	Kiziluy MFY	1	t	34
752	Kuprikboshi MFY	1	t	34
753	Bozorboshi MFY	1	t	34
754	S.Otajonov MFY	1	t	34
755	Yangi arik MFY	1	t	34
756	Andijon QFY	1	t	34
757	Neftchilar MFY	1	t	34
758	Ittifok MFY	1	t	34
759	Sanoat MFY	1	t	34
760	Balandchek MFY	1	t	34
761	Oxunboboev MFY	1	t	35
762	A.Yo`lchiev MFY	1	t	35
763	Nasirdinbek MFY	1	t	35
764	Guzar MFY	1	t	35
765	Bo`ston MFY	1	t	35
766	O`rda to`p MFY	1	t	35
767	Do`stlik MFY	1	t	35
768	Axmadobod MFY	1	t	35
769	Bo`z SHFY	1	t	35
770	Dexqonobod MFY	1	t	35
771	Ma`rufobod MFY	1	t	35
772	Mexnatobod MFY	1	t	35
773	Xovos MFY	1	t	35
774	Guliston MFY	1	t	35
775	Xalqobod MFY	1	t	35
776	Xovos QFY	1	t	35
777	Solimaxsum MFY	1	t	35
778	Mustaqillik 15 yilligi MFY	1	t	35
779	Xoldevonbek MFY	1	t	35
780	Yangi qishloq MFY	1	t	35
781	Yangi obod MFY	1	t	35
782	Holdevonbek QFY	1	t	35
783	M.Jalolov MFY	1	t	35
784	Navro`z MFY	1	t	35
785	Yangi hayot MFY	1	t	35
786	Darmonqulota MFY	1	t	35
787	Yangi turmush MFY	1	t	35
788	Yakka tol MFY	1	t	35
789	M.Jalolov QFY	1	t	35
790	Navoiy MFY	1	t	36
791	Yangichek MFY	1	t	36
792	Namuna MFY	1	t	36
793	Urokchi-tepa MFY	1	t	36
794	Bozarboshi MFY	1	t	36
795	Kadaksin MFY	1	t	36
796	Guliston MFY	1	t	36
797	Sufikishlok MFY	1	t	36
798	Tuyalas MFY	1	t	36
799	Boycheki MFY	1	t	36
800	J.Olamushuk SHFY	1	t	36
801	Birlashgan MFY	1	t	36
802	Navoiy MFY	1	t	36
803	Ittifok MFY	1	t	36
804	Yorqishloq KFY	1	t	36
805	Galaba MFY	1	t	36
806	Yorkishlok MFY	1	t	36
807	Kutlug MFY	1	t	36
808	Kashkar MFY	1	t	36
809	Toshxovuz MFY	1	t	36
810	Yangikurpa MFY	1	t	36
811	Beshtol KFY	1	t	36
812	Kushtepa MFY	1	t	36
813	Guliston MFY	1	t	36
814	Beshtol MFY	1	t	36
815	Xamza MFY	1	t	36
816	Jalaquduq KFY	1	t	36
817	Jalakuduk MFY	1	t	36
818	Dungkishlok MFY	1	t	36
819	Buston MFY	1	t	36
820	Yangisor MFY	1	t	36
821	Urgu MFY	1	t	36
822	Koragul MFY	1	t	36
823	Guliston KFY	1	t	36
824	Gozichek MFY	1	t	36
825	Beshkaram MFY	1	t	36
826	Sharxonchek MFY	1	t	36
827	Kesak MFY	1	t	36
828	Xasankovok MFY	1	t	36
829	Abdullabiy KFY	1	t	36
830	Kalambek MFY	1	t	36
831	Oxunboboev MFY	1	t	36
832	Kutarma MFY	1	t	36
833	Abdullabiy MFY	1	t	36
834	Dustlik MFY	1	t	36
835	Ibrat MFY	1	t	36
836	Oyim KFY	1	t	36
837	Kukalam MFY	1	t	36
838	Uzbekiston MFY	1	t	36
839	Toshlok MFY	1	t	36
840	Buzrukxontura MFY	1	t	36
841	Delvarzin MFY	1	t	36
842	Olmazor MFY	1	t	36
843	A.Raxmonov MFY	1	t	36
844	Ittifok MFY	1	t	36
845	Teshiktosh KFY	1	t	36
846	Gayrat MFY	1	t	36
847	Xakikat MFY	1	t	36
848	Uzunkucha MFY	1	t	36
849	Bolgariya MFY	1	t	36
850	Dexkonobod MFY	1	t	36
851	Kurtki MFY	1	t	36
852	Qatortol KFY	1	t	36
853	Korayontok MFY	1	t	36
854	Kattapolvon MFY	1	t	36
855	Akcha MFY	1	t	36
856	Kapa MFY	1	t	36
857	Xamzaobod MFY	1	t	36
858	Kilichmozar MFY	1	t	36
859	Turacheki MFY	1	t	36
860	Dostonobod MFY	1	t	36
861	Madaniyat MFY	1	t	36
862	O.Masaidov MFY	1	t	37
863	Oybek MFY	1	t	37
864	Qashqarliq MFY	1	t	37
865	T.Mamajonov MFY	1	t	37
866	Oxunboboev MFY	1	t	37
867	Amir Temur MFY	1	t	37
868	M.Usmonov MFY	1	t	37
869	A.Navoiy MFY	1	t	37
870	U.Mansurov MFY	1	t	37
871	M.To`xtaboev MFY	1	t	37
872	Obod MFY	1	t	37
873	Yuqori-Jonobod MFY	1	t	37
874	Yangi obod MFY	1	t	37
875	Zarbdor MFY	1	t	37
876	Daminboychek MFY	1	t	37
877	Oq-oltin MFY	1	t	37
878	Qo`shko`prik MFY	1	t	37
879	Jonobod MFY	1	t	37
880	Birlashgan MFY	1	t	37
881	O`rtoqlar KFY	1	t	37
882	Navro`zobod MFY	1	t	37
883	Birlashgan MFY	1	t	37
884	A.Jomiy MFY	1	t	37
885	Tuyachi MFY	1	t	37
886	Yangizamon MFY	1	t	37
887	Bo`ston MFY	1	t	37
888	Do`stlik MFY	1	t	37
889	Yangizamon KFY	1	t	37
890	Guliston MFY	1	t	37
891	Qo`g`ay MFY	1	t	37
892	Beshterak MFY	1	t	37
893	Urganji MFY	1	t	37
894	Kuygan-yor MFY	1	t	37
895	O`rta-qishloq MFY	1	t	37
896	Erkin KFY	1	t	37
897	Gurkirov-1 MFY	1	t	37
898	Gurkirov-2 MFY	1	t	37
899	Toshkechik MFY	1	t	37
900	Uzun-ko`chasi MFY	1	t	37
901	Qum-ko`chasi MFY	1	t	37
902	Beshmirza MFY	1	t	37
903	Qora-yantoq MFY	1	t	37
904	Yukori-Chuvama MFY	1	t	37
905	Cho`rtanliq MFY	1	t	37
906	Izboskan KFY	1	t	37
907	Yuqori hosil MFY	1	t	37
908	Moygir MFY	1	t	37
909	Daryo-bo`yi MFY	1	t	37
910	Sorboshi MFY	1	t	37
911	Moygir KFY	1	t	37
912	Botirobod MFY	1	t	37
913	To`rtko`l MFY	1	t	37
914	T.Shokirov MFY	1	t	37
915	A.Ikromov MFY	1	t	37
916	Guzar MFY	1	t	37
917	Shermatobod KFY	1	t	37
918	To`raobod MFY	1	t	37
919	Yakkatut MFY	1	t	37
920	Y.Po`latov MFY	1	t	37
921	Yakkatut KFY	1	t	37
922	Boy mahalla MFY	1	t	37
923	Urganji MFY	1	t	37
924	Elatan MFY	1	t	37
925	Yangi-qishloq MFY	1	t	37
926	Yangikishlok KFY	1	t	37
927	Chek MFY	1	t	37
928	Rovot MFY	1	t	37
929	Navjur MFY	1	t	37
930	Xaqqulobod MFY	1	t	37
931	Yuqori MFY	1	t	37
932	Namyman QFY	1	t	37
933	A.Navoiy MFY	1	t	38
934	A.Temur MFY	1	t	38
935	A.Yassaviy MFY	1	t	38
936	B.Ahmedov MFY	1	t	38
937	Bo`rilik MFY	1	t	38
938	Z.M.Bobur MFY	1	t	38
939	Paxtachi MFY	1	t	38
940	M.Ulug`bek MFY	1	t	38
941	Mustaqillik MFY	1	t	38
942	Mustaqillikning 15 y. MFY	1	t	38
943	Uch tegirmon MFY	1	t	38
944	A.Jomiy MFY	1	t	39
945	A.Navoiy MFY	1	t	39
946	Guliston MFY	1	t	39
947	Ibn Sino MFY	1	t	39
948	Qo`rg`ontepa MFY	1	t	39
949	Mustaqillik MFY	1	t	39
950	Navro`z MFY	1	t	39
951	S.Raximov MFY	1	t	39
952	Savay MFY	1	t	39
953	Toshqo`rg`on MFY	1	t	39
954	U.YusupovMFY	1	t	39
955	Xon ko`chasi MFY	1	t	39
956	Shaxrixonsoy MFY	1	t	39
957	EshonqishloqMFY	1	t	39
958	Yangi hayotMFY	1	t	39
959	Qo`rg`ontepa QFY	1	t	39
960	Bobur MFY	1	t	39
961	Bozorboshi MFY	1	t	39
962	G`ayrat MFY	1	t	39
963	Dexqonobod MFY	1	t	39
964	Ijtimoyat MFY	1	t	39
965	Qo`tkar MFY	1	t	39
966	Qo`shtepa MFY	1	t	39
967	Ma`murobod MFY	1	t	39
968	T.Sodiqov MFY	1	t	39
969	Toshloq MFY	1	t	39
970	Uchqun MFY	1	t	39
971	Ho`jatepa MFY	1	t	39
972	Sultonobod QFY	1	t	39
973	Ittifoq MFY	1	t	39
974	Mirabdullaev MFY	1	t	39
975	Nishonbekov MFY	1	t	39
976	Toshmatov MFY	1	t	39
977	U.Nosirov MFY	1	t	39
978	Furkat MFY	1	t	39
979	Xamza MFY	1	t	39
980	Savay QFY	1	t	39
981	Birlashgan MFY	1	t	39
982	G`alaba MFY	1	t	39
983	Mustaqillik MFY	1	t	39
984	Obodon MFY	1	t	39
985	R.Boboxonov MFY	1	t	39
986	Savay MFY	1	t	39
987	Chorvador MFY	1	t	39
988	Yangi-bo`ston MFY	1	t	39
989	Chimyon QFY	1	t	39
990	Beshkaltak MFY	1	t	39
991	Dehqonchek MFY	1	t	39
992	Do`stlik MFY	1	t	39
993	Navoiy MFY	1	t	39
994	Namuna MFY	1	t	39
995	Norbo`ta MFY	1	t	39
996	O.Yo`lboev MFY	1	t	39
997	Ozod MFY	1	t	39
998	Oltinsoy MFY	1	t	39
999	SutkonMFY	1	t	39
1000	Chimyon MFY	1	t	39
1001	Eshonobod MFY	1	t	39
1002	Dardoq QFY	1	t	39
1003	Dardoq MFY	1	t	39
1004	DardoqtepaMFY	1	t	39
1005	Yortibosh MFY	1	t	39
1006	Qizilto`qay MFY	1	t	39
1007	Qirlik MFY	1	t	39
1008	Navoiy MFY	1	t	39
1009	Nodira MFY	1	t	39
1010	Oxunboboev MFY	1	t	39
1011	Raxmonov MFY	1	t	39
1012	Uzbekiston MFY	1	t	40
1013	Navruz MFY	1	t	40
1014	Turkiston MFY	1	t	40
1015	Ming-tepa MFY	1	t	40
1016	Yangi maxalla MFY	1	t	40
1017	Guliston MFY	1	t	40
1018	Marhamat QFY	1	t	40
1019	T. Mirzaev MFY	1	t	40
1020	G. Gulom MFY	1	t	40
1021	X. Vosiliy MFY	1	t	40
1022	Oybek MFY	1	t	40
1023	Nayman MFY	1	t	40
1024	Yangi xayot MFY	1	t	40
1025	Qoraqo`rg`on QFY	1	t	40
1026	T. Yusupov MFY	1	t	40
1027	Korakurgon MFY	1	t	40
1028	Bozorboshi MFY	1	t	40
1029	Yulamatol MFY	1	t	40
1030	Buriboshi MFY	1	t	40
1031	Xujaarik MFY	1	t	40
1032	Tosh yuli MFY	1	t	40
1033	Gar-gar MFY	1	t	40
1034	Jiydamozor MFY	1	t	40
1035	Ok bosh MFY	1	t	40
1036	Ko`tarma QFY	1	t	40
1037	Kutarma MFY	1	t	40
1038	Ukchi MFY	1	t	40
1039	Dustlik MFY	1	t	40
1040	Uvaysiy MFY	1	t	40
1041	Dorboz MFY	1	t	40
1042	Qorabag`ish QFY	1	t	40
1043	Korabogish MFY	1	t	40
1044	Roxat MFY	1	t	40
1045	Chilon MFY	1	t	40
1046	Yangi kishlok MFY	1	t	40
1047	Alitepa MFY	1	t	40
1048	Toshlok MFY	1	t	40
1049	Kurgoncha MFY	1	t	40
1050	Boboxorason MFY	1	t	40
1051	Shukurmergan QFY	1	t	40
1052	Shomat MFY	1	t	40
1053	Xakka MFY	1	t	40
1054	Yuvvosh MFY	1	t	40
1055	Shurkishlok MFY	1	t	40
1056	Shurkakir MFY	1	t	40
1057	Tulga MFY	1	t	40
1058	Shukurmergan MFY	1	t	40
1059	Yukori rovvot MFY	1	t	40
1060	Yangi rovvot MFY	1	t	40
1061	Xasanmergan MFY	1	t	40
1062	Polvontosh MFY	1	t	40
1063	Polvontosh shaxarcha	1	t	40
1064	S. Raximov MFY	1	t	40
1065	Markaziy MFY	1	t	40
1066	Oltinko`l QFY	1	t	41
1067	Bo`ston MFY	1	t	41
1068	Saroy-1 MFY	1	t	41
1069	Saroy-2 MFY	1	t	41
1070	Ittifoq MFY	1	t	41
1071	Oq tepa MFY	1	t	41
1072	Katta oqtepa MFY	1	t	41
1073	Qoraqolpoq MFY	1	t	41
1074	Mamayusufchek MFY	1	t	41
1075	Markaz MFY	1	t	41
1076	Namuna MFY	1	t	41
1077	Oftabachek MFY	1	t	41
1078	Oxunboboev QFY	1	t	41
1079	Qayirma MFY	1	t	41
1080	Madiyorchek MFY	1	t	41
1081	Temirxo`ja MFY	1	t	41
1082	Xondibog`i MFY	1	t	41
1083	Jalabek QFY	1	t	41
1084	Dalvarzin MFY	1	t	41
1085	Jalabek MFY	1	t	41
1086	Qo`shtepa MFY	1	t	41
1087	Mexnat MFY	1	t	41
1088	Uyg`ur MFY	1	t	41
1089	Yangi chek MFY	1	t	41
1090	Kumakay QFY	1	t	41
1091	Ayshaxonum MFY	1	t	41
1092	Kumakay MFY	1	t	41
1093	Sadda MFY	1	t	41
1094	Uyshin MFY	1	t	41
1095	Chek MFY	1	t	41
1096	Cho`ntak MFY	1	t	41
1097	Qo`shtepasaroy KFY	1	t	41
1098	Andijon MFY	1	t	41
1099	Qo`shko`prik MFY	1	t	41
1100	Saroy MFY	1	t	41
1101	Safarobod MFY	1	t	41
1102	Toptiq MFY	1	t	41
1103	O`rta MFY	1	t	41
1104	Sharq yulduzi MFY	1	t	41
1105	Oqtumor MFY	1	t	41
1106	Maslaxat QFY	1	t	41
1107	Ijtimoyat MFY	1	t	41
1108	Ittifoq MFY	1	t	41
1109	Madaniy-mexnat MFY1	1	t	41
1110	Madaniy-mexnat MFY2	1	t	41
1111	Maqsad MFY	1	t	41
1112	Xasan-Xusan MFY	1	t	41
1113	Xuja MFY	1	t	41
1114	Erkin MFY	1	t	41
1115	Oraziy QFY	1	t	41
1116	Ganjirovon MFY	1	t	41
1117	Jiyanbek MFY	1	t	41
1118	Qipchoq MFY	1	t	41
1119	Ko`tarmachek MFY	1	t	41
1120	Uzun kucha MFY	1	t	41
1121	Suvyulduz QFY	1	t	41
1122	Ayronchi MFY	1	t	41
1123	Gulbog`-Ittifoq MFY	1	t	41
1124	Mirobod MFY	1	t	41
1125	ORS MFY	1	t	41
1126	Suvyulduz MFY	1	t	41
1127	Chaqqon-1 MFY	1	t	41
1128	Chaqqon-2 MFY	1	t	41
1129	Qashqar MFY	1	t	41
1130	Navro`z MFY	1	t	42
1131	Yuqori MFY	1	t	42
1132	Shomat MFY	1	t	42
1133	Z.Xabibiy MFY	1	t	42
1134	Qo`qonqishloq MFY	1	t	42
1135	Nodirabegim MFY	1	t	42
1136	Qashqar MFY	1	t	42
1137	Muazzinboy MFY	1	t	42
1138	Qorashox MFY	1	t	42
1139	Mustaqillik MFY	1	t	42
1140	Bobur MFY	1	t	42
1141	Ittifoq QFY	1	t	42
1142	Sangraobod MFY	1	t	42
1143	Qo`yi Sangraobod MFY	1	t	42
1144	To`pajuvoz MFY	1	t	42
1145	Tojikqishloq MFY	1	t	42
1146	Xayraobod-1 MFY	1	t	42
1147	Xayraobod-2 MFY	1	t	42
1148	Guliston-Pastqishloq MFY	1	t	42
1149	Shuvoqzor-Boykechik MFY	1	t	42
1150	Uyg`ur QFY	1	t	42
1151	Paynob MFY	1	t	42
1152	Omonjo`ra-1 MFY	1	t	42
1153	Omonjo`ra-2 MFY	1	t	42
1154	Do`ngkishlok MFY	1	t	42
1155	Soxil MFY	1	t	42
1156	Guzar MFY	1	t	42
1157	To`qqizbog` MFY	1	t	42
1158	Shovruq MFY	1	t	42
1159	Pushmon MFY	1	t	42
1160	Ittifoq MFY	1	t	42
1161	Soy MFY	1	t	42
1162	Uchqurg`on MFY	1	t	42
1163	Paxtakor QFY	1	t	42
1164	Yangi chek MFY	1	t	42
1165	Ovushqa MFY	1	t	42
1166	Cho`ngqirg`iz MFY	1	t	42
1167	Teraktagi MFY	1	t	42
1168	Qumshaydon MFY	1	t	42
1169	Ko`kto`nlik MFY	1	t	42
1170	Eskiqo`rg`on MFY	1	t	42
1171	Uchko`za MFY	1	t	42
1172	Fayzaobod MFY	1	t	42
1173	To`raobod MFY	1	t	42
1174	Yolg`izbog`-1 MFY	1	t	42
1175	Yolg`izbog`-2 MFY	1	t	42
1176	Qoraqo`rg`on MFY	1	t	42
1177	Qayir MFY	1	t	42
1178	Madaniyat QFY	1	t	42
1179	Bo`ston MFY	1	t	42
1180	Xamza MFY	1	t	42
1181	Bodrog`obod MFY	1	t	42
1182	Guliston MFY	1	t	42
1183	Qirg`izqo`rg`on MFY	1	t	42
1184	Do`stlik MFY	1	t	42
1185	Chorbog` MFY	1	t	42
1186	Mustaqillik MFY	1	t	42
1187	Madaniyat MFY	1	t	42
1188	Izboskan MFY	1	t	42
1189	Sanoat MFY	1	t	42
1190	Tinchlik MFY	1	t	42
1191	Yangi xayot MFY	1	t	42
1192	Toshqo`rg`on MFY	1	t	42
1193	Soxil MFY	1	t	42
1194	Andijon MFY	1	t	42
1195	Ittifoq MFY	1	t	42
1196	Xolboyota MFY	1	t	42
1197	Buston QFY	1	t	42
1198	Bo`ston MFY	1	t	42
1199	Navbaxor MFY	1	t	42
1200	Yangi xayot MFY	1	t	42
1201	Do`stlik MFY	1	t	42
1202	Oq-oltin QFY	1	t	43
1203	Obod MFY	1	t	43
1204	Ulug`bek MFY	1	t	43
1205	Bobur MFY	1	t	43
1206	Shaxriobod MFY	1	t	43
1207	Ovulmat MFY	1	t	43
1208	Gagarin MFY	1	t	43
1209	Navoiy QFY	1	t	43
1210	Sariqsuv MFY	1	t	43
1211	Yangiobod MFY	1	t	43
1212	To`rttol MFY	1	t	43
1213	Oq tom MFY	1	t	43
1214	Guliston MFY	1	t	43
1215	Mingbuloq QFY	1	t	43
1216	Cho`lobod MFY	1	t	43
1217	Mingbuloq MFY	1	t	43
1218	Terakzor MFY	1	t	43
1219	Bo`ston MFY	1	t	43
1220	Dexqonobod MFY	1	t	43
1221	O`zbekiston MFY	1	t	43
1222	Mingchinor QFY	1	t	43
1223	Mingchinor MFY	1	t	43
1224	Uchko`prik MFY	1	t	43
1225	Kampirravot MFY	1	t	44
1226	Teyit MFY	1	t	44
1227	Mustaqillik MFY	1	t	44
1228	Fitrat MFY	1	t	44
1229	Istiqlol MFY	1	t	44
1230	Anxor MFY	1	t	44
1231	Xonobod MFY	1	t	44
1232	Oxunboboev MFY	1	t	44
1233	Madraximov MFY	1	t	44
1234	Navoiy MFY	1	t	44
1235	Xidirsha MFY	1	t	44
1236	Yangi hayot MFY	1	t	44
1237	Xonobod SHFY	1	t	44
1238	Fozilmon MFY	1	t	44
1239	S.Mexmonov MFY	1	t	44
1240	Andijon MFY	1	t	45
1241	Beshkaram MFY	1	t	45
1242	Navoiy MFY	1	t	45
1243	Jo`me MFY	1	t	45
1244	Baxrin MFY	1	t	45
1245	Guliston MFY	1	t	45
1246	Uzun ko`chasi MFY	1	t	45
1247	Bobur MFY	1	t	45
1248	Chimbuloq MFY	1	t	45
1249	Kurama MFY	1	t	45
1250	So`qaloq MFY	1	t	45
1251	Yetmishmergan MFY	1	t	45
1252	Guraguri MFY	1	t	45
1253	Xo`jaobod QFY	1	t	45
1254	Sanoatchilar SHFY	1	t	45
1255	Ipakchi MFY	1	t	45
1256	Beshqovoq MFY	1	t	45
1257	Solpi MFY	1	t	45
1258	Oltin vodiy QFY	1	t	45
1259	Ko`tarma SHFY	1	t	45
1260	Sarqamish MFY	1	t	45
1261	Xidirsha MFY	1	t	45
1262	Yangi xayot MFY	1	t	45
1263	Qorabuloq MFY	1	t	45
1264	Uch ko`chasi MFY	1	t	45
1265	Mustaxkam MFY	1	t	45
1266	Ko`prikboshi MFY	1	t	45
1267	Birlashgan QFY	1	t	45
1268	Manak MFY	1	t	45
1269	Yangi Farg`ona MFY	1	t	45
1270	Egamberdiobod MFY	1	t	45
1271	Faqirqishloq MFY	1	t	45
1272	To`raobod MFY	1	t	45
1273	Dilkushod MFY	1	t	45
1274	Quvvatmurod MFY	1	t	45
1275	Karnaychi MFY	1	t	45
1276	Orday MFY	1	t	45
1277	Nishobbo`yi MFY	1	t	45
1278	Tosh ota MFY	1	t	45
1279	Guliston MFY	1	t	45
1280	Manak QFY	1	t	45
1281	Do`rman MFY	1	t	46
1282	Xo`jaobod MFY	1	t	46
1283	Segaza MFY	1	t	46
1284	Yonbosh durman MFY	1	t	46
1285	Begbachcha MFY	1	t	46
1286	Ortish MFY	1	t	46
1287	Qum MFY	1	t	46
1288	Paxtaobod Q.F.Y	1	t	46
1289	Polason MFY	1	t	46
1290	Oqto`nnik MFY	1	t	46
1291	Axmadbek MFY	1	t	46
1292	Shaydo MFY	1	t	46
1293	Qalacha MFY	1	t	46
1294	Toshtepa Q.F.Y	1	t	46
1295	Qibchaqo`rg`on MFY	1	t	46
1296	Yuzlar MFY	1	t	46
1297	Nayman MFY	1	t	46
1298	Markaz MFY	1	t	46
1299	Yangi yo`l Q.F.Y	1	t	46
1300	Vaxim MFY	1	t	46
1301	Yangi vaxim MFY	1	t	46
1302	Beshmaxalla MFY	1	t	46
1303	Karnaychi MFY	1	t	46
1304	Guliston Q.F.Y	1	t	46
1305	Tegirmon boshi MFY	1	t	46
1306	Qoziqo`rg`on MFY	1	t	46
1307	Andijonlik MFY	1	t	46
1308	Shokirboy MFY	1	t	46
1309	Yangi maxalla MFY	1	t	46
1310	O`rta sharhon Q.F.Y	1	t	46
1311	Qo`rg`oncha MFY	1	t	46
1312	Nazarmaxram MFY	1	t	46
1313	Qumtepa MFY	1	t	46
1314	Nazarmaxram Q.F.Y	1	t	46
1315	Bayroq MFY	1	t	46
1316	Maslaxattepa MFY	1	t	46
1317	Qo`rg`oncha MFY	1	t	46
1318	Bobochik MFY	1	t	46
1319	Nayman MFY	1	t	46
1320	O`zbekiston Q.F.Y	1	t	46
1321	Yangi naynavo MFY	1	t	46
1322	Qorabo`yin MFY	1	t	46
1323	Qushqo`noq MFY	1	t	46
1324	Qum ariq MFY	1	t	46
1325	Azamat MFY	1	t	46
1326	To`lqin MFY	1	t	46
1327	Naynavo Q.F.Y	1	t	46
1328	Cho`ja MFY	1	t	46
1329	Eshon qishloq MFY	1	t	46
1330	Bo`ston MFY	1	t	46
1331	Do`stlik MFY	1	t	46
1332	Quruqsor MFY	1	t	46
1333	Cho`ja Q.F.Y	1	t	46
1334	So`zoq MFY	1	t	46
1335	Abdubiy MFY	1	t	46
1336	Shurqo`rg`on MFY	1	t	46
1337	Oqto`nlik MFY	1	t	46
1338	Birlashkan MFY	1	t	46
1339	Qumqayroq MFY	1	t	46
1340	Abdubiy Q.F.Y	1	t	46
1341	Qashqar MFY	1	t	46
1342	Saroy MFY	1	t	46
1343	Paxtako`l MFY	1	t	46
1344	Dorilamo MFY	1	t	46
1345	Xaqiqat Q.F.Y	1	t	46
1346	Soxiobod MFY	1	t	46
1347	Tumor MFY	1	t	46
1348	Yangi maxalla MFY	1	t	46
1349	Do`lan MFY	1	t	46
1350	Yuqori shahrixon Q.F.Y	1	t	46
1351	Abdusamad MFY	1	t	46
1352	Andijonlik MFY	1	t	46
1353	Beshariq MFY	1	t	46
1354	Buvayda MFY	1	t	46
1355	Bo`ston MFY	1	t	46
1356	Qayrog`ich guzar MFY	1	t	46
1357	Qorako`rpa MFY	1	t	46
1358	Mullaboy MFY	1	t	46
1359	Mustaqillik MFY	1	t	46
1360	Navbaxor MFY	1	t	46
1361	Navro`z MFY	1	t	46
1362	Nomozgox MFY	1	t	46
1363	Taraqqiyot MFY	1	t	46
1364	Teraktagi MFY	1	t	46
1365	O`zbekiston MFY	1	t	46
1366	Shahrixon MFY	1	t	46
1367	Yakka tut MFY	1	t	46
1368	Yangi xayot MFY	1	t	46
1369	1-son M.Narshaxiy MFY	1	t	47
1370	2-son S.Boxarziy MFY	1	t	47
1371	3-son Furqat MFY	1	t	47
1372	4-son A.Navoiy MFY	1	t	47
1373	5-son G`.G`ulom MFY	1	t	47
1374	6-son Ko`kaldosh MFY	1	t	47
1375	7-son Imom-al Buxoriy MFY	1	t	47
1376	8-son H.Olimjon MFY	1	t	47
1377	9-son J.Ikromiy MFY	1	t	47
1378	10-son A.Fitrat MFY	1	t	47
1379	11-son S.Sheroziy MFY	1	t	47
1380	12-son Xo`ja Xunjoriy MFY	1	t	47
1381	13- son "Jo`ybor" MFY	1	t	47
1382	14- son Abu Ali ibn Sino MFY	1	t	47
1383	15- son Nizomiy MFY	1	t	47
1384	16- son M.Ashrafiy MFY	1	t	47
1385	17-son S.Raximov MFY	1	t	47
1386	18-son Dilkusho MFY	1	t	47
1387	19- son F.Xo`jaev MFY	1	t	47
1388	20-son M.Ulugbek MFY	1	t	47
1389	21-son Shergiron MFY	1	t	47
1390	22-son Chorbaxosa MFY	1	t	47
1391	23-son Ko`ksaroy MFY	1	t	47
1392	24-son Shayx-ul Olam MFY	1	t	47
1393	25-son Sitorai Moxi-xosa MFY	1	t	47
1394	26- son Turki Jandi MFY	1	t	47
1395	27-son Sharq Yulduzi MFY	1	t	47
1396	28-son M.Burxonov MFY	1	t	47
1397	29-son Gulchorbog` MFY	1	t	47
1398	30-son Xavzi Nav MFY	1	t	47
1399	31-son Yangiobod MFY	1	t	47
1400	32-son Guliston MFY	1	t	47
1401	33-son A.G`ijduvoniy MFY	1	t	47
1402	34-son Navro`z MFY	1	t	47
1403	35-son Bunyodkor MFY	1	t	47
1404	36-son Zarafshon MFY	1	t	47
1405	37-son A.Temur MFY	1	t	47
1406	38-son Piridastgir MFY	1	t	47
1407	39-son Shodlik MFY	1	t	47
1408	40-son R.Xamroev MFY	1	t	47
1409	41-son Gulshan MFY	1	t	47
1410	42-son Varaxsha MFY	1	t	47
1411	43-son Olim Xo`jaev MFY	1	t	47
1412	44-son To`qimachi MFY	1	t	47
1413	45-son Foshun MFY	1	t	47
1414	46-son Do`stlik MFY	1	t	47
1415	47-son Istiqlol MFY	1	t	47
1416	48-son Yoshlik MFY	1	t	47
1417	49-son Navbaxor MFY	1	t	47
1418	50-son Namozgox MFY	1	t	47
1419	51-son B.Nakshband MFY	1	t	47
1420	52-son Afshor MFY	1	t	47
1421	53-son M.Tarobiy MFY	1	t	47
1422	54-son Losha MFY	1	t	47
1423	55-son S.Ayniy MFY	1	t	47
1424	56-son A.Donish MFY	1	t	47
1425	57-son Bixishtiyon MFY	1	t	47
1426	58-son Toshmasjid MFY	1	t	47
1427	59-son Oybek MFY	1	t	47
1428	60-son Xujamushkin MFY	1	t	47
1429	61-son Bogidasht MFY	1	t	47
1430	62-son A.Sifatmuniy MFY	1	t	47
1431	63-son Shayxon MFY	1	t	47
1432	64-son Otbozor MFY	1	t	47
1433	65-son Shirbuddin MFY	1	t	47
1434	Kuchkumar QFY	1	t	48
1435	Kavola Maxmud QFY	1	t	48
1436	Sufikorgar QFY	1	t	48
1437	Bogikalon QFY	1	t	48
1438	Kushxodim MFY	1	t	48
1439	Yangiturmush QFY	1	t	48
1440	Turkon MFY	1	t	48
1441	Istikbol QFY	1	t	48
1442	Rabotak MFY	1	t	48
1443	Kunji-kal`a QFY	1	t	48
1444	Novmetan MFY	1	t	48
1445	Zarmanok MFY	1	t	48
1446	Shergiron QFY	1	t	48
1447	Rabotipoyon MFY	1	t	48
1448	Xonabod MFY	1	t	48
1449	Yurinbolo QFY	1	t	48
1450	Talaliyon MFY	1	t	48
1451	Kulonxona MFY	1	t	48
1452	Rabotikalmok QFY	1	t	48
1453	Dexcha MFY	1	t	48
1454	Arabxona MFY	1	t	48
1455	Podshoxi MFY	1	t	48
1456	Losha QFY	1	t	48
1457	Xumin MFY	1	t	48
1458	Bogdasht MFY	1	t	48
1459	Shexoncha QFY	1	t	48
1460	Saxovat QFY	1	t	48
1461	Soxibkor QFY	1	t	48
1462	Mustakillik MFY	1	t	48
1463	Galaosiyo MFY	1	t	48
1464	Dustlik MFY	1	t	48
1465	Navruz MFY	1	t	48
1466	Oybek MFY	1	t	48
1467	Kumushkent QFY	1	t	49
1468	Rozmoz MFY	1	t	49
1469	Xo`jarabod MFY	1	t	49
1470	Cariosiyo MFY	1	t	49
1471	Xalvogaron MFY	1	t	49
1472	Exson QFY	1	t	49
1473	Garibshox MFY	1	t	49
1474	Ko`lxatib MFY	1	t	49
1475	Teraklik MFY	1	t	49
1476	Kipchok QFY	1	t	49
1477	Mirvoshi MFY	1	t	49
1478	Changaron MFY	1	t	49
1479	Churikalon MFY	1	t	49
1480	Sufidexkon MFY	1	t	49
1481	Kungirot QFY	1	t	49
1482	Kosari MFY	1	t	49
1483	Muminobod MFY	1	t	49
1484	Beshrabod MFY	1	t	49
1485	Xajivon MFY	1	t	49
1486	Roxkent QFY	1	t	49
1487	Qo`qin MFY	1	t	49
1488	Guliston MFY	1	t	49
1489	Arabxona MFY	1	t	49
1490	Pirmast QFY	1	t	49
1491	Bozorjoyi MFY	1	t	49
1492	Anjirbog MFY	1	t	49
1493	Ko`lodina MFY	1	t	49
1494	Xalach QFY	1	t	49
1495	Latifsobungar MFY	1	t	49
1496	Shakarkent MFY	1	t	49
1497	Niyozxuja MFY	1	t	49
1498	Xargush QFY	1	t	49
1499	Katagan MFY	1	t	49
1500	Panob MFY	1	t	49
1501	Nayman MFY	1	t	49
1502	Xargo`sh MFY	1	t	49
1503	Xayrobodcha QFY	1	t	49
1504	Pushmon MFY	1	t	49
1505	Uzbakon MFY	1	t	49
1506	Shanba MFY	1	t	49
1507	Imomkozixon QFY	1	t	49
1508	Xalach MFY	1	t	49
1509	Kalti MFY	1	t	49
1510	Yangikent QFY	1	t	49
1511	Shoxnigor MFY	1	t	49
1512	Chorbogkent MFY	1	t	49
1513	Shirin MFY	1	t	49
1514	Vobkent MFY	1	t	49
1515	Charmgaron MFY	1	t	49
1516	Shifokor MFY	1	t	49
1517	Dustlik MFY	1	t	49
1518	Kuruvchi MFY	1	t	49
1519	S.Raximov MFY	1	t	49
1520	Kulolchi MFY	1	t	49
1521	Rabotoxun MFY	1	t	49
1522	F.Yunusov QFY	1	t	50
1523	Havzak MFY	1	t	50
1524	Paxtaobod QFY	1	t	50
1525	Ayirtom MFY	1	t	50
1526	Toshloq MFY	1	t	50
1527	Ulfatbibi QFY	1	t	50
1528	Rostgo`y MFY	1	t	50
1529	Oqrabot MFY	1	t	50
1530	Baqqollar MFY	1	t	50
1531	G`ishti MFY	1	t	50
1532	Beshtuvo MFY	1	t	50
1533	Baraka MFY	1	t	50
1534	Qaraxoni QFY	1	t	50
1535	Qarabog` MFY	1	t	50
1536	Qo`riq MFY	1	t	50
1537	Olmazor MFY	1	t	50
1538	Soktari QFY	1	t	50
1539	Mirakon MFY	1	t	50
1540	Tarxanon MFY	1	t	50
1541	Saidkent MFY	1	t	50
1542	Sarvari QFY	1	t	50
1543	Kalon MFY	1	t	50
1544	Tavariyon MFY	1	t	50
1545	Zarangari QFY	1	t	50
1546	Bo`lakiyon MFY	1	t	50
1547	Mahalla MFY	1	t	50
1548	Mustaqillik MFY	1	t	50
1549	G`ovshun QFY	1	t	50
1550	Xatcha MFY	1	t	50
1551	O`zanon MFY	1	t	50
1552	Mahallai Mirzayon MFY	1	t	50
1553	Mazragan MFY	1	t	50
1554	Biyosin MFY	1	t	50
1555	Sarmijon QFY	1	t	50
1556	Ko`lijabbor MFY	1	t	50
1557	Labiro`t MFY	1	t	50
1558	Gajdumak MFY	1	t	50
1559	Jovgari MFY	1	t	50
1560	Firishkent QFY	1	t	50
1561	Sho`rcha MFY	1	t	50
1562	Sohibiyon MFY	1	t	50
1563	Qassabon MFY	1	t	50
1564	Zargaron MFY	1	t	50
1565	Armechan QFY	1	t	50
1566	Cho`g`alon MFY	1	t	50
1567	Todon MFY	1	t	50
1568	Denov MFY	1	t	50
1569	Buktaroy QFY	1	t	50
1570	Chag`dari MFY	1	t	50
1571	Buktaroy MFY	1	t	50
1572	Vazirshox MFY	1	t	50
1573	Ko`shk MFY	1	t	50
1574	Taxtaxon MFY	1	t	50
1575	Pozagari QFY	1	t	50
1576	Dodarak MFY	1	t	50
1577	Qumoq MFY	1	t	50
1578	Karna MFY	1	t	50
1579	Ko`kcha QFY	1	t	50
1580	Zafarobod SHFY	1	t	50
1581	Chorsu MFY	1	t	50
1582	Sardor MFY	1	t	50
1583	Qo`rg`on MFY	1	t	50
1584	A.G`ijduvoniy MFY	1	t	50
1585	Dilkusho MFY	1	t	50
1586	F.Xo`jaev MFY	1	t	50
1587	Sharq MFY	1	t	50
1588	A.Qahhor MFY	1	t	50
1589	Pomo`za MFY	1	t	50
1590	Guliston MFY	1	t	50
1591	Bobur MFY	1	t	50
1592	F.Yunusov MFY	1	t	50
1593	Nodirabegim MFY	1	t	50
1594	Ulug`bek MFY	1	t	50
1595	Degrezon MFY	1	t	50
1596	Samonchuq QFY	1	t	51
1597	Murg`ak MFY	1	t	51
1598	Samonchuq shfy	1	t	51
1599	Xumdonak QFY	1	t	51
1600	Ushot MFY	1	t	51
1601	Pasana MFY	1	t	51
1602	Ko`liyon MFY	1	t	51
1603	Po`loti QFY	1	t	51
1604	Zangi MFY	1	t	51
1605	Sho`robot MFY	1	t	51
1606	Demun MFY	1	t	51
1607	Hazorman MFY	1	t	51
1608	Xumin QFY	1	t	51
1609	Qalmoq MFY	1	t	51
1610	Qozikenti MFY	1	t	51
1611	Boloiob MFY	1	t	51
1612	Qaroli QFY	1	t	51
1613	Dovud MFY	1	t	51
1614	Xo`jaxayron MFY	1	t	51
1615	Eronshox MFY	1	t	51
1616	Yangiobod MFY	1	t	51
1617	Sapatta QFY	1	t	51
1618	Tobagar MFY	1	t	51
1619	Chorzona MFY	1	t	51
1620	Darveshi MFY	1	t	51
1621	Navrabot QFY	1	t	51
1622	Bahoriston MFY	1	t	51
1623	Oytug`di MFY	1	t	51
1624	Pochchoyi MFY	1	t	51
1625	Qorovul MFY	1	t	51
1626	Aleli QFY	1	t	51
1627	Jondor MFY	1	t	51
1628	Obod MFY	1	t	51
1629	Rabot MFY	1	t	51
1630	Oxshix QFY	1	t	51
1631	Namgoni MFY	1	t	51
1632	Qovchin MFY	1	t	51
1633	Lolo QFY	1	t	51
1634	Luqmon MFY	1	t	51
1635	Romish QFY	1	t	51
1636	Oqtepa MFY	1	t	51
1637	Qazoqon MFY	1	t	51
1638	Dalmun QFY	1	t	51
1639	Dalmunobod MFY	1	t	51
1640	Jamiyat MFY	1	t	51
1641	Mirzayon QFY	1	t	51
1642	Yosh kuch MFY	1	t	51
1643	Jondor SHFY	1	t	51
1644	Paxtakor MFY	1	t	51
1645	Zarafshon MFY	1	t	51
1646	Navgadi MFY	1	t	51
1647	Beklar QFY	1	t	52
1648	Istiqbol MFY	1	t	52
1649	Niyoz hoji QFY	1	t	52
1650	O`ba-cho`li MFY	1	t	52
1651	Mustaqillik MFY	1	t	52
1652	Nurafshon QFY	1	t	52
1653	Xukumatobod MFY	1	t	52
1654	Sorgun MFY	1	t	52
1655	Geofizika MFY	1	t	52
1656	Tutkunda MFY	1	t	52
1657	Sarayon QFY	1	t	52
1658	Navro`z MFY	1	t	52
1659	O`rta-cho`l MFY	1	t	52
1660	Choloki MFY	1	t	52
1661	Siyozpoyon QFY	1	t	52
1662	Tuniroq MFY	1	t	52
1663	Kogon QFY	1	t	52
1664	Naqshband QFY	1	t	52
1665	Suxor MFY	1	t	52
1666	Xo`ja-yakshaba QFY	1	t	52
1667	Yangi-hayot QFY	1	t	52
1668	Arabxona MFY	1	t	53
1669	F.Xujaev MFY	1	t	53
1670	Maxtumkuli MFY	1	t	53
1671	Zirabod MFY	1	t	53
1672	Furkat MFY	1	t	53
1673	A.Kodiriy MFY	1	t	53
1674	A.Navoiy MFY	1	t	53
1675	Ziekor MFY	1	t	53
1676	Xuja bargi MFY	1	t	53
1677	Bobur MFY	1	t	53
1678	B.Zokirov MFY	1	t	53
1679	Temir yo`lchi MFY	1	t	53
1680	A.Temur MFY	1	t	53
1681	Istiklol MFY	1	t	53
1682	Navzirabod MFY	1	t	53
1683	B. Sharif MFY	1	t	53
1684	Dustlik MFY	1	t	53
1685	Beruniy MFY	1	t	53
1686	Turkiston MFY	1	t	53
1687	Ulugbek MFY	1	t	53
1688	Mustakillik MFY	1	t	53
1689	Eski kal`a MFY	1	t	54
1690	Zarafshon MFY	1	t	54
1691	Paxtakor MFY	1	t	54
1692	Chekirchi MFY	1	t	54
1693	Xujalar MFY	1	t	54
1694	Dustlik MFY	1	t	54
1695	Tinchlik MFY	1	t	54
1696	Taykir MFY	1	t	54
1697	Korakul QFY	1	t	54
1698	Durman MFY	1	t	54
1699	Tojikent MFY	1	t	54
1700	Sayyot QFY	1	t	54
1701	Solur MFY	1	t	54
1702	Alikaxuja MFY	1	t	54
1703	Paykent MFY	1	t	54
1704	Dargali QFY	1	t	54
1705	Dargabogi MFY	1	t	54
1706	Shakarbek MFY	1	t	54
1707	Jigachi QFY	1	t	54
1708	Vaxm MFY	1	t	54
1709	Korakulonchi MFY	1	t	54
1710	Osiyo MFY	1	t	54
1711	Koraxoji QFY	1	t	54
1712	Dexkonobod MFY	1	t	54
1713	Arabxona MFY	1	t	54
1714	Kuyi Yangibozor QFY	1	t	54
1715	Arna MFY	1	t	54
1716	Koraun QFY	1	t	54
1717	Mirzakal`a MFY	1	t	54
1718	Yangi zamon MFY	1	t	54
1719	Sort MFY	1	t	54
1720	Chovli QFY	1	t	54
1721	Mustakillik MFY	1	t	54
1722	Mirob MFY	1	t	54
1723	Ok oltin MFY	1	t	54
1724	Mallasheyx QFY	1	t	54
1725	Xujakon MFY	1	t	54
1726	Ziyorat QFY	1	t	54
1727	Regeydar MFY	1	t	54
1728	Kozon QFY	1	t	54
1729	Yangi turmush MFY	1	t	54
1730	Istiklol MFY	1	t	54
1731	Tashabbus MFY	1	t	54
1732	Shuroobod QFY	1	t	54
1733	Bandboshi QFY	1	t	54
1734	Kulonchi QFY	1	t	54
1735	Chandirobod QFY	1	t	54
1736	Kuvvacha QFY	1	t	54
1737	Yangi kal`a MFY	1	t	54
1738	Al-Buxoriy MFY	1	t	55
1739	Cho`lquvar MFY	1	t	55
1740	Tinchlik MFY	1	t	55
1741	Bo`ston MFY	1	t	55
1742	Bo`zachi MFY	1	t	55
1743	Navbahor QFY	1	t	55
1744	Jarqoq QFY	1	t	55
1745	Jumabozor QFY	1	t	56
1746	Chovdur MFY	1	t	56
1747	Muxtor MFY	1	t	56
1748	Jumabozor MFY	1	t	56
1749	Kesakli MFY	1	t	56
1750	Soinkorovul QFY	1	t	56
1751	Chorbog QFY	1	t	56
1752	Asajam MFY	1	t	56
1753	Usmonshayx MFY	1	t	56
1754	Yoshbotir MFY	1	t	56
1755	Chandir QFY	1	t	56
1756	Buribek Chandir MFY	1	t	56
1757	Ganchi Chandir MFY	1	t	56
1758	Xidreyli MFY	1	t	56
1759	Buston MFY	1	t	56
1760	Baxoriston QFY	1	t	56
1761	Kirtay	1	t	56
1762	Uzbekiston MFY	1	t	56
1763	Kul Chovdur MFY	1	t	56
1764	Paxtakor QFY	1	t	56
1765	Bayot MFY	1	t	56
1766	Kumkashon MFY	1	t	56
1767	Guliston QFY	1	t	56
1768	Opshok MFY	1	t	56
1769	Dilkor MFY	1	t	56
1770	Xosabuyi MFY	1	t	56
1771	Kirlishon QFY	1	t	56
1772	Denov QFY	1	t	56
1773	Kuk kuz MFY	1	t	56
1774	Pichokchi MFY	1	t	56
1775	Davlatboy MFY	1	t	56
1776	Balandmachit	1	t	56
1777	Talkonsayyot QFY	1	t	56
1778	Ok oltin MFY	1	t	56
1779	Fayzobod MFY	1	t	56
1780	Burjok MFY	1	t	56
1781	Solokorovul MFY	1	t	56
1782	Arabxona MFY	1	t	56
1783	Eski Olot MFY	1	t	56
1784	Akkali MFY	1	t	56
1785	Bunyodkor MFY	1	t	56
1786	Xalifa MFY	1	t	56
1787	Nonimas MFY	1	t	56
1788	Yangibozor SHFY	1	t	57
1789	Mustaqillik MFY	1	t	57
1790	Chiqirchi MFY	1	t	57
1791	Istiqbol QFY	1	t	57
1792	Navbahor MFY	1	t	57
1793	Bog`imuso QFY	1	t	57
1794	Valfajr MFY	1	t	57
1795	Ibn Sino QFY	1	t	57
1796	Sadir MFY	1	t	57
1797	Deycha MFY	1	t	57
1798	Zandani QFY	1	t	57
1799	Bobohoji MFY	1	t	57
1800	Xorkash MFY	1	t	57
1801	Qoraqalpoq QFY	1	t	57
1802	Do`stlik MFY	1	t	57
1803	Yangiobod MFY	1	t	57
1804	Xo`lbor MFY	1	t	57
1805	KalaymirishkorQFY	1	t	57
1806	So'sana MFY	1	t	57
1807	Talisobun MFY	1	t	57
1808	Navoiy QFY├б	1	t	57
1809	Uzbek MFY	1	t	57
1810	Varaxsho QFY	1	t	57
1811	Turkiston MFY	1	t	57
1812	Kuyovxo`ja MFY	1	t	57
1813	MFY	1	t	57
1814	Navgoxon MFY	1	t	57
1815	SHFYB	1	t	57
1816	QFYB	1	t	57
1817	MFY	1	t	57
1818	MFY	1	t	57
1819	Xurram MFY	1	t	57
1820	QFYB	1	t	57
1821	MFY	1	t	57
1822	MFY	1	t	57
1823	Jongeldi QFY	1	t	57
1824	Romitan QFY	1	t	58
1825	Tarnavut MFY	1	t	58
1826	Attaron MFY	1	t	58
1827	Mirishkor MFY	1	t	58
1828	Bog`cha MFY	1	t	58
1829	O`ba MFY	1	t	58
1830	Qahramon MFY	1	t	58
1831	Q,Chorbog` MFY	1	t	58
1832	Mug`oncha MFY	1	t	58
1833	Chelongu QFY	1	t	58
1834	Chandir MFY	1	t	58
1835	Toshrabot MFY	1	t	58
1836	Urganjiyon MFY	1	t	58
1837	Xosa MFY	1	t	58
1838	Decha MFY	1	t	58
1839	G`azberon MFY	1	t	58
1840	Qo`rg`on QFY	1	t	58
1841	Baxtiyorchi MFY	1	t	58
1842	Azizon MFY	1	t	58
1843	Samosiy MFY	1	t	58
1844	O`zbekiston MFY	1	t	58
1845	Bog`iturkon QFY	1	t	58
1846	Qumrabot MFY	1	t	58
1847	Bog`isaydon MFY	1	t	58
1848	Xo`jaubbon MFY	1	t	58
1849	Marziya MFY	1	t	58
1850	Hofizrabot MFY	1	t	58
1851	Hazortut MFY	1	t	58
1852	Sho`rcha QFY	1	t	58
1853	O`tabek MFY	1	t	58
1854	Sho`robod MFY	1	t	58
1855	Yomg`ir MFY	1	t	58
1856	Mo`ri MFY	1	t	58
1857	Sho`rcha MFY	1	t	58
1858	Qoqishtuvon MFY	1	t	58
1859	Poyjo`y MFY	1	t	58
1860	Qizilravot QFY	1	t	58
1861	MFY	1	t	58
1862	MFY	1	t	58
1863	MFY	1	t	58
1864	MFY	1	t	58
1865	MFY	1	t	58
1866	MFY	1	t	58
1867	MFY	1	t	58
1868	Baynalminal MFY	1	t	58
1869	Durmen QFY	1	t	59
1870	Sultonobod MFY	1	t	59
1871	Temirchi MFY	1	t	59
1872	Shibirgon MFY	1	t	59
1873	Denav QFY	1	t	59
1874	Kayragoch MFY	1	t	59
1875	Pattaxon MFY	1	t	59
1876	Navbaxor MFY	1	t	59
1877	Nekkishi MFY	1	t	59
1878	Juyrabod QFY	1	t	59
1879	Xorin MFY	1	t	59
1880	Kalon MFY	1	t	59
1881	Juyrabod MFY	1	t	59
1882	Kurishkent MFY	1	t	59
1883	Dorigar MFY	1	t	59
1884	Mingchinor MFY	1	t	59
1885	Tezguzar QFY	1	t	59
1886	Boboxaydar MFY	1	t	59
1887	Paxtaobod MFY	1	t	59
1888	Savrak QFY	1	t	59
1889	Kotiyon MFY	1	t	59
1890	Xorkash MFY	1	t	59
1891	S.Jura QFY	1	t	59
1892	Mirzokul MFY	1	t	59
1893	Bobo-Ato MFY	1	t	59
1894	Chandir QFY	1	t	59
1895	Chitkaron MFY	1	t	59
1896	Jushura MFY	1	t	59
1897	Arabxona MFY	1	t	59
1898	Sh.Xamroev QFY	1	t	59
1899	Talisangobod MFY	1	t	59
1900	Guliston MFY	1	t	59
1901	Nurafshon MFY	1	t	59
1902	Juynav QFY	1	t	59
1903	Talisafed MFY	1	t	59
1904	Gulomte MFY	1	t	59
1905	Vardonze QFY	1	t	59
1906	Yangikishlok MFY	1	t	59
1907	K.Vardonze MFY	1	t	59
1908	Bogiafzal QFY	1	t	59
1909	Pashmon MFY	1	t	59
1910	Jilvon MFY	1	t	59
1911	Iskogare QFY	1	t	59
1912	Yu.Iskogare MFY	1	t	59
1913	Kuyi Chukurak	1	t	59
1914	X.Orif MFY	1	t	59
1915	Shodlik MFY	1	t	59
1916	Kalmakon MFY	1	t	59
1917	Savrak MFY	1	t	59
1918	Zarchabek MFY	1	t	59
1919	O.Vodiy QFY	1	t	60
1920	Yangibo`ston QFY	1	t	60
1921	Zarafshon QFY	1	t	60
1922	Do`stlik QFY	1	t	60
1923	Bo`ston QFY	1	t	60
1924	Cho`lquvar QFY	1	t	60
1925	Toshkent MFY	1	t	60
1926	G`.G`ulom MFY	1	t	60
1927	Bobur MFY	1	t	60
1928	Forish MFY	1	t	60
1929	Baxtli MFY	1	t	60
1930	Chinobod MFY	1	t	60
1931	Tinchlik MFY	1	t	60
1932	O`smat SHFY	1	t	61
1933	Qutlug`obod MFY	1	t	61
1934	Oyqor QFY	1	t	61
1935	Baxmal QFY	1	t	61
1936	Mo`g`ol QFY	1	t	61
1937	Oqtosh QFY	1	t	61
1938	Do`stlik MFY	1	t	61
1939	Novqa MFY	1	t	61
1940	Saroy MFY	1	t	61
1941	Tongotar QFY	1	t	61
1942	Shodmon MFY	1	t	61
1943	Qatortol MFY	1	t	61
1944	Bo`ron MFY	1	t	61
1945	Do`smat MFY	1	t	61
1946	Muzbuloq MFY	1	t	61
1947	Alamli MFY	1	t	61
1948	Madaniyat MFY	1	t	61
1949	G`allakon MFY	1	t	61
1950	Yangibog` MFY	1	t	61
1951	Toypoqsoy MFY	1	t	61
1952	Nushkent MFY	1	t	61
1953	Uzunbuloq QFY	1	t	61
1954	Barlos QFY	1	t	61
1955	Bog`ishamol QFY	1	t	61
1956	Sangzor QFY	1	t	61
1957	Gulbuloq QFY	1	t	61
1958	Marjonbuloq SHFY	1	t	62
1959	Qo`ytosh SHFY	1	t	62
1960	Do`stlik MFY	1	t	62
1961	Alamli MFY	1	t	62
1962	Samarqand MFY	1	t	62
1963	G`.G`ulom MFY	1	t	62
1964	Olimlar MFY	1	t	62
1965	Baxt MFY	1	t	62
1966	Madaniyat QFY	1	t	62
1967	Buloqboshi QFY	1	t	62
1968	Guliston QFY	1	t	62
1969	Tozaurug` QFY	1	t	62
1970	Mirzabuloq QFY	1	t	62
1971	Mulkush QFY	1	t	62
1972	Moltob QFY	1	t	62
1973	G`o`bdin QFY	1	t	62
1974	Xonimqo`rg`on QFY	1	t	62
1975	Qipchoqsuv QFY	1	t	62
1976	Jiydali QFY	1	t	62
1977	Korizquduq QFY	1	t	62
1978	Gulchambar QFY	1	t	62
1979	Ko`kbuloq QFY	1	t	62
1980	Qashqabuloq QFY	1	t	62
1981	Oqtosh MFY	1	t	62
1982	Sarbozor MFY	1	t	62
1983	Savruk MFY	1	t	62
1984	A.Navoiy MFY	1	t	63
1985	G`.G`ulom MFY	1	t	63
1986	Xamza MFY	1	t	63
1987	Xolxo`jaev MFY	1	t	63
1988	Qahramon QFY	1	t	63
1989	Yangiobod QFY	1	t	63
1990	Saritepa QFY	1	t	63
1991	Bunyodkor QFY	1	t	63
1992	Istiqlol QFY	1	t	63
1993	Navro`z QFY	1	t	63
1994	Bog`zor QFY	1	t	63
1995	Mevazor QFY	1	t	63
1996	Ziyokor QFY	1	t	64
1997	Ziyokor MFY	1	t	64
1998	Xavastlik MFY	1	t	64
1999	Jizzaxlik MFY	1	t	64
2000	Sovungarlik MFY	1	t	64
2001	Qulama QFY	1	t	64
2002	Qo`shko`prik MFY	1	t	64
2003	Toshkentlik MFY	1	t	64
2004	Mulkanlik MFY	1	t	64
2005	Qatortol MFY	1	t	64
2006	Qizlartepa MFY	1	t	64
2007	Paxtaobod QFY	1	t	64
2008	Saraylik MFY	1	t	64
2009	Yaxtanlik MFY	1	t	64
2010	Eski Toshkentlik MFY	1	t	64
2011	Gandumtosh QFY	1	t	64
2012	Kuyovboshi MFY	1	t	64
2013	Gandumtosh MFY	1	t	64
2014	Xamzaobod QFY	1	t	64
2015	Ittifoq MFY	1	t	64
2016	Olmachi MFY	1	t	64
2017	G`ozg`ontepa MFY	1	t	64
2018	Pastki So`loqli MFY	1	t	64
2019	Oq oltin QFY	1	t	64
2020	Qorayantoq MFY	1	t	64
2021	Yangiobod MFY	1	t	64
2022	Tuyoqli MFY	1	t	64
2023	Fayzobod MFY	1	t	64
2024	Xayrobod QFY	1	t	64
2025	Xayrobod MFY	1	t	64
2026	Kattaqishloq MFY	1	t	64
2027	Sharilloq MFY	1	t	64
2028	Uch tepa QFY	1	t	64
2029	Uch tepa MFY	1	t	64
2030	Yangiobod MFY	1	t	64
2031	Yangihayot MFY	1	t	64
2032	Samarqandquduq QFY	1	t	64
2033	Qangli QFY	1	t	64
2034	Qangli MFY	1	t	64
2035	Yangiobod MFY	1	t	64
2036	Yoyilma MFY	1	t	64
2037	Toqchilik QFY	1	t	64
2038	Toqchilik MFY	1	t	64
2039	Ravalliq MFY	1	t	64
2040	Ravalliq - 1 MFY	1	t	64
2041	Ravot QFY	1	t	64
2042	Umar MFY	1	t	64
2043	Nonsingil MFY	1	t	64
2044	Uchqiz yangiqishloq MFY	1	t	64
2045	Qo`shbarmoq QFY	1	t	64
2046	Qaxramon MFY	1	t	64
2047	Qulpisar MFY	1	t	64
2048	Ko`rpasoy MFY	1	t	64
2049	Ittifoq MFY	1	t	65
2050	Yoshlik MFY	1	t	65
2051	Qaliya MFY	1	t	65
2052	So`loqli MFY	1	t	65
2053	Bobur MFY	1	t	65
2054	Zargarlik MFY	1	t	65
2055	Xalqabod MFY	1	t	65
2056	Olmazor MFY	1	t	65
2057	Qassoblik MFY	1	t	65
2058	O`ratepalik MFY	1	t	65
2059	X.Abdujabborov MFY	1	t	65
2060	Oqqo`rg`onlik MFY	1	t	65
2061	Toshloq MFY	1	t	65
2062	Zilol MFY	1	t	65
2063	Jizzaxlik MFY	1	t	65
2064	Ravalliq MFY	1	t	65
2065	Xamzaobod MFY	1	t	65
2066	Sayiljoyi MFY	1	t	65
2067	Kimyogar MFY	1	t	65
2068	Ko`tarma MFY	1	t	65
2069	Madaniyat MFY	1	t	65
2070	Ulug`bek MFY	1	t	65
2071	Tinchlik MFY	1	t	65
2072	Xayrobod MFY	1	t	65
2073	Sayxon MFY	1	t	65
2074	Qipchoq MFY	1	t	65
2075	Jelli-gulli MFY	1	t	65
2076	Navro`z MFY	1	t	65
2077	Bunyod MFY	1	t	65
2078	H.Olimjon MFY	1	t	65
2079	A.Navoiy MFY	1	t	65
2080	Sangzor MFY	1	t	65
2081	Do`stlik MFY	1	t	65
2082	Bunyodkor MFY	1	t	65
2083	Mustaqillik MFY	1	t	66
2084	Oybek MFY	1	t	66
2085	Tinchlik MFY	1	t	66
2086	Oqbuloq MFY	1	t	66
2087	Shodlik MFY	1	t	66
2088	Do`stlik MFY	1	t	66
2089	Navro`z MFY	1	t	66
2090	Yangiobod MFY	1	t	66
2091	Lalmikor QFY	1	t	66
2092	Taraqqiyot MFY	1	t	66
2093	Ravot MFY	1	t	66
2094	Navoiy MFY	1	t	66
2095	Yangihayot MFY	1	t	66
2096	Yangikent QFY	1	t	66
2097	Nurafshon MFY	1	t	66
2098	Adirobod QFY	1	t	66
2099	Tozaurug` MFY	1	t	66
2100	Andijon QFY	1	t	66
2101	Sharq yulduzi QFY	1	t	66
2102	Zafarobod SHFY	1	t	67
2103	Bo`ston MFY	1	t	67
2104	Samarqand MFY	1	t	67
2105	S.Sindarov QFY	1	t	67
2106	Yorqin QFY	1	t	67
2107	Birlik QFY	1	t	67
2108	Xulkar SHFY	1	t	67
2109	Lolazor QFY	1	t	67
2110	Chimqo`rg`on QFY	1	t	67
2111	Temiryazov QFY	1	t	67
2112	Ulug`bek MFY	1	t	68
2113	Xamza MFY	1	t	68
2114	Beruniy MFY	1	t	68
2115	Paxtakor MFY	1	t	68
2116	O`zbekiston MFY	1	t	68
2117	Qoratepa MFY	1	t	68
2118	Baxt MFY	1	t	68
2119	H.Olimjon MFY	1	t	68
2120	Zomin SHFY	1	t	68
2121	Bog`ishamol MFY	1	t	68
2122	Birlik MFY	1	t	68
2123	Kattabog` MFY	1	t	68
2124	Qayirma MFY	1	t	68
2125	Navbahor MFY	1	t	68
2126	Oqtepa MFY	1	t	68
2127	S.Rahimov MFY	1	t	68
2128	Sh.Rashidov MFY	1	t	68
2129	Qo`rg`on MFY	1	t	68
2130	G`.G`ulom MFY	1	t	68
2131	Beshkubi QFY	1	t	68
2132	Gulshan QFY	1	t	68
2133	Teshiktepa MFY	1	t	68
2134	Duoba QFY	1	t	68
2135	Istiqlol QFY	1	t	68
2136	Navoiy QFY	1	t	68
2137	Qo`shtol MFY	1	t	68
2138	Pishog`ar MFY	1	t	68
2139	Yoshlik MFY	1	t	68
2140	Achchi MFY	1	t	68
2141	Obi-hayot QFY	1	t	68
2142	Tinchlik QFY	1	t	68
2143	Guliston MFY	1	t	68
2144	Toshkesgan QFY	1	t	68
2145	Chorvador QFY	1	t	68
2146	Turkman MFY	1	t	68
2147	Shirin QFY	1	t	68
2148	G`allakor QFY	1	t	68
2149	To`rttom MFY	1	t	68
2150	Laylak uya MFY	1	t	68
2151	Yangi hayot QFY	1	t	68
2152	Chilonzor MFY	1	t	68
2153	Yerjar MFY	1	t	69
2154	Mustaqillik MFY	1	t	69
2155	Do`stlik MFY	1	t	69
2156	G`alaba MFY	1	t	69
2157	Ipak yo`li QFY	1	t	69
2158	Mirzadala QFY	1	t	69
2159	Toshkent QFY	1	t	69
2160	Yangidala QFY	1	t	69
2161	Paxtazor QFY	1	t	69
2162	O`zbekiston QFY	1	t	69
2163	Gulzor QFY	1	t	69
2164	Bog`bon QFY	1	t	69
2165	Do`stlik MFY	1	t	70
2166	Dilorom MFY	1	t	70
2167	Toshkent MFY	1	t	70
2168	Samarqand MFY	1	t	70
2169	Suvonobod MFY	1	t	70
2170	G`alaba MFY	1	t	70
2171	Oltinko`l MFY	1	t	70
2172	A.Ikromov QFY	1	t	70
2173	Paxtakor QFY	1	t	70
2174	Samarqand QFY	1	t	70
2175	Mingchinor QFY	1	t	70
2176	Chamanzor QFY	1	t	70
2177	Olmazor QFY	1	t	70
2178	Oq-buloq QFY	1	t	70
2179	Yangiqishloq SHFY	1	t	71
2180	E.Kamolov MFY	1	t	71
2181	Bog`don MFY	1	t	71
2182	O`zbekiston MFY	1	t	71
2183	Uchquloch SHFY	1	t	71
2184	Xonbandi MFY	1	t	71
2185	Omonkeldi QFY	1	t	71
2186	Darboza QFY	1	t	71
2187	Arnasoy QFY	1	t	71
2188	Qizilqum QFY	1	t	71
2189	Aydarovul MFY	1	t	71
2190	Egizbuloq QFY	1	t	71
2191	Oqtom MFY	1	t	71
2192	Egizbuloq MFY	1	t	71
2193	Nurak MFY	1	t	71
2194	Garasha QFY	1	t	71
2195	Garasha MFY	1	t	71
2196	Ilonli MFY	1	t	71
2197	Forish QFY	1	t	71
2198	Qo`lba MFY	1	t	71
2199	Uchma MFY	1	t	71
2200	Osmonsoy QFY	1	t	71
2201	Osmonsoy MFY	1	t	71
2202	Sayyod MFY	1	t	71
2203	Oqtepa MFY	1	t	71
2204	Qorabdol QFY	1	t	71
2205	Qorabdol ota MFY	1	t	71
2206	Narvon MFY	1	t	71
2207	Yassikechuv MFY	1	t	71
2208	Mustaqillik MFY	1	t	71
2209	O`xum QFY	1	t	71
2210	O`xum MFY	1	t	71
2211	Xovos QFY	1	t	72
2212	Puchug`oy MFY	1	t	72
2213	Balandchaqir MFY	1	t	72
2214	Sovot QFY	1	t	72
2215	Sovot MFY	1	t	72
2216	Sarmich QFY	1	t	72
2217	Yuqori Sarmich MFY	1	t	72
2218	Pastki sarmich MFY	1	t	72
2219	Xo`jamushkent QFY	1	t	72
2220	Erganakli MFY	1	t	72
2221	Xovotog` QFY	1	t	72
2222	Qo`shqand MFY	1	t	72
2223	Yangiobod MFY	1	t	72
2224	Batosh QFY	1	t	73
2225	Mo`minobod MFY	1	t	73
2226	Bo`ston QFY	1	t	73
2227	Avchonboch MFY	1	t	73
2228	Guliston QFY	1	t	73
2229	Do`ltali MFY	1	t	73
2230	Toshguzar MFY	1	t	73
2231	Chugurtma QFY	1	t	73
2232	Gulshan QFY	1	t	73
2233	Jarariq MFY	1	t	73
2234	Yonqishloq MFY	1	t	73
2235	Yakkadaraxt MFY	1	t	73
2236	Zarbdor QFY	1	t	73
2237	ch	1	t	73
2238	Qovchin MFY	1	t	73
2239	Qorako`l QFY	1	t	73
2240	Eshonquduq MFY	1	t	73
2241	Qo`shtepa QFY	1	t	73
2242	Apardi MFY	1	t	73
2243	ch	1	t	73
2244	Mexnatobod QFY	1	t	73
2245	ch	1	t	73
2246	Parmiston MFY	1	t	73
2247	Cho`michli MFY	1	t	73
2248	Pachkamar QFY	1	t	73
2249	Xalqobod QFY	1	t	73
2250	Xalqobod MFY	1	t	73
2251	Shakarbuloq QFY	1	t	73
2252	Yangikent MFY	1	t	73
2253	Sherali QFY	1	t	73
2254	Xo`jaguzar MFY	1	t	73
2255	Chanoq MFY	1	t	73
2256	Iqbol Egamberdieva	1	t	73
2257	Navro`z MFY	1	t	73
2258	h	1	t	73
2259	Paxtazor MFY	1	t	73
2260	Amir Temur MFY	1	t	73
2261	Ergash Qurbonov	1	t	73
2262	Tinchlik MFY	1	t	73
2263	Mustakillik MFY	1	t	73
2264	Dexkonobod SHFY	1	t	74
2265	Aerodrom MFY	1	t	74
2266	Oxunbobonv MFY	1	t	74
2267	Bibikorasoch QFY	1	t	74
2268	Gumbulok MFY	1	t	74
2269	Beshbulok MFY	1	t	74
2270	Otkamar MFY	1	t	74
2271	Korashina QFY	1	t	74
2272	Okrabot QFY	1	t	74
2273	K.Baxshi MFY	1	t	74
2274	Nodira MFY	1	t	74
2275	M.Tursunzoda MFY	1	t	74
2276	Ayridevol MFY	1	t	74
2277	Kizilcha QFY	1	t	74
2278	Kurgontosh QFY chegara xudud	1	t	74
2279	Okirtma QFY (chegara xudud)	1	t	74
2280	Torkapchugay MFY (chegara xudud)	1	t	74
2281	Beshkuton QFY	1	t	74
2282	Guroti MFY	1	t	74
2283	Oktosh QFY	1	t	74
2284	Chalika MFY	1	t	74
2285	Boshchorbog QFY	1	t	74
2286	Chashmamiron MFY	1	t	74
2287	Chilgaz MFY	1	t	74
2288	Sarchashma MFY	1	t	74
2289	Bozortepa QFY	1	t	74
2290	Obod MFY	1	t	74
2291	Obirovon QFY	1	t	74
2292	Okmachit MFY	1	t	74
2293	Duob QFY	1	t	74
2294	Okkishlok QFY	1	t	74
2295	Oybek MFY	1	t	74
2296	Koluvdor MFY	1	t	74
2297	Buston MFY	1	t	74
2298	Chim QFY	1	t	75
2299	Kushkapa MFY	1	t	75
2300	Gishtli MFY	1	t	75
2301	Gagarin MFY	1	t	75
2302	Kiziltepa QFY	1	t	75
2303	Kishlik MFY	1	t	75
2304	Bobirtepa MFY	1	t	75
2305	Tukboy QFY	1	t	75
2306	Berdoli MFY	1	t	75
2307	Boyburi MFY	1	t	75
2308	Jonbuzsoy QFY	1	t	75
2309	Jonbuz MFY	1	t	75
2310	Mexr MFY	1	t	75
2311	Kamay QFY	1	t	75
2312	Okguzar MFY	1	t	75
2313	Yertepa QFY	1	t	75
2314	Oynakul MFY	1	t	75
2315	Korabog QFY	1	t	75
2316	Balandchayla MFY	1	t	75
2317	Kovchin MFY	1	t	75
2318	Rabod QFY	1	t	75
2319	Uzun MFY	1	t	75
2320	Gulshan MFY	1	t	75
2321	Kaptarxona MFY	1	t	75
2322	Loykasoy QFY	1	t	75
2323	Badaxshon MFY	1	t	75
2324	Qoratepa QFY	1	t	75
2325	Mayda MFY	1	t	75
2326	Azlartepa MFY	1	t	75
2327	Kukbulok QFY	1	t	75
2328	Kattaura MFY	1	t	75
2329	Changak MFY	1	t	75
2330	Kizilkishlok MFY	1	t	75
2331	Urtadara MFY	1	t	75
2332	Mangit MFY	1	t	75
2333	Obod MFY	1	t	75
2334	Oybek MFY	1	t	75
2335	F.Xujaev MFY	1	t	75
2336	Samarkand MFY	1	t	75
2337	Korasuv MFY	1	t	75
2338	Uzbekiston MFY	1	t	75
2339	Ulugbek MFY	1	t	75
2340	Navoiy MFY	1	t	75
2341	Ibn-Sino MFY	1	t	75
2342	Olmazor MFY	1	t	75
2343	SarbozorMFY	1	t	75
2344	Bodomzor MFY	1	t	76
2345	Rovot MFY	1	t	76
2346	Navruz MFY	1	t	76
2347	Navbaxor MFY	1	t	76
2348	Xitoykenti MFY	1	t	76
2349	S. Raximov MFY	1	t	76
2350	Navoiy MFY	1	t	76
2351	Potron QFY	1	t	76
2352	Yukori Beshkent MFY	1	t	76
2353	Kuyi Beshkent MFY	1	t	76
2354	Kaxlak MFY	1	t	76
2355	Tallikuron QFY	1	t	76
2356	Chorbogboygundi MFY	1	t	76
2357	Kovchin QFY	1	t	76
2358	Shirkent MFY	1	t	76
2359	Yangi xayot MFY	1	t	76
2360	Turakul MFY	1	t	76
2361	Kojor QFY	1	t	76
2362	Lagandi MFY	1	t	76
2363	Kojor MFY	1	t	76
2364	Nukrobod QFY	1	t	76
2365	Mevazor MFY	1	t	76
2366	Yertepa MFY	1	t	76
2367	Nukrobod MFY	1	t	76
2368	Yertepa QFY	1	t	76
2369	Kuchkak MFY	1	t	76
2370	Batosh MFY	1	t	76
2371	Lagmon MFY	1	t	76
2372	Mirmiron MFY	1	t	76
2373	Pistakent MFY	1	t	76
2374	Niyozmudin MFY	1	t	76
2375	Kat QFY	1	t	76
2376	Taxtapul MFY	1	t	76
2377	Paxtazor MFY	1	t	76
2378	Dasht QFY	1	t	76
2379	Xonyon MFY	1	t	76
2380	Jumabozor MFY	1	t	76
2381	Shilvi MFY	1	t	76
2382	Koratepa QFY	1	t	76
2383	Fayzobod MFY	1	t	76
2384	Mustakillik MFY	1	t	76
2385	Saroy MFY	1	t	76
2386	Mangit MFY	1	t	76
2387	Xonobod QFY	1	t	76
2388	Xonobod MFY	1	t	76
2389	Xilol QFY	1	t	76
2390	Kerayit MFY	1	t	76
2391	Chulbuston QFY	1	t	76
2392	Charagil QFY	1	t	76
2393	Bogobod QFY	1	t	76
2394	Poshton QFY	1	t	76
2395	Shayxali shaxarcha	1	t	77
2396	A.Navoiy MFY	1	t	77
2397	Aral MFY	1	t	77
2398	Aralovul MFY	1	t	77
2399	Arabxona MFY	1	t	77
2400	Batosh MFY	1	t	77
2401	Beglar MFY	1	t	77
2402	Bogishamol MFY	1	t	77
2403	Buston MFY	1	t	77
2404	Gulshan MFY	1	t	77
2405	Gungon MFY	1	t	77
2406	Geolog MFY	1	t	77
2407	G.Gulom MFY	1	t	77
2408	Darvozatutak max	1	t	77
2409	Zaxokimaron max	1	t	77
2410	Zogza MFY	1	t	77
2411	Istiklol MFY	1	t	77
2412	Kavali MFY	1	t	77
2413	Kamandi MFY	1	t	77
2414	Karlikbogot max	1	t	77
2415	Karlikxona max	1	t	77
2416	Karshi MFY	1	t	77
2417	Kat MFY	1	t	77
2418	Kunchikar MFY	1	t	77
2419	Kurgoncha MFY	1	t	77
2420	K.Kurgoncha max	1	t	77
2421	Magzon MFY	1	t	77
2422	Maxallot MFY	1	t	77
2423	Maxtumkuli MFY	1	t	77
2424	Maxsimobod MFY	1	t	77
2425	Mustakillik max	1	t	77
2426	Navo MFY	1	t	77
2427	Navruz MFY	1	t	77
2428	Nasaf MFY	1	t	77
2429	Nuriston MFY	1	t	77
2430	Neftchi MFY	1	t	77
2431	Oydin MFY	1	t	77
2432	Otchopar MFY	1	t	77
2433	Paxtazor MFY	1	t	77
2434	Paxtazor-1 MFY	1	t	77
2435	Ravok MFY	1	t	77
2436	Roguzar MFY	1	t	77
2437	Samarkand MFY	1	t	77
2438	S.Raximov MFY	1	t	77
2439	Tabassum MFY	1	t	77
2440	Tabassum-1 MFY	1	t	77
2441	Temiryulchi MFY	1	t	77
2442	Usmon.Yusupov MFY	1	t	77
2443	F.Xujaev MFY	1	t	77
2444	Xaramjuy MFY	1	t	77
2445	Xontepa MFY	1	t	77
2446	Xudoyzod MFY	1	t	77
2447	Xujaxiyol MFY	1	t	77
2448	Chakar MFY	1	t	77
2449	Charmgar MFY	1	t	77
2450	Chulkuvar MFY	1	t	77
2451	Shayxali MFY	1	t	77
2452	Shodlik MFY	1	t	77
2453	Shurtangaz MFY	1	t	77
2454	Shoxbekat MFY	1	t	77
2455	Eskianxor MFY	1	t	77
2456	Yangiturmush MFY	1	t	77
2457	Muglon QFY	1	t	78
2458	Okkamish MFY	1	t	78
2459	Xujakasbi MFY	1	t	78
2460	Mustakilobod MFY	1	t	78
2461	Dustlik MFY	1	t	78
2462	Tinchlik MFY	1	t	78
2463	Koratepa MFY	1	t	78
2464	Yuksalish QFY	1	t	78
2465	G.Raxmonov MFY	1	t	78
2466	Kasbi MFY	1	t	78
2467	Jizza MFY	1	t	78
2468	Yangi Xayot QFY	1	t	78
2469	Fazli MFY	1	t	78
2470	Nazartepa MFY	1	t	78
2471	Galaba QFY	1	t	78
2472	Xujakarlik MFY	1	t	78
2473	Katagan QFY	1	t	78
2474	Okjangal MFY	1	t	78
2475	Soxibkor MFY	1	t	78
2476	Maymanok MFY	1	t	78
2477	Istiklol MFY	1	t	78
2478	Kamashi QFY	1	t	78
2479	Nurobod MFY	1	t	78
2480	Xujaki MFY	1	t	78
2481	Denov QFY	1	t	78
2482	Oktepa MFY	1	t	78
2483	Talliyulgun MFY	1	t	78
2484	Pandiron MFY	1	t	78
2485	Korakungirot QFY	1	t	78
2486	Shakarjuy MFY	1	t	78
2487	Talishbe MFY	1	t	78
2488	M.Ulugbek MFY	1	t	78
2489	Kungirot MFY	1	t	78
2490	Komilon QFY	1	t	78
2491	Mesit MFY	1	t	78
2492	Chulkuvar QFY	1	t	78
2493	Xo`jaxayron MFY	1	t	78
2494	Mushqoqi MFY	1	t	78
2495	Paxtaobod QFY	1	t	79
2496	Qaynarbuloq QFY	1	t	79
2497	Qatorbog` QFY	1	t	79
2498	Jilisuv QFY	1	t	79
2499	Sevaz QFY	1	t	79
2500	Palandara QFY	1	t	79
2501	Makrid QFY	1	t	79
2502	Quyioqboy QFY	1	t	79
2503	Bektemir QFY	1	t	79
2504	Tupchoq QFY	1	t	79
2505	Bog`bon QFY	1	t	79
2506	Beshterak QFY	1	t	79
2507	Kuxsor MFY	1	t	79
2508	Surum MFY	1	t	79
2509	Qaynar MFY	1	t	79
2510	Sariosie MFY	1	t	79
2511	Saroy MFY	1	t	79
2512	Bashir MFY	1	t	79
2513	Panji MFY	1	t	79
2514	Iskana MFY	1	t	79
2515	Beshqazoq MFY	1	t	79
2516	Vatkana MFY	1	t	79
2517	Shurobsoy MFY	1	t	79
2518	Yakkatut MFY	1	t	79
2519	Oeqchi MFY	1	t	79
2520	Hoji MFY	1	t	79
2521	Yo`ldosh shaxarcha MFY	1	t	79
2522	S.Raximov MFY	1	t	79
2523	Toshkent MFY	1	t	79
2524	H.Olimjon MFY	1	t	79
2525	Guliston MFY	1	t	79
2526	Ulug`bek MFY	1	t	79
2527	A.Qushchi MFY	1	t	79
2528	X.Dustligi MFY	1	t	79
2529	Xiromiy MFY	1	t	79
2530	Yangiobod MFY	1	t	79
2531	Charmgar MFY	1	t	79
2532	Sanam MFY	1	t	79
2533	Pulati QFY	1	t	80
2534	dustlik QFY	1	t	80
2535	Guvalak QFY	1	t	80
2536	Alachabob QFY	1	t	80
2537	Obidida QFY	1	t	80
2538	tinchlik QFY	1	t	80
2539	Koson QFY	1	t	80
2540	Bulmas QFY	1	t	80
2541	gulbog QFY	1	t	80
2542	Dustlik MFY	1	t	80
2543	Ravot MFY	1	t	80
2544	mesit MFY	1	t	80
2545	Regzor MFY	1	t	80
2546	Mugjagul MFY	1	t	80
2547	Lolazor MFY	1	t	80
2548	Nartichukur MFY	1	t	80
2549	jizzalik MFY	1	t	80
2550	Yangiobod MFY	1	t	80
2551	nartibaland MFY	1	t	80
2552	Kuybog MFY	1	t	80
2553	Istikbol MFY	1	t	80
2554	paxtazor MFY	1	t	80
2555	Saripul MFY	1	t	80
2556	Navbaxor MFY	1	t	80
2557	Oxunboboev MFY	1	t	80
2558	Arabxona MFY	1	t	80
2559	Mulali MFY	1	t	80
2560	Obod MFY	1	t	80
2561	Pistali MFY	1	t	80
2562	Sherbek MFY	1	t	80
2563	Boyterak MFY	1	t	80
2564	Kozokli MFY	1	t	80
2565	Urtaobron MFY	1	t	80
2566	Yakkasaroy MFY	1	t	80
2567	Chirokchi MFY	1	t	80
2568	Guliston MFY	1	t	80
2569	Boygundi MFY	1	t	80
2570	Beshkutan MFY	1	t	80
2571	navruz MFY	1	t	80
2572	Ushok tepa MFY	1	t	80
2573	Pudina MFY	1	t	80
2574	Surxon MFY	1	t	80
2575	Esaboy MFY	1	t	80
2576	shirintepa MFY	1	t	80
2577	darcha MFY	1	t	80
2578	Xujakuduk MFY	1	t	80
2579	Korabayir MFY	1	t	80
2580	Mudin MFY	1	t	80
2581	Etak MFY	1	t	80
2582	Maydayobu MFY	1	t	80
2583	Nekuz MFY	1	t	80
2584	Ayronchi MFY	1	t	80
2585	nixol MFY	1	t	80
2586	Raximsufi MFY	1	t	80
2587	Xalkobod MFY	1	t	80
2588	gala MFY	1	t	80
2589	Kaldaryo MFY	1	t	80
2590	nurafshon MFY	1	t	80
2591	kuyiobron MFY	1	t	80
2592	Uyrot MFY	1	t	80
2593	Mustakillik MFY	1	t	80
2594	xalima MFY	1	t	80
2595	Toshkuprik MFY	1	t	80
2596	Mirishkor QFY	1	t	81
2597	Jeynov QFY	1	t	81
2598	Guliston QFY	1	t	81
2599	Navbahor QFY	1	t	81
2600	Obod QFY	1	t	81
2601	Yangiobod QFY	1	t	81
2602	Avazcho`l QFY (chegara xudud)	1	t	81
2603	Pomuq QFY (chegara xudud)	1	t	81
2604	Chamanzor QFY	1	t	81
2605	Chandir QFY	1	t	81
2606	Vori QFY(chegara xudud)	1	t	81
2607	Gulshanbog` QFY (chegara xudud)	1	t	81
2608	Yangi Mirishkor MFY	1	t	81
2609	Obodon MFY	1	t	81
2610	Kalta MFY	1	t	81
2611	Qumbangi MFY	1	t	81
2612	Okmachit MFY	1	t	81
2613	O`zbekiston MFY	1	t	81
2614	Yangi Jeynov MFY	1	t	81
2615	Avvona MFY	1	t	81
2616	Anxo`y MFY	1	t	81
2617	Ayzabod MFY	1	t	81
2618	Kattapoy MFY	1	t	81
2619	Oltin boshoq MFY	1	t	81
2620	Bahoriston MFY	1	t	81
2621	Ignachi MFY	1	t	81
2622	Yangiqishloq MFY	1	t	81
2623	Malla MFY	1	t	81
2624	Shodlik MFY	1	t	81
2625	Zafar MFY	1	t	81
2626	Yangihayot MFY	1	t	81
2627	Istiqlol MFY	1	t	81
2628	Madaniyat MFY	1	t	81
2629	Guliston MFY	1	t	81
2630	Shirin MFY	1	t	81
2631	Maxtimquli MFY	1	t	81
2632	Konchilar MFY	1	t	82
2633	Yoshlik MFY	1	t	82
2634	Tong MFY	1	t	82
2635	Bobur MFY	1	t	82
2636	Dustlik MFY	1	t	82
2637	A.Navoiy MFY	1	t	82
2638	Geolog MFY	1	t	82
2639	Mash`al MFY	1	t	82
2640	Quruvchilar MFY	1	t	82
2641	Sariq QFY	1	t	82
2642	A.Temur MFY	1	t	82
2643	Muborak QFY	1	t	82
2644	Kuxnashaxar MFY	1	t	82
2645	Qora-qum QFY	1	t	82
2646	X.Ismoilov MFY	1	t	82
2647	Xitoy MFY	1	t	82
2648	S.Omonov MFY	1	t	82
2649	Qarliq QFY	1	t	82
2650	X.Karimov MFY	1	t	82
2651	K.Shoniyozov MFY	1	t	82
2652	Sardoba MFY	1	t	82
2653	baynalmilal MFY	1	t	83
2654	ulug`bek MFY	1	t	83
2655	Navbaxor MFY	1	t	83
2656	Paxtakor MFY	1	t	83
2657	Yuksalish MFY	1	t	83
2658	Paxtaobod MFY	1	t	83
2659	Nuriston shfy	1	t	83
2660	Navro`z QFY	1	t	83
2661	Guliston MFY	1	t	83
2662	Samarqand MFY	1	t	83
2663	Istiqbol MFY	1	t	83
2664	Yangiobod MFY	1	t	83
2665	Qirqquloch QFY (chegara xudud )	1	t	83
2666	Obod MFY(chegara xudud)	1	t	83
2667	Do`stlik MFY(chegara xudud)	1	t	83
2668	Obixayot MFY(chegara xudud)	1	t	83
2669	Tinchlik MFY(chegara xudud)	1	t	83
2670	Shirinobod QFY	1	t	83
2671	Paxtazor QFY	1	t	83
2672	Balxiyak QFY	1	t	83
2673	Nishon QFY	1	t	83
2674	oq oltin QFY	1	t	83
2675	oydin QFY	1	t	83
2676	A.Qodiriy MFY	1	t	83
2677	Kaptarli MFY	1	t	83
2678	Ibn sino MFY	1	t	83
2679	Kimyogar MFY	1	t	83
2680	Nurchi MFY	1	t	83
2681	Chiroqchi MFY	1	t	84
2682	Bog`ishamol MFY	1	t	84
2683	Kishmishtepa MFY	1	t	84
2684	O`zbekiston MFY	1	t	84
2685	Yangiobod MFY	1	t	84
2686	Choshtepa MFY	1	t	84
2687	A.Navoiy MFY	1	t	84
2688	Paxtaobod QFY	1	t	84
2689	Yangiqishloq MFY	1	t	84
2690	Olmazor QFY	1	t	84
2691	Chiljivut MFY	1	t	84
2692	Dam QFY	1	t	84
2693	Pakandi MFY	1	t	84
2694	Zarbdor MFY	1	t	84
2695	Uymovut QFY	1	t	84
2696	Xumo QFY	1	t	84
2697	Yangiobod MFY	1	t	84
2698	Ko`ktosh MFY	1	t	84
2699	Jar QFY	1	t	84
2700	Qizilchovra MFY	1	t	84
2701	Dodiq QFY	1	t	84
2702	Navro`z MFY	1	t	84
2703	Qaxramon QFY	1	t	84
2704	Buronjuz MFY	1	t	84
2705	Dursun MFY	1	t	84
2706	Uyshun QFY	1	t	84
2707	G`allachi MFY	1	t	84
2708	Oq oltin MFY	1	t	84
2709	Oq tosh MFY	1	t	84
2710	Mirzatup QFY	1	t	84
2711	Arabbandi MFY	1	t	84
2712	Chiyal QFY	1	t	84
2713	Uymovut MFY	1	t	84
2714	To`qmor MFY	1	t	84
2715	G`allakor MFY	1	t	84
2716	Qumdaryo QFY	1	t	84
2717	Suvliq MFY	1	t	84
2718	Annaro`z MFY	1	t	84
2719	Chuvilloq MFY	1	t	84
2720	Qalqama QFY	1	t	84
2721	Galabek MFY	1	t	84
2722	Langar QFY	1	t	84
2723	Quruqsoy MFY	1	t	84
2724	Kukdala QFY	1	t	84
2725	Soybo`yi MFY	1	t	84
2726	O`tamayli MFY	1	t	84
2727	Beglamish MFY	1	t	84
2728	Torjilg`a QFY	1	t	84
2729	Guliston MFY	1	t	84
2730	Eski anhor QFY	1	t	84
2731	Ayritom MFY	1	t	84
2732	Paxtalisoy MFY	1	t	84
2733	Yangihayot QFY	1	t	84
2734	Taloqtepa MFY	1	t	84
2735	Xarduri MFY	1	t	84
2736	Sho`rbozor MFY	1	t	84
2737	Chorvador QFY	1	t	84
2738	Qanotli MFY	1	t	84
2739	Sho`rquduq QFY	1	t	84
2740	Naymansaroy MFY	1	t	84
2741	Umakay MFY	1	t	84
2742	Chanbil MFY	1	t	84
2743	Qirg`iz MFY	1	t	84
2744	O`rda MFY	1	t	85
2745	Zingiron MFY	1	t	85
2746	Kulollik MFY	1	t	85
2747	Zargarlik MFY	1	t	85
2748	Qo`shxovuzMFY	1	t	85
2749	Qoziguzar MFY	1	t	85
2750	Sa`diy MFY	1	t	85
2751	X. Baxshi MFY	1	t	85
2752	Kunchiqar MFY	1	t	85
2753	Qushxona MFY	1	t	85
2754	Uychilik MFY	1	t	85
2755	NamozgoxMFY	1	t	85
2756	Oq saroy MFY	1	t	85
2757	XabarlikMFY	1	t	85
2758	Navro`zMFY	1	t	85
2759	SariosiyoMFY	1	t	85
2760	Cho`lponMFY	1	t	85
2761	G'ulom MFY	1	t	85
2762	Ipak Yuli MFY	1	t	85
2763	Paxtakor MFY	1	t	85
2764	Kesh MFY	1	t	85
2765	Do`stlik MFY	1	t	85
2766	Turon MFY	1	t	85
2767	Pillakashlik MFY	1	t	85
2768	Tutzor MFY	1	t	85
2769	TeparlikMFY	1	t	85
2770	Pisandi MFY	1	t	85
2771	KamolotMFY	1	t	85
2772	A.Jomiy MFY	1	t	85
2773	Ma`rifat MFY	1	t	85
2774	Sinabog` MFY	1	t	85
2775	Kunchiqar QFY	1	t	85
2776	Shamaton QFY	1	t	85
2777	O`zbekiston QFY	1	t	85
2778	Namaton QFY	1	t	85
2779	Duqchi QFY	1	t	85
2780	Muminobod QFY	1	t	85
2781	Shakarteri QFY	1	t	85
2782	Oqsuv QFY	1	t	85
2783	Qutchi QFY	1	t	85
2784	Tudamaydon QFY	1	t	85
2785	Miraki QFY	1	t	85
2786	Xisorak QFY (chegara xudud)	1	t	85
2787	Xitoy QFY	1	t	85
2788	Muminobod MFY	1	t	85
2789	Avazmalik MFY	1	t	85
2790	Uymovut MFY	1	t	85
2791	Xitoy	1	t	85
2792	G`elon (chegara xudud)	1	t	85
2793	Choshtepa MFY	1	t	85
2794	Chorshanbe MFY	1	t	85
2795	Yangiqishloq MFY	1	t	85
2796	K.Novqat MFY	1	t	85
2797	Paxtakor MFY	1	t	85
2798	Xujaxuroson MFY	1	t	85
2799	Urtaqurg`on MFY	1	t	85
2800	A.Temur MFY	1	t	85
2801	Tudamaydon MFY	1	t	85
2802	Xazara MFY	1	t	85
2803	Qutchi MFY	1	t	85
2804	Achchig`i MFY	1	t	85
2805	Saroy MFY	1	t	85
2806	Ommag`on MFY	1	t	85
2807	Chuqun MFY	1	t	85
2808	Furkat MFY	1	t	86
2809	Oxunboboev MFY	1	t	86
2810	Jambul MFY	1	t	86
2811	Chumich MFY	1	t	86
2812	Yangiobod MFY	1	t	86
2813	Xujailgor MFY	1	t	86
2814	Xamza MFY	1	t	86
2815	Jaychi MFY	1	t	86
2816	Aygirkul MFY	1	t	86
2817	Oktosh MFY	1	t	86
2818	Eski Yakkabog MFY	1	t	86
2819	Ibn Sino MFY	1	t	86
2820	Mustakillik MFY	1	t	86
2821	Esat MFY	1	t	86
2822	Kozok MFY	1	t	86
2823	Choydori MFY	1	t	86
2824	Jiyda MFY	1	t	86
2825	Uzun MFY	1	t	86
2826	Kishlik MFY	1	t	86
2827	Katagon MFY	1	t	86
2828	Kushchinor MFY	1	t	86
2829	Mevazor MFY	1	t	86
2830	Kayragoch MFY	1	t	86
2831	Uygur MFY	1	t	86
2832	Xonaka MFY	1	t	86
2833	Xiyobon MFY	1	t	86
2834	Darxon MFY	1	t	86
2835	Kushtegirmon MFY	1	t	86
2836	Urta MFY	1	t	86
2837	Ishkent MFY	1	t	86
2838	Samok MFY	1	t	86
2839	Tatar MFY	1	t	86
2840	Kenguzar MFY	1	t	86
2841	sandal MFY	1	t	86
2842	Sovukbulok MFY	1	t	86
2843	Madaniyat MFY	1	t	86
2844	beshugil MFY	1	t	86
2845	Daryo MFY	1	t	86
2846	Shar shar bogat MFY	1	t	86
2847	Alakuylak MFY	1	t	86
2848	Ulamji MFY	1	t	86
2849	Gozlik MFY	1	t	86
2850	Turon MFY	1	t	86
2851	Patakor MFY	1	t	86
2852	Tukboy	1	t	86
2853	Navruz MFY	1	t	86
2854	Zarapetyan MFY	1	t	87
2855	Shaxtyor MFY	1	t	87
2856	Oltin vodiy MFY	1	t	87
2857	Kuruvchi MFY	1	t	87
2858	Yoshlik MFY	1	t	87
2859	Tinchlik MFY	1	t	87
2860	Geolog MFY	1	t	87
2861	Baxor MFY	1	t	87
2862	Navruz MFY	1	t	87
2863	Yulduz MFY	1	t	87
2864	Yangi-Zarafshon	1	t	87
2865	Muruntau SHFY	1	t	87
2866	Daugiztau SHFY	1	t	87
2867	Yangi ariq QFY	1	t	88
2868	Varq MFY	1	t	88
2869	Kalovot MFY	1	t	88
2870	Arg`un MFY	1	t	88
2871	Yangi ariq MFY	1	t	88
2872	Talqoq MFY	1	t	88
2873	Katta machit MFY	1	t	88
2874	Uyrot QFY	1	t	88
2875	Uyrot MFY	1	t	88
2876	Ayronchi MFY	1	t	88
2877	Yangiobod MFY	1	t	88
2878	Xoncharbog` MFY	1	t	88
2879	Durman QFY	1	t	88
2880	Durman MFY	1	t	88
2881	Azamat MFY	1	t	88
2882	Qahramon MFY	1	t	88
2883	Malikrabot QFY	1	t	88
2884	Sardoba MFY	1	t	88
2885	Do`stlik MFY	1	t	88
2886	Xazora QFY	1	t	88
2887	Malik MFY	1	t	88
2888	Toshrabod MFY	1	t	88
2889	Degaron MFY	1	t	88
2890	Arabxona MFY	1	t	88
2891	Narpay QFY	1	t	88
2892	T. Gafurov MFY	1	t	88
2893	Navro`z MFY	1	t	88
2894	Paxtaobod MFY	1	t	88
2895	S. Umarov MFY	1	t	88
2896	Jaloir QFY	1	t	88
2897	Allon MFY	1	t	88
2898	Gurda MFY	1	t	88
2899	Yuqori bo`g` MFY	1	t	88
2900	Shibzon MFY	1	t	88
2901	Arabxona MFY	1	t	88
2902	Mirsaid Baxrom MFY	1	t	88
2903	Xisrav MFY	1	t	88
2904	Ko`hna Qurg`on MFY	1	t	88
2905	Gulobod MFY	1	t	88
2906	A.Navoiy MFY	1	t	88
2907	U. Yusupov MFY	1	t	88
2908	Farhod MFY	1	t	88
2909	Dehqon MFY	1	t	88
2910	Beshkent MFY	1	t	88
2911	Xuja-Xasan KFY	1	t	89
2912	Gamxur MFY	1	t	89
2913	Urtakurgon MFY	1	t	89
2914	Xasancha MFY	1	t	89
2915	Malikobod MFY	1	t	89
2916	Uzilishkent MFY	1	t	89
2917	Saroy MFY	1	t	89
2918	Kal`ayi-Azizon MFY	1	t	89
2919	Xujakurgon MFY	1	t	89
2920	Okrabot MFY	1	t	89
2921	Bobodugi MFY	1	t	89
2922	Gardiyon KFY	1	t	89
2923	Mayta MFY	1	t	89
2924	Balandgardiyon MFY	1	t	89
2925	Kulolon MFY	1	t	89
2926	Kusharta MFY	1	t	89
2927	Buston KFY	1	t	89
2928	Sufiyon MFY	1	t	89
2929	Kasriashurak MFY	1	t	89
2930	Bulakrabot MFY	1	t	89
2931	Xomrabot MFY	1	t	89
2932	Tavois MFY	1	t	89
2933	Goyibon MFY	1	t	89
2934	Gumbaz MFY	1	t	89
2935	Ok oltin KFY	1	t	89
2936	Miltikchi MFY	1	t	89
2937	Oksoch MFY	1	t	89
2938	Ayronchi MFY	1	t	89
2939	Vangozi KFY	1	t	89
2940	Vangozi MFY	1	t	89
2941	Toshmachit MFY	1	t	89
2942	Bashir MFY	1	t	89
2943	Madaniyat MFY	1	t	89
2944	Tojikon MFY	1	t	89
2945	Paxtaobod MFY	1	t	89
2946	Okmachit MFY	1	t	89
2947	Xafkoriyon MFY	1	t	89
2948	Zarmetan KFY	1	t	89
2949	Zarmetan MFY	1	t	89
2950	Rabot MFY	1	t	89
2951	Azizobod MFY	1	t	89
2952	Arabxona MFY	1	t	89
2953	Varozun MFY	1	t	89
2954	Sheyxon MFY	1	t	89
2955	Arabon KFY	1	t	89
2956	Xusbuddin MFY	1	t	89
2957	Demas MFY	1	t	89
2958	Konsurun MFY	1	t	89
2959	Gulbog MFY	1	t	89
2960	Yangi Xayot KFY	1	t	89
2961	Furkat MFY	1	t	89
2962	Gulzor MFY	1	t	89
2963	T.Xamid nomli	1	t	89
2964	Uzbekiston MFY	1	t	89
2965	F.Xujaev MFY	1	t	89
2966	Konimex SHFY	1	t	90
2967	Navruz MFY	1	t	90
2968	Dustlik MFY	1	t	90
2969	Birlik MFY	1	t	90
2970	Chordora KFY	1	t	90
2971	Shurtepa MFY	1	t	90
2972	U.Mirzaliev MFY	1	t	90
2973	Telemen MFY	1	t	90
2974	Yangiobod KFY	1	t	90
2975	M.Muratov MFY	1	t	90
2976	Oxunbobaev MFY	1	t	90
2977	Yangikazgan KFY	1	t	90
2978	Karakata KFY	1	t	90
2979	Sarjal OFY	1	t	90
2980	Baymurat OFY (chegaraga yaqin )	1	t	90
2981	Uchtepa OFY (chegaraga yaqin )	1	t	90
2982	"Keskanterak" KFY	1	t	91
2983	"Kushkochdi" MFY	1	t	91
2984	"Korajon" MFY	1	t	91
2985	Keskanterak MFY	1	t	91
2986	Yangi xayot MFY	1	t	91
2987	Kiziloy MFY	1	t	91
2988	Yangi yul KFY	1	t	91
2989	Uzbekiston MFY	1	t	91
2990	Gujbogtepa MFY	1	t	91
2991	O.Farmonov MFY	1	t	91
2992	Burkut MFY	1	t	91
2993	Mirzamumin MFY	1	t	91
2994	Mavlonbobo MFY	1	t	91
2995	Paxtakor MFY	1	t	91
2996	Beshrabod KFY	1	t	91
2997	Arabxona MFY	1	t	91
2998	Kuxron MFY	1	t	91
2999	Beshrabod MFY	1	t	91
3000	Yukori Beshrabot MFY	1	t	91
3001	Yangiobod MFY	1	t	91
3002	Ok oltin MFY	1	t	91
3003	Kelachi M.F.Y	1	t	91
3004	Olchin KFY	1	t	91
3005	ToshrabotMFY	1	t	91
3006	Kalkonota MFY	1	t	91
3007	Uchtut M.F.Y	1	t	91
3008	Mexnat M.F.Y	1	t	91
3009	Xalovat-tepa M.F.Y	1	t	91
3010	Yosh kuch MFY.	1	t	91
3011	Mirzo Ulug`bek	1	t	91
3012	Arabsaroy KFY	1	t	91
3013	Karvon MFY	1	t	91
3014	Sovungar MFY	1	t	91
3015	Arabxona MFY	1	t	91
3016	Saroy MFY	1	t	91
3017	Xashman MFY	1	t	91
3018	Vomitan MFY	1	t	91
3019	Armijon MFY	1	t	91
3020	Duldul MFY	1	t	91
3021	Turkiston QFY	1	t	91
3022	Kiziltepa MFY	1	t	91
3023	Yangi kuch MFY	1	t	91
3024	Yaltirabot M.F.Y	1	t	91
3025	Qizilrabot MFY	1	t	91
3026	Yangiqurg`on QFY	1	t	91
3027	Charvokguzar M.F.Y	1	t	91
3028	Navkar M.F.Y	1	t	91
3029	Sarbozor MFY	1	t	91
3030	Hayot MFY	1	t	92
3031	Istiqlol MFY	1	t	92
3032	Yangi ariq MFY	1	t	92
3033	Guliston MFY	1	t	92
3034	Binokor MFY	1	t	92
3035	Janubiy MFY	1	t	92
3036	Bunyodkor MFY	1	t	92
3037	O`zbekiston MFY	1	t	92
3038	G`alaba MFY	1	t	92
3039	Zarafshon MFY	1	t	92
3040	Yangiobod MFY	1	t	92
3041	Lochin MFY	1	t	92
3042	Me`mor MFY	1	t	92
3043	Muruvvat MFY	1	t	92
3044	Orzu MFY	1	t	92
3045	Umid MFY	1	t	92
3046	Baxor MFY	1	t	92
3047	Xumo MFY	1	t	92
3048	Do`stlik MFY	1	t	92
3049	Oltin Vodiy MFY	1	t	92
3050	Matonat MFY	1	t	92
3051	Gulzor MFY	1	t	92
3052	Turon MFY	1	t	92
3053	Mustaqillik MFY	1	t	92
3054	Ishonch MFY	1	t	92
3055	Vatan MFY	1	t	92
3056	Chinor MFY	1	t	92
3057	Kimyogar MFY	1	t	92
3058	Tinchlik MFY	1	t	92
3059	Xoncharvoq MFY	1	t	92
3060	Sayidato MFY	1	t	93
3061	Okmachit MFY	1	t	93
3062	Isiklol MFY	1	t	93
3063	Turko MFY	1	t	93
3064	A.Navoiy MFY	1	t	93
3065	Shaxriston MFY	1	t	93
3066	Mirishkor MFY	1	t	93
3067	G.Gulom MFY	1	t	93
3068	E.Sudur MFY	1	t	93
3069	Budik MFY	1	t	93
3070	Ibn Sino MFY	1	t	93
3071	Mustakillik MFY	1	t	93
3072	"Nurota 60 yil" MFY	1	t	93
3073	Nurota KFY	1	t	93
3074	Yangixayot MFY	1	t	93
3075	Amon Jalil MFY	1	t	93
3076	Chuya KFY	1	t	93
3077	Chuya MFY	1	t	93
3078	Kadok MFY	1	t	93
3079	Jarma MFY	1	t	93
3080	Gum KFY	1	t	93
3081	Yangiturmush MFY	1	t	93
3082	Suvlik MFY	1	t	93
3083	Istiklol MFY	1	t	93
3084	Dexibaland KFY	1	t	93
3085	Dexibaland MFY	1	t	93
3086	Avazsoy MFY	1	t	93
3087	Orasoy MFY	1	t	93
3088	G`ozgon KFY	1	t	93
3089	Guliston MFY	1	t	93
3090	Shayxon MFY	1	t	93
3091	Marmar-obod MFY	1	t	93
3092	Tumor MFY	1	t	93
3093	Kizilcha KFY	1	t	93
3094	Kizilcha MFY	1	t	93
3095	Sentob KFY	1	t	93
3096	Sentob MFY	1	t	93
3097	Temirkovuk MFY	1	t	93
3098	A.Zayniddinov MFY	1	t	93
3099	"Tomdibuloq" OFY	1	t	94
3100	"Aktau" OFY	1	t	94
3101	"Ayakquduq" OFY	1	t	94
3102	"Sukitti" OFY (chegarada joylashgan)	1	t	94
3103	"Kerizbulak" OFY (chegarada joylashgan)	1	t	94
3104	"Keregetau" OFY (chegarada joylashgan)	1	t	94
3105	"Shieli" OFY (chegarada joylashgan)	1	t	94
3106	Dustlik MFY	1	t	95
3107	Mustakillik MFY	1	t	95
3108	Aytim MFY	1	t	95
3109	Navoiy MFY	1	t	95
3110	Abay MFY	1	t	95
3111	Ko`kpatas MFY	1	t	95
3112	L.Murashimov OFY	1	t	95
3113	Bozdun OFY	1	t	95
3114	Mingbulok OFY	1	t	95
3115	Altintau OFY (chegaraga yaqin joylashgan)	1	t	95
3116	Uzunkuduk OFY	1	t	95
3117	Avangard OFY (chegaraga yaqin joylashgan)	1	t	95
3118	Yangirobod QFY	1	t	96
3119	Damariq MFY	1	t	96
3120	Samarqand MFY	1	t	96
3121	Paraxun MFY	1	t	96
3122	Navbahor MFY	1	t	96
3123	Chinobod MFY	1	t	96
3124	R.Maxmanov MFY	1	t	96
3125	Q.Razzoqov MFY	1	t	96
3126	Langar MFY	1	t	96
3127	Yangirobod MFY	1	t	96
3128	Oq-oltin QFY	1	t	96
3129	Bogishamol MFY	1	t	96
3130	P.Yorloqobov MFY	1	t	96
3131	Chechak-ota MFY	1	t	96
3132	Q.Gadoev MFY	1	t	96
3133	Mustaqillik MFY	1	t	96
3134	Bogchakolon QFY	1	t	96
3135	Navruz MFY	1	t	96
3136	Zarafshon MFY	1	t	96
3137	Bogchakolon MFY	1	t	96
3138	Tinchlik MFY	1	t	96
3139	Yangi qurulish MFY	1	t	96
3140	Qoracha QFY	1	t	96
3141	U.Boirov MFY	1	t	96
3142	M.Bobomurodov MFY	1	t	96
3143	A.Navoiy MFY	1	t	96
3144	Kattasoy MFY	1	t	96
3145	Quchchi MFY	1	t	96
3146	Changir MFY	1	t	96
3147	Qoracha MFY	1	t	96
3148	E.Layliev MFY	1	t	96
3149	Saroy MFY	1	t	96
3150	Zarbdor MFY	1	t	96
3151	Uzbekiston QFY	1	t	96
3152	Galabek MFY	1	t	96
3153	J.Hamroev MFY	1	t	96
3154	K.Arab MFY	1	t	96
3155	A.Temur MFY	1	t	96
3156	Qurg`oncha MFY	1	t	96
3157	T.Shirinov MFY	1	t	96
3158	Yangiyul QFY	1	t	96
3159	Paxtakor MFY	1	t	96
3160	Novja MFY	1	t	96
3161	Xujakulobod MFY	1	t	96
3162	Toshquloq MFY	1	t	96
3163	Ikrom Karvon MFY	1	t	96
3164	Istiqlol MFY	1	t	96
3165	Tamabaxrin MFY	1	t	96
3166	Polvon ota MFY	1	t	96
3167	Avoqli MFY	1	t	96
3168	Kuksaroy MFY	1	t	96
3169	Olchinobod QFY	1	t	96
3170	Oq-oltin MFY	1	t	96
3171	T.Narzullaev MFY	1	t	96
3172	Jaloyir MFY	1	t	96
3173	A.Jumanov MFY	1	t	96
3174	M.Ulug`bek MFY	1	t	96
3175	N.Uroqov MFY	1	t	96
3176	Madaniyat MFY	1	t	96
3177	Xonaqa QFY	1	t	96
3178	Yangi MFY	1	t	96
3179	Bug`irdoq MFY	1	t	96
3180	Jaloer MFY	1	t	96
3181	Uyshun MFY	1	t	96
3182	Chag`atoy MFY	1	t	96
3183	Tasmachi MFY	1	t	96
3184	Oltinobod MFY	1	t	96
3185	Mirdosh MFY	1	t	96
3186	Uchqora MFY	1	t	96
3187	Pulkan Shoir QFY	1	t	96
3188	Oltinsoy MFY	1	t	96
3189	Angidon MFY	1	t	96
3190	Sangijuman MFY	1	t	96
3191	Baxshijar MFY	1	t	96
3192	Oqtepa MFY	1	t	96
3193	Maydon MFY	1	t	96
3194	A.Dadaxonov MFY	1	t	97
3195	A.Jomiy MFY	1	t	97
3196	A.Navoiy MFY	1	t	97
3197	Beshketmon MFY	1	t	97
3198	Baxoriston MFY	1	t	97
3199	Bog kucha MFY	1	t	97
3200	Bog MFY	1	t	97
3201	Bogishamol MFY	1	t	97
3202	Bogishamol-1 MFY	1	t	97
3203	Bomraxa MFY	1	t	97
3204	Bulokboshi MFY	1	t	97
3205	Buston MFY	1	t	97
3206	Chak MFY	1	t	97
3207	Chindovul MFY	1	t	97
3208	Chindovul QFY	1	t	97
3209	Chorbog MFY	1	t	97
3210	Chungbosh MFY	1	t	97
3211	Chust kucha MFY	1	t	97
3212	Dam MFY	1	t	97
3213	Dilshod MFY	1	t	97
3214	Gul bog MFY	1	t	97
3215	Guliston-1 MFY	1	t	97
3216	Guliston-2 MFY	1	t	97
3217	Gulobod MFY	1	t	97
3218	Gurmiron MFY	1	t	97
3219	Guzar MFY	1	t	97
3220	Iftixor MFY	1	t	97
3221	Jar MFY	1	t	97
3222	Korasuv MFY	1	t	97
3223	Koson QFY	1	t	97
3224	Kozokovul MFY	1	t	97
3225	Kukumboy MFY	1	t	97
3226	M`azam MFY	1	t	97
3227	Navbaxor MFY	1	t	97
3228	Navbaxor-1 MFY	1	t	97
3229	Navruz MFY	1	t	97
3230	o`Ashirov MFY	1	t	97
3231	Obod MFY	1	t	97
3232	Obodon MFY	1	t	97
3233	Olmazor MFY	1	t	97
3234	Ozod MFY	1	t	97
3235	Panixon MFY	1	t	97
3236	Qorasuv QFY	1	t	97
3237	Ququmboy QFY	1	t	97
3238	Ravot MFY	1	t	97
3239	S.Sheroziy MFY	1	t	97
3240	Sadacha MFY	1	t	97
3241	Shayxon MFY	1	t	97
3242	Shirin QFY	1	t	97
3243	Soy buyi MFY	1	t	97
3244	Soycha MFY	1	t	97
3245	Tergachi QFY	1	t	97
3246	Tagijar MFY	1	t	97
3247	Takarang MFY	1	t	97
3248	Taxta kuprik MFY	1	t	97
3249	Uchkurgon MFY	1	t	97
3250	Urikzor MFY	1	t	97
3251	Urta kucha MFY	1	t	97
3252	Urta tukay MFY	1	t	97
3253	O`zbekiston MFY	1	t	97
3254	Uzunkishlok MFY	1	t	97
3255	Xonkurgon MFY	1	t	97
3256	Xuriyat MFY	1	t	97
3257	Xurriyat-1 MFY	1	t	97
3258	Yalama MFY	1	t	97
3259	Yangi shaxar MFY	1	t	97
3260	Yangi yul MFY	1	t	97
3261	Yoshlik MFY	1	t	97
3262	Yoshlik QFY	1	t	97
3263	Yu.Sh.M MFY	1	t	97
3264	Alami MFY	1	t	98
3265	Beserka MFY	1	t	98
3266	Baland Gurtepa MFY	1	t	98
3267	Birlashgan MFY	1	t	98
3268	Bozorboshi MFY	1	t	98
3269	Bo`ston qfy	1	t	98
3270	Chordona MFY	1	t	98
3271	Damkul MFY	1	t	98
3272	Dovduq QFY	1	t	98
3273	Farovon MFY	1	t	98
3274	Guliston MFY	1	t	98
3275	Gulobog` QFY	1	t	98
3276	Gurtepa QFY	1	t	98
3277	Ingichka MFY	1	t	98
3278	Jomashuy SHFY	1	t	98
3279	Kayrogochovul MFY	1	t	98
3280	Kichik jomashuy MFY	1	t	98
3281	Kirkchek MFY	1	t	98
3282	Kizilkum MFY	1	t	98
3283	Kolgandaryo	1	t	98
3284	Kora shaxar MFY	1	t	98
3285	Kozokovul MFY	1	t	98
3286	Kugolikul MFY	1	t	98
3287	Kurikobod MFY	1	t	98
3288	Kushkishlok MFY	1	t	98
3289	Mexnaobod MFY	1	t	98
3290	Mexnaobod QFY	1	t	98
3291	Madaniyat MFY	1	t	98
3292	Madiyarovul MFY	1	t	98
3293	Momoxon QFY	1	t	98
3294	Momoxon MFY	1	t	98
3295	Mulkobod MFY	1	t	98
3296	Mustakillik MFY	1	t	98
3297	Nayman MFY	1	t	98
3298	Oltinko`l QFY	1	t	98
3299	Oyb?k MFY	1	t	98
3300	Paxtakor MFY	1	t	98
3301	Serxarakat MFY	1	t	98
3302	Tegirmonboshi MFY	1	t	98
3303	Tollik MFY	1	t	98
3304	Tupsada MFY	1	t	98
3305	Urta kishlok MFY	1	t	98
3306	Uyurchi damkul MFY	1	t	98
3307	Uzgarish MFY	1	t	98
3308	Xayitobod MFY	1	t	98
3309	Yakkatol MFY	1	t	98
3310	Yangi Gulbog` MFY	1	t	98
3311	Yangiobod MFY	1	t	98
3312	Yoshlik MFY	1	t	98
3313	Anjirzor MFY	1	t	99
3314	Bektemir (jamoatchi) MFY	1	t	99
3315	Beshkapa MFY	1	t	99
3316	Bodomzor (jamoatchi) MFY	1	t	99
3317	Bog` kucha MFY	1	t	99
3318	Bog` mahalla MFY	1	t	99
3319	Bog`ishamol QFY	1	t	99
3320	Bozorboshi MFY	1	t	99
3321	Bo`ston MFY	1	t	99
3322	Chag`ir MFY	1	t	99
3323	Dasht MFY	1	t	99
3324	Elatan MFY	1	t	99
3325	Eshobod MFY	1	t	99
3326	G`alcha-1 MFY	1	t	99
3327	G`alcha-2 MFY	1	t	99
3328	G`alcha-3 MFY	1	t	99
3329	G`lcha QFY	1	t	99
3330	G`irvon QFY	1	t	99
3331	G`uldirov MFY	1	t	99
3332	I.Raxmatov QFY	1	t	99
3333	Irvadon -1 MFY	1	t	99
3334	Irvadon -2 MFY	1	t	99
3335	Irvadon -3 MFY	1	t	99
3336	Irvadon QFY	1	t	99
3337	Katta Toshbuloq MFY	1	t	99
3338	Kaykovus MFY	1	t	99
3339	Kichik qurama MFY	1	t	99
3340	Kichik Toshbuloq MFY	1	t	99
3341	Ko`l bo`yi MFY	1	t	99
3342	Ko`lqo`rg`on (jamoatchi) MFY	1	t	99
3343	Qumkurg`on QFY	1	t	99
3344	Kurmak MFY	1	t	99
3345	Mallahovuz MFY	1	t	99
3346	Mallaxovuz MFY	1	t	99
3347	Mirishkor QFY	1	t	99
3348	Mirishkor-1 MFY	1	t	99
3349	Mirishkor-2 MFY	1	t	99
3350	Mullakudung-1 MFY	1	t	99
3351	Mullakudung-2 MFY	1	t	99
3352	Ne`matjon MFY	1	t	99
3353	No`g`ayqo`rg`on MFY	1	t	99
3354	Olaxamak MFY	1	t	99
3355	Oq ?r MFY	1	t	99
3356	Oq buloq MFY	1	t	99
3357	Oq-Er MFY	1	t	99
3358	Orzu MFY	1	t	99
3359	Oxunboboev QFY	1	t	99
3360	O`lmas MFY	1	t	99
3361	O`rta G`irvon MFY	1	t	99
3362	O`rta Rovuston MFY	1	t	99
3363	Past Qiyot MFY	1	t	99
3364	Qirg`izqo`rg`on MFY	1	t	99
3365	Qorako`l MFY	1	t	99
3366	Qoratepa 1 MFY	1	t	99
3367	Qoratepa 2 MFY	1	t	99
3368	Qo`qon-qishloq MFY	1	t	99
3369	Qumqo`rg`on 1 MFY	1	t	99
3370	Qumqo`rg`on 2 MFY	1	t	99
3371	Qurama MFY	1	t	99
3372	Quyi G`irvon MFY	1	t	99
3373	Quyi Rovuston MFY	1	t	99
3374	Sherbuloq MFY	1	t	99
3375	Shamsiko`l MFY	1	t	99
3376	Shishaki MFY	1	t	99
3377	Sho`rqishloq MFY	1	t	99
3378	Sho`rqo`rg`on MFY	1	t	99
3379	Shurkishlok QFY	1	t	99
3380	Tepa MFY	1	t	99
3381	Tepa Qiyot MFY	1	t	99
3382	Tepakurg`on QFY	1	t	99
3383	Tepaqo`rg`on MFY	1	t	99
3384	Toshbuloq SHFY	1	t	99
3385	To`sar MFY	1	t	99
3386	Urganji MFY	1	t	99
3387	Uzbekiston QFY	1	t	99
3388	Xonobod QFY	1	t	99
3389	Xonobod MFY	1	t	99
3390	xo`jaqishloq-1 MFY	1	t	99
3391	xo`jaqishloq-2 MFY	1	t	99
3392	Yangi yo`l MFY	1	t	99
3393	Yuqori G`irvon MFY	1	t	99
3394	Yuqori Rovuston MFY	1	t	99
3395	A.Beruniy MFY	1	t	100
3396	A.Fazliy MFY	1	t	100
3397	Alpomish MFY	1	t	100
3398	Atangan Guzar MFY	1	t	100
3399	Avliyo Domla MFY	1	t	100
3400	Axsikent MFY	1	t	100
3401	B. Eshon MFY	1	t	100
3402	Baxor MFY	1	t	100
3403	Baynalminal MFY	1	t	100
3404	Bunyodkor MFY	1	t	100
3405	Buston MFY	1	t	100
3406	Chinor MFY	1	t	100
3407	Chorsu MFY	1	t	100
3408	Dambog` MFY	1	t	100
3409	Dashtbog` MFY	1	t	100
3410	Davlatobod MFY	1	t	100
3411	Do`stlik MFY	1	t	100
3412	Furqat MFY	1	t	100
3413	G`isht kuprik MFY	1	t	100
3414	Gulbog MFY	1	t	100
3415	Guliston MFY	1	t	100
3416	Gulpora MFY	1	t	100
3417	Gulshan MFY	1	t	100
3418	Guncha MFY	1	t	100
3419	Guzal MFY	1	t	100
3420	Isfarxon MFY	1	t	100
3421	Ishchi MFY	1	t	100
3422	Ishonch MFY	1	t	100
3423	Islomobod MFY	1	t	100
3424	Isok Chuyan MFY	1	t	100
3425	Istikbol MFY	1	t	100
3426	Istiqlol MFY	1	t	100
3427	Kurashxona MFY	1	t	100
3428	M.Maorif MFY	1	t	100
3429	Mexnatobod MFY	1	t	100
3430	Mexribonlik MFY	1	t	100
3431	Ma`naviyat MFY	1	t	100
3432	Ma`rifat MFY	1	t	100
3433	Madaniy MFY	1	t	100
3434	Majnuntol MFY	1	t	100
3435	Marg`ilon MFY	1	t	100
3436	Mashrab MFY	1	t	100
3437	Mingchinor MFY	1	t	100
3438	Mingterak MFY	1	t	100
3439	Must.5-yilligi MFY	1	t	100
3440	Mustakillik MFY	1	t	100
3441	Navbaxor MFY	1	t	100
3442	Navruz MFY	1	t	100
3443	Nurobod MFY	1	t	100
3444	Obixayot MFY	1	t	100
3445	Obod MFY	1	t	100
3446	Olvalizor MFY	1	t	100
3447	Oromgox MFY	1	t	100
3448	Ozod MFY	1	t	100
3449	O`zbekiston MFY	1	t	100
3450	Porloq MFY	1	t	100
3451	Qadamjoy MFY	1	t	100
3452	R.Mumin MFY	1	t	100
3453	S.Guzari MFY	1	t	100
3454	Sardoba MFY	1	t	100
3455	Shark tongi MFY	1	t	100
3456	Sharshara MFY	1	t	100
3457	Sixatgoh MFY	1	t	100
3458	Soxibkor MFY	1	t	100
3459	Sufizoda MFY	1	t	100
3460	Tinchlik MFY	1	t	100
3461	To`quvchi MFY	1	t	100
3462	Uch yog`och MFY	1	t	100
3463	Umid MFY	1	t	100
3464	Haqiqat MFY	1	t	100
3465	Xalklar dustligi MFY	1	t	100
3466	Xasti-Xizir MFY	1	t	100
3467	Yakkasada MFY	1	t	100
3468	Yangi asr MFY	1	t	100
3469	Yangi kurilish MFY	1	t	100
3470	Yangi rivojiya MFY	1	t	100
3471	Yaagi tong MFY	1	t	100
3472	Yangi xayot MFY	1	t	100
3473	Yangi yul MFY	1	t	100
3474	Zarafshon MFY	1	t	100
3475	Zarbdor MFY	1	t	100
3476	Zarkent MFY	1	t	100
3477	Ettiqashqa MFY	1	t	101
3478	A.Ikromov MFY	1	t	101
3479	Bobur MFY	1	t	101
3480	Boyovul MFY	1	t	101
3481	Buritepa MFY	1	t	101
3482	Buzulmas MFY	1	t	101
3483	Changitma MFY	1	t	101
3484	Dumar MFY	1	t	101
3485	Do`stlik MFY	1	t	101
3486	Furqat MFY	1	t	101
3487	Kemaboshi MFY	1	t	101
3488	Katta Ulmas MFY	1	t	101
3489	Katta Yaydok MFY	1	t	101
3490	Katta-Oktovlik MFY	1	t	101
3491	Kiziltov MFY	1	t	101
3492	Korateri MFY	1	t	101
3493	Kozokovul MFY	1	t	101
3494	Kukmozor MFY	1	t	101
3495	Qurama MFY	1	t	101
3496	Qurg`oncha MFY	1	t	101
3497	Kurg`ontepa QFY	1	t	101
3498	Kusharik MFY	1	t	101
3499	Kushchek MFY	1	t	101
3500	Kuyultepa MFY	1	t	101
3501	Margizor QFY	1	t	101
3502	Margizor MFY	1	t	101
3503	Mirsultonchek MFY	1	t	101
3504	Mustakillikning 20 yilligi	1	t	101
3505	Navoiy MFY	1	t	101
3506	Naymanobod MFY	1	t	101
3507	Norinkapa QFY	1	t	101
3508	Norinkapa MFY	1	t	101
3509	Otbozor MFY	1	t	101
3510	Pastki-chuja MFY	1	t	101
3511	Paxtaqishloq QFY	1	t	101
3512	Polvonkul MFY	1	t	101
3513	S.Raximov MFY	1	t	101
3514	Shoxidmozor MFY	1	t	101
3515	Shoxidon MFY	1	t	101
3516	Shurariq MFY	1	t	101
3517	Sirmok MFY	1	t	101
3518	Soy buyi MFY	1	t	101
3519	Suzakovul MFY	1	t	101
3520	Tegirmonboshi MFY	1	t	101
3521	Toshkin MFY	1	t	101
3522	Toshlok QFY	1	t	101
3523	Toshlok MFY	1	t	101
3524	Tuda QFY	1	t	101
3525	Tuda MFY	1	t	101
3526	Tulkin MFY	1	t	101
3527	Uchtepa QFY	1	t	101
3528	Uchtepa MFY	1	t	101
3529	O`zbekiston MFY	1	t	101
3530	Xajintoli MFY	1	t	101
3531	Xo`jaqurgoncha MFY	1	t	101
3532	Xo`jaobod QFY	1	t	101
3533	Xo`jaobod MFY	1	t	101
3534	Yangi tong MFY	1	t	101
3535	Yangi-Farg`ona MFY	1	t	101
3536	Yashik MFY	1	t	101
3537	Yaydok MFY	1	t	101
3538	Yuqori-Chuja MFY	1	t	101
3539	Zarbdor MFY	1	t	101
3540	A.Kaxxor MFY	1	t	102
3541	A.Navoyi MFY	1	t	102
3542	Birlashgan MFY	1	t	102
3543	Bog kucha MFY	1	t	102
3544	Bog MFY	1	t	102
3545	Buchiyon MFY	1	t	102
3546	Chartok MFY	1	t	102
3547	Chiganok MFY	1	t	102
3548	Chinor MFY	1	t	102
3549	Chodak boshi MFY	1	t	102
3550	Chodak QFY	1	t	102
3551	Chorkesar MFY	1	t	102
3552	Chorkesar SHFY	1	t	102
3553	Do`stlik MFY	1	t	102
3554	Do`stlik MFY	1	t	102
3555	Eski qishloq MFY	1	t	102
3556	Guliston MFY	1	t	102
3557	G`urumsaroy MFY	1	t	102
3558	Guzar MFY	1	t	102
3559	Imom ota MFY	1	t	102
3560	Iskovut MFY	1	t	102
3561	Ittifoq MFY	1	t	102
3562	Kenagas MFY	1	t	102
3563	Kalqurbon MFY	1	t	102
3564	Kandig`on MFY	1	t	102
3565	Qushminor MFY	1	t	102
3566	Qushtepa MFY	1	t	102
3567	M.Toshmatov QFY	1	t	102
3568	M.Umurzaqov QFY	1	t	102
3569	Madaniyat MFY	1	t	102
3570	Madanyat QFY	1	t	102
3571	Margizor-1 MFY	1	t	102
3572	Margizor-2 MFY	1	t	102
3573	Mayda millat MFY	1	t	102
3574	Maydon MFY	1	t	102
3575	Mozor MFY	1	t	102
3576	Muqimiy MFY	1	t	102
3577	Navbaxor SHFY	1	t	102
3578	Navboxor MFY	1	t	102
3579	Navruz MFY	1	t	102
3580	Nayman MFY	1	t	102
3581	Nayman QFY	1	t	102
3582	Olmozor MFY	1	t	102
3583	Oltinkon SHFY	1	t	102
3584	Oybek MFY	1	t	102
3585	Paxtakor MFY	1	t	102
3586	Paxtaobod QFY	1	t	102
3587	Pillakash MFY	1	t	102
3588	Pilol MFY	1	t	102
3589	Pop MFY	1	t	102
3590	Pop QFY	1	t	102
3591	Pungon QFY	1	t	102
3592	S.Ergashev MFY	1	t	102
3593	S.Raximov MFY	1	t	102
3594	Shayxon MFY	1	t	102
3595	Shomozor MFY	1	t	102
3596	Soxibkor MFY	1	t	102
3597	Temir yo`l usti. MFY	1	t	102
3598	Tepaqurg`on MFY	1	t	102
3599	Tinchlik MFY	1	t	102
3600	Toshqurg`on MFY	1	t	102
3601	Tuman-1 MFY	1	t	102
3602	U.Ikromov MFY	1	t	102
3603	uch uyli MFY	1	t	102
3604	Ultarma MFY	1	t	102
3605	Uyg`ur QFY	1	t	102
3606	Uyg`ursoy SHFY	1	t	102
3607	Uyg`ursoy SHFY	1	t	102
3608	Uyg`ur MFY	1	t	102
3609	O`zbekiston MFY	1	t	102
3610	Vodiy MFY	1	t	102
3611	H.Olimjon MFY	1	t	102
3612	Xalkobod-1 MFY	1	t	102
3613	Xalkobod-2 MFY	1	t	102
3614	Xalkobod-3 MFY	1	t	102
3615	Xalkobod-4 MFY	1	t	102
3616	Xalqabod SHFY	1	t	102
3617	Hamza MFY	1	t	102
3618	Hazrati bob MFY	1	t	102
3619	Xo`jaobod-1 MFY	1	t	102
3620	Xo`jaobod-2 MFY	1	t	102
3621	Xonobod urta MFY	1	t	102
3622	Yakkatut MFY	1	t	102
3623	Yangier MFY	1	t	102
3624	Yangi qishloq MFY	1	t	102
3625	Yangichek MFY	1	t	102
3626	Yangiobod MFY	1	t	102
3627	Yangihayot QFY	1	t	102
3628	Yu.Xotamov MFY	1	t	102
3629	Yuqori chodak boshi MFY	1	t	102
3630	Yukori qishloq MFY	1	t	102
3631	Elxon	1	t	103
3632	Er Masjid MFY	1	t	103
3633	Ettikon MFY	1	t	103
3634	Axsi QFY	1	t	103
3635	Axsi MFY	1	t	103
3636	Bekobod MFY	1	t	103
3637	Beruniy MFY	1	t	103
3638	Baxt	1	t	103
3639	Birlashgan MFY	1	t	103
3640	Bordimkul MFY	1	t	103
3641	Buramatut QFY	1	t	103
3642	Buramatut MFY	1	t	103
3643	Ch.Kuprik	1	t	103
3644	Chorbog` MFY	1	t	103
3645	Dasht MFY	1	t	103
3646	Dukat MFY	1	t	103
3647	Eshonchek MFY	1	t	103
3648	Fayziobod MFY	1	t	103
3649	Go`zal	1	t	103
3650	Guliston MFY	1	t	103
3651	Gulkishloq MFY	1	t	103
3652	Ibrat MFY	1	t	103
3653	Isvaxon MFY	1	t	103
3654	Kalvak MFY	1	t	103
3655	Qashqarguzar MFY	1	t	103
3656	Qatag`on MFY	1	t	103
3657	Qatag`on-Saroy QFY	1	t	103
3658	Katta Qo`rg`oncha MFY	1	t	103
3659	Katta-Qurama MFY	1	t	103
3660	Kichik Qo`rg`oncha MFY	1	t	103
3661	Kodirobod MFY	1	t	103
3662	Kujron MFY	1	t	103
3663	Kumidon MFY	1	t	103
3664	Qushqayrag`och MFY	1	t	103
3665	Kuymazor MFY	1	t	103
3666	Langarbobo MFY	1	t	103
3667	M.Kayumov MFY	1	t	103
3668	Majnuntol MFY	1	t	103
3669	Mozorkuxna MFY	1	t	103
3670	Obod MFY	1	t	103
3671	Obodon MFY	1	t	103
3672	Okava MFY	1	t	103
3673	Oktosh MFY	1	t	103
3674	Oktosh shfy	1	t	103
3675	Olchin MFY	1	t	103
3676	Ozod MFY	1	t	103
3677	Parasmon MFY	1	t	103
3678	Past Naymancha MFY	1	t	103
3679	Past-Mugultoy MFY	1	t	103
3680	Saroy MFY	1	t	103
3681	Sayram QFY	1	t	103
3682	Shark MFY	1	t	103
3683	Shaxand QFY	1	t	103
3684	Shovon MFY	1	t	103
3685	Shoxidon MFY	1	t	103
3686	Soxibkor MFY	1	t	103
3687	Soxilobod-1	1	t	103
3688	Soxilobod-2	1	t	103
3689	Temirqishloq MFY	1	t	103
3690	Tepa Naymancha MFY	1	t	103
3691	Toshkent MFY	1	t	103
3692	Toshlok MFY	1	t	103
3693	Turkiston MFY	1	t	103
3694	O`rda MFY	1	t	103
3695	O`rta qishloq MFY	1	t	103
3696	O`zbekiston MFY	1	t	103
3697	O`zbekiston MFY	1	t	103
3698	H.Olimjon	1	t	103
3699	Xolmatov QFY	1	t	103
3700	Xujand MFY	1	t	103
3701	Xujand QFY	1	t	103
3702	Yakkatom MFY	1	t	103
3703	Yangi shaxar MFY	1	t	103
3704	Yangi hayot MFY	1	t	103
3705	Yangiobod MFY	1	t	103
3706	Yangiobod MFY	1	t	103
3707	Yortepa QFY	1	t	103
3708	Yortepa kucha	1	t	103
3709	Yortepa MFY	1	t	103
3710	Yu.Mugultoy	1	t	103
3711	Zarbdor MFY	1	t	103
3712	A.Mo`minov MFY	1	t	104
3713	Beruniy MFY	1	t	104
3714	Balandariq MFY	1	t	104
3715	Birlashgan QFY	1	t	104
3716	Bog` ko`cha MFY	1	t	104
3717	Bog` MFY	1	t	104
3718	Boyagon MFY	1	t	104
3719	Bsston MFY	1	t	104
3720	Churtuk MFY	1	t	104
3721	Dexqon MFY	1	t	104
3722	Dexqonobod MFY	1	t	104
3723	Daxyakota MFY	1	t	104
3724	Do`stlik MFY	1	t	104
3725	Do`stlik MFY	1	t	104
3726	Ezgulik MFY	1	t	104
3727	Fayziobod MFY	1	t	104
3728	g`ayrat MFY	1	t	104
3729	g`ayrat QFY	1	t	104
3730	Gulbog` MFY	1	t	104
3731	Guliston MFY	1	t	104
3732	Gulzor MFY	1	t	104
3733	Gumbaz MFY	1	t	104
3734	Guzar MFY	1	t	104
3735	I.Ro`ziba?v MFY	1	t	104
3736	Islomobod MFY	1	t	104
3737	Ittifoq MFY	1	t	104
3738	Jiydakapa QFY	1	t	104
3739	Keskanyor MFY	1	t	104
3740	Mevazor MFY	1	t	104
3741	Mashad MFY	1	t	104
3742	Mashad QFY	1	t	104
3743	Mirzaravot MFY	1	t	104
3744	Muborak MFY	1	t	104
3745	Navoiy MFY	1	t	104
3746	Objuvoz MFY	1	t	104
3747	Obod MFY	1	t	104
3748	Olmurut MFY	1	t	104
3749	Oltitosh MFY	1	t	104
3750	Oqtosh MFY	1	t	104
3751	Oxunbobo?v MFY	1	t	104
3752	O`nxayat MFY	1	t	104
3753	O`nxayat SHFY	1	t	104
3754	o`urriyat MFY	1	t	104
3755	Pastguzar MFY	1	t	104
3756	Qashqar MFY	1	t	104
3757	Qaxramon MFY	1	t	104
3758	Qo`rg`oncha MFY	1	t	104
3759	Qumtepa MFY	1	t	104
3760	Quvurboshi MFY	1	t	104
3761	Rovot SHFY	1	t	104
3762	Sanoat MFY	1	t	104
3763	Sh.Xo`jamb?rdi?v MFY	1	t	104
3764	Shaftoli MFY	1	t	104
3765	Shifokor MFY	1	t	104
3766	Soku MFY	1	t	104
3767	Tepasaroy MFY	1	t	104
3768	Toshloq MFY	1	t	104
3769	Umid MFY	1	t	104
3770	Uychi QFY	1	t	104
3771	Uychi SHFY	1	t	104
3772	Xizirobod MFY	1	t	104
3773	Xojiobod MFY	1	t	104
3774	Xo`jaobod MFY	1	t	104
3775	Yakkatut MFY	1	t	104
3776	Yangi er MFY	1	t	104
3777	Yangi xayot MFY	1	t	104
3778	Yangich?k MFY	1	t	104
3779	Yorkatay MFY	1	t	104
3780	Yorkatay QFY	1	t	104
3781	Yorqo`rg`on QFY	1	t	104
3782	Yuksalish MFY	1	t	104
3783	Ziyokor MFY	1	t	104
3784	A.Rustamov MFY	1	t	105
3785	Atlas MFY	1	t	105
3786	Balandkuprik MFY	1	t	105
3787	Baxriobod MFY	1	t	105
3788	Baxt QFY	1	t	105
3789	Birlik MFY	1	t	105
3790	Bog kucha MFY	1	t	105
3791	Buston MFY	1	t	105
3792	Chek MFY	1	t	105
3793	Chorvador MFY	1	t	105
3794	Dexkonobod MFY	1	t	105
3795	Do`stlik MFY	1	t	105
3796	Do`stlik MFY	1	t	105
3797	Elatan MFY	1	t	105
3798	Eshontupi MFY	1	t	105
3799	Fargona MFY	1	t	105
3800	Farovon MFY	1	t	105
3801	Fayziobod MFY	1	t	105
3802	Guliston MFY	1	t	105
3803	Islomobod MFY	1	t	105
3804	Istiqlol MFY	1	t	105
3805	Kattach?k MFY	1	t	105
3806	Kattamogol MFY	1	t	105
3807	Kayki QFY	1	t	105
3808	Kozokovul MFY	1	t	105
3809	Kuchaboshi MFY	1	t	105
3810	Kugay QFY	1	t	105
3811	Kugay MFY	1	t	105
3812	Kugay Ulmas QFY	1	t	105
3813	Kugay Ulmas MFY	1	t	105
3814	Kumtugon MFY	1	t	105
3815	Kuprikboshi MFY	1	t	105
3816	Kurama MFY	1	t	105
3817	Kurgoncha MFY	1	t	105
3818	Mexnatobod MFY	1	t	105
3819	Madaniyat MFY	1	t	105
3820	Madaniyat MFY	1	t	105
3821	Namuna MFY	1	t	105
3822	Navoiy MFY	1	t	105
3823	Norin MFY	1	t	105
3824	Nurobod MFY	1	t	105
3825	Obod MFY	1	t	105
3826	Oktovlik MFY	1	t	105
3827	Ozod MFY	1	t	105
3828	Paxtachi MFY	1	t	105
3829	Sanoat MFY	1	t	105
3830	Sharxanchek MFY	1	t	105
3831	Sholdirama MFY	1	t	105
3832	Soxil MFY	1	t	105
3833	Tegirmon MFY	1	t	105
3834	Turkiston MFY	1	t	105
3835	Uchkuprik MFY	1	t	105
3836	Uchyogoch MFY	1	t	105
3837	Uchyogoch-2 MFY	1	t	105
3838	Uljatupi MFY	1	t	105
3839	Ulugbek MFY	1	t	105
3840	Urdabog MFY	1	t	105
3841	Uzunkucha MFY	1	t	105
3842	Xalfatupi MFY	1	t	105
3843	Xamza QFY	1	t	105
3844	Xamza MFY	1	t	105
3845	Yangier QFY	1	t	105
3846	Yangier MFY	1	t	105
3847	Yangiobod QFY	1	t	105
3848	Yangiobod MFY	1	t	105
3849	Yangixayot MFY	1	t	105
3850	Yangixayot MFY	1	t	105
3851	Yashik QFY	1	t	105
3852	Yashik MFY	1	t	105
3853	Yogdu MFY	1	t	105
3854	Yopisxon MFY	1	t	105
3855	Yorkinboychek MFY	1	t	105
3856	Yorkinxayot MFY	1	t	105
3857	Yoshlik MFY	1	t	105
3858	A.Navoiy MFY	1	t	106
3859	A.Navoiy MFY	1	t	106
3860	Alixon MFY	1	t	106
3861	Alixon QFY	1	t	106
3862	Arbag`ish MFY	1	t	106
3863	Beshkapa MFY	1	t	106
3864	Beshkapa MFY	1	t	106
3865	Beshtol MFY	1	t	106
3866	Baliq-ko`l MFY	1	t	106
3867	Bog` MFY	1	t	106
3868	Bog` MFY	1	t	106
3869	Bog`iston MFY	1	t	106
3870	Bog`iston QFY	1	t	106
3871	Bozorboshi MFY	1	t	106
3872	Bulon MFY	1	t	106
3873	Bulon MFY	1	t	106
3874	Chig`atoy MFY(Jamoatchilik)	1	t	106
3875	Chorsu MFY	1	t	106
3876	Dehqonobod MFY	1	t	106
3877	Damariq MFY	1	t	106
3878	Do`stlik MFY	1	t	106
3879	Do`stlik MFY	1	t	106
3880	Guldirov MFY	1	t	106
3881	Gulshan MFY	1	t	106
3882	Gulshan QFY	1	t	106
3883	Iftixor MFY	1	t	106
3884	Iftixor MFY	1	t	106
3885	Isroilov MFY	1	t	106
3886	Keskanyor MFY(Jamoatchi)	1	t	106
3887	Koroskon QFY	1	t	106
3888	Laskidon MFY	1	t	106
3889	Muchum QFY	1	t	106
3890	Mustaqillik MFY	1	t	106
3891	Namangan MFY	1	t	106
3892	Namangan MFY	1	t	106
3893	Navbaxor MFY	1	t	106
3894	Navbaxor MFY	1	t	106
3895	Navro`z MFY	1	t	106
3896	Oltitosh MFY(Jamoatchilik)	1	t	106
3897	Oqterak MFY	1	t	106
3898	Ora-ariq MFY	1	t	106
3899	Oromgox MFY	1	t	106
3900	Oromgox MFY	1	t	106
3901	Oyqiron MFY	1	t	106
3902	Oyqiron QFY	1	t	106
3903	O`rikzor MFY	1	t	106
3904	O`zbekiston MFY	1	t	106
3905	O`zbekiston MFY	1	t	106
3906	Peshqo`rg`on QFY	1	t	106
3907	Qorabog` MFY	1	t	106
3908	Qoramurt MFY	1	t	106
3909	S.Raximov MFY	1	t	106
3910	S.Raximov MFY	1	t	106
3911	Sarkor MFY	1	t	106
3912	Saroy MFY	1	t	106
3913	Saroy QFY	1	t	106
3914	Shodlik MFY(Jamoatchi)	1	t	106
3915	Soxibkor MFY(Jamoatchi)	1	t	106
3916	Soy MFY	1	t	106
3917	Soz-soy	1	t	106
3918	Tinchlik MFY	1	t	106
3919	Tinchlik MFY	1	t	106
3920	To`pqayrag`och MFY	1	t	106
3921	Turiq MFY	1	t	106
3922	Turkiston MFY	1	t	106
3923	Turkiston MFY	1	t	106
3924	Uzunko`cha MFY	1	t	106
3925	Hazratishox MFY	1	t	106
3926	Hazratishox QFY	1	t	106
3927	Yangiobod MFY	1	t	106
3928	Yangiobod MFY	1	t	106
3929	Yangiobod MFY	1	t	106
3930	Z.Diyor MFY	1	t	106
3931	Z.Diyor MFY	1	t	106
3932	Zangobod MFY	1	t	106
3933	Ettiqo`rg`on MFY	1	t	107
3934	Ariqbo`yi MFY	1	t	107
3935	Aqcha QFY	1	t	107
3936	Baliqchi MFY	1	t	107
3937	Baymoq MFY	1	t	107
3938	Baymoq QFY	1	t	107
3939	Bibiona MFY	1	t	107
3940	Birlik MFY	1	t	107
3941	Birlik MFY	1	t	107
3942	Bofanda MFY	1	t	107
3943	Bog`ieram MFY	1	t	107
3944	Bog`ormos MFY	1	t	107
3945	Bolo MFY	1	t	107
3946	Bozorboshi MFY	1	t	107
3947	Buloqboshi MFY	1	t	107
3948	Chustnon-Do`stlarobod MFY	1	t	107
3949	Dehqonobod MFY	1	t	107
3950	Dam MFY	1	t	107
3951	Do`stlik MFY	1	t	107
3952	Do`stlik MFY	1	t	107
3953	Do`zanda MFY	1	t	107
3954	G`ova QFY	1	t	107
3955	Guliston MFY	1	t	107
3956	Guliston MFY	1	t	107
3957	Guzar MFY	1	t	107
3958	Istiqlol MFY	1	t	107
3959	Kamarsada MFY	1	t	107
3960	Karkidon QFY	1	t	107
3961	Karnon QFY	1	t	107
3962	Ko`cha MFY	1	t	107
3963	Ko`ktosh MFY	1	t	107
3964	Laylakuya MFY	1	t	107
3965	Mehnatobod MFY	1	t	107
3966	Mashxad MFY	1	t	107
3967	Maydon MFY	1	t	107
3968	Mo`nchoqtepa MFY	1	t	107
3969	Mustaqillik MFY	1	t	107
3970	Navbahor MFY	1	t	107
3971	Navro`z MFY	1	t	107
3972	Og`asaroy MFY	1	t	107
3973	Og`asaroy QFY	1	t	107
3974	Olmos QFY	1	t	107
3975	Pansada MFY	1	t	107
3976	Pilol MFY	1	t	107
3977	Qaleai poyon MFY	1	t	107
3978	Qayirma MFY	1	t	107
3979	Qiziltepa MFY	1	t	107
3980	Qorakapa MFY	1	t	107
3981	Qoraqo`rg`on MFY	1	t	107
3982	Quyi Karnon MFY	1	t	107
3983	Rezaksoy MFY	1	t	107
3984	Serob MFY	1	t	107
3985	Sabzazor MFY	1	t	107
3986	Sadacha MFY	1	t	107
3987	Sarimsoqtepa MFY	1	t	107
3988	Sarqamish-Mirzaobod MFY	1	t	107
3989	Shoyon MFY	1	t	107
3990	Shoyon QFY	1	t	107
3991	Sho`rbuloq MFY	1	t	107
3992	Shurkent QFY	1	t	107
3993	Shuvar MFY	1	t	107
3994	Tepaqo`rg`on MFY	1	t	107
3995	Toshqo`rg`on MFY	1	t	107
3996	Toymas-1 MFY	1	t	107
3997	Toymas-2 MFY	1	t	107
3998	Varzigon MFY	1	t	107
3999	Varzik QFY	1	t	107
4000	Xisorak MFY	1	t	107
4001	Xisorak QFY	1	t	107
4002	Xo`jaobod MFY	1	t	107
4003	Yakkabuloq MFY	1	t	107
4004	Yangichak MFY	1	t	107
4005	Yangihayot MFY	1	t	107
4006	Yangiobod MFY	1	t	107
4007	Yorqishloq MFY	1	t	107
4008	Yuqori Karnon MFY	1	t	107
4009	Yuqori MFY	1	t	107
4010	Yutmos MFY	1	t	107
4011	Zarafshon MFY	1	t	107
4012	Zarafshon MFY	1	t	107
4013	Zvutqand MFY	1	t	107
4014	Bekobod QFY	1	t	108
4015	Beshbulok MFY	1	t	108
4016	Baraka MFY	1	t	108
4017	Baratov MFY	1	t	108
4018	Birlashgan K.FY	1	t	108
4019	Birlik MFY	1	t	108
4020	Bog MFY	1	t	108
4021	Bogiston MFY	1	t	108
4022	Bulokboshi MFY	1	t	108
4023	Buston MFY	1	t	108
4024	Chunbagish MFY	1	t	108
4025	Dexkonobod MFY	1	t	108
4026	Duldi MFY	1	t	108
4027	Dustlk MFY	1	t	108
4028	Furkat MFY	1	t	108
4029	Furkat MFY	1	t	108
4030	Gaiston MFY	1	t	108
4031	Gayrat MFY	1	t	108
4032	Gaznon MFY	1	t	108
4033	Govozon MFY	1	t	108
4034	Guliston MFY	1	t	108
4035	Guliston MFY	1	t	108
4036	Ibrat MFY	1	t	108
4037	Istiqlol QFY	1	t	108
4038	Kanda MFY	1	t	108
4039	Kandiyon MFY	1	t	108
4040	Kayroki MFY	1	t	108
4041	Kizilqiyoq MFY	1	t	108
4042	Kizilyozi MFY	1	t	108
4043	Korapolvon QFY	1	t	108
4044	Korapolvon MFY	1	t	108
4045	Korayontok MFY	1	t	108
4046	Kukyor MFY	1	t	108
4047	Kurik MFY	1	t	108
4048	Kutlug`tol MFY	1	t	108
4049	Kuyikorapolvon MFY	1	t	108
4050	Madaniyat MFY	1	t	108
4051	Madaniyat MFY	1	t	108
4052	Mamay MFY	1	t	108
4053	Mugol MFY	1	t	108
4054	Nanay QFY	1	t	108
4055	Navkent QFY	1	t	108
4056	Navkent MFY	1	t	108
4057	Navruzobod QFY	1	t	108
4058	Nov MFY	1	t	108
4059	Oksuvgovozon MFY	1	t	108
4060	Oktepa MFY	1	t	108
4061	Oktom MFY	1	t	108
4062	Olmazor MFY	1	t	108
4063	Oxunbobo?v MFY	1	t	108
4064	Poromon QFY	1	t	108
4065	Poromon MFY	1	t	108
4066	Radivon MFY	1	t	108
4067	Rovot MFY	1	t	108
4068	Rovut MFY	1	t	108
4069	Salmon MFY	1	t	108
4070	Shark Yulduzi QFY	1	t	108
4071	Soxibkor MFY	1	t	108
4072	Soxil MFY	1	t	108
4073	Soy buyi MFY	1	t	108
4074	Sutli bulok MFY	1	t	108
4075	Tinchlik MFY	1	t	108
4076	Tinchlik MFY	1	t	108
4077	Toshkent MFY	1	t	108
4078	Tuman MFY	1	t	108
4079	Urta MFY	1	t	108
4080	Xadikent MFY	1	t	108
4081	Xakikat MFY	1	t	108
4082	Xujashurkent MFY	1	t	108
4083	Xurriyat MFY	1	t	108
4084	Yangi bogiston MFY	1	t	108
4085	Yangiobod MFY	1	t	108
4086	Yangiobod MFY	1	t	108
4087	Yorilgan MFY	1	t	108
4088	Yukori Korayontok MFY	1	t	108
4089	Yukorinavkent MFY	1	t	108
4090	Yumalok tepa MFY	1	t	108
4091	Zarbdor QFY	1	t	108
4092	Zarbdor MFY	1	t	108
4093	Zarkent QFY	1	t	108
4094	A.Temur MFY	1	t	109
4095	Avliyo Parpi	1	t	109
4096	Beshkuvi MFY	1	t	109
4097	Beshqo`ton MFY	1	t	109
4098	Beshqo`ton QFY	1	t	109
4099	Bog`bon MFY	1	t	109
4100	Bo`dana MFY	1	t	109
4101	Bulung`ur MFY	1	t	109
4102	Bulung`ur-ariq MFY	1	t	109
4103	Changal MFY	1	t	109
4104	Changal-1 MFY	1	t	109
4105	Changalpayon MFY	1	t	109
4106	Chorbog` MFY	1	t	109
4107	Do`stlik MFY	1	t	109
4108	Erganakli MFY	1	t	109
4109	Esonturdi MFY	1	t	109
4110	FYo`ldosh QFY	1	t	109
4111	G`o`bdin MFY	1	t	109
4112	Guliston MFY	1	t	109
4113	Gulobod MFY	1	t	109
4114	Gulzor MFY	1	t	109
4115	Isori O`roqli	1	t	109
4116	Istiqlol MFY	1	t	109
4117	Kaptarxona MFY	1	t	109
4118	Kattqishloq MFY	1	t	109
4119	Kattqishloq-1 MFY	1	t	109
4120	Kichikkildon MFY	1	t	109
4121	Kildon MFY	1	t	109
4122	Kildon QFY	1	t	109
4123	Kulchabiy QFY	1	t	109
4124	Mehrjon MFY	1	t	109
4125	Mextar MFY	1	t	109
4126	Mingchinor MFY	1	t	109
4127	Mingtepa MFY	1	t	109
4128	Mo`g`ol MFY	1	t	109
4129	Nebo`sa MFY	1	t	109
4130	Navbahor MFY	1	t	109
4131	Navoiy QFY	1	t	109
4132	Niyozmat MFY	1	t	109
4133	Nurli yo`l MFY	1	t	109
4134	Olmazor MFY	1	t	109
4135	Oqtepa MFY	1	t	109
4136	Oqtosh MFY	1	t	109
4137	O`roqli MFY	1	t	109
4138	O`rtabuloq QFY	1	t	109
4139	Qirqshodi MFY	1	t	109
4140	Qo`ng`irot MFY	1	t	109
4141	Samarqand MFY	1	t	109
4142	Sarpichoq MFY	1	t	109
4143	Sayiltepa MFY	1	t	109
4144	Soxibkor MFY	1	t	109
4145	Soxibkor QFY	1	t	109
4146	Suluqo`rg`on MFY	1	t	109
4147	Ulug`bek MFY	1	t	109
4148	Xo`jabachcha MFY	1	t	109
4149	Xo`jamazgil MFY	1	t	109
4150	Yangiariq MFY	1	t	109
4151	Yangiobod MFY	1	t	109
4152	Yangiqo`rg`on MFY	1	t	109
4153	Zarafshon MFY	1	t	109
4154	A.Navoiy MFY	1	t	110
4155	A.Qurbonov MFY	1	t	110
4156	Beshbola MFY	1	t	110
4157	Dehqonobod QFY	1	t	110
4158	Dexqonobod MFY	1	t	110
4159	Eski Jomboy MFY	1	t	110
4160	Eski Jomboy QFY	1	t	110
4161	G`azira MFY	1	t	110
4162	Guliston MFY	1	t	110
4163	Juriyat MFY	1	t	110
4164	Juriyat QFY	1	t	110
4165	Katta qishloq MFY	1	t	110
4166	Kukgumbaz MFY	1	t	110
4167	Nayman MFY	1	t	110
4168	Naymantepa MFY	1	t	110
4169	Nazar MFY	1	t	110
4170	Nogaxon MFY	1	t	110
4171	No`sh MFY	1	t	110
4172	Olmazor MFY	1	t	110
4173	Polvonariq MFY	1	t	110
4174	Qang`li MFY	1	t	110
4175	Qang`li QFY	1	t	110
4176	Qoramo`yin MFY	1	t	110
4177	Qoramo`yin QFY	1	t	110
4178	Qo`lbosti MFY	1	t	110
4179	Qo`ng`irot MFY	1	t	110
4180	Qo`ng`irot QFY	1	t	110
4181	Qo`rg`onsalomon MFY	1	t	110
4182	Quduqli MFY	1	t	110
4183	Samarqand MFY	1	t	110
4184	Sarichashma MFY	1	t	110
4185	Sariqipchoq MFY	1	t	110
4186	Saroy MFY	1	t	110
4187	Sherqo`rg`on MFY	1	t	110
4188	Sherqo`rg`on QFY	1	t	110
4189	Shirinkent MFY	1	t	110
4190	Shodlik MFY	1	t	110
4191	So`xmon MFY	1	t	110
4192	Taldirazzoq MFY	1	t	110
4193	Toshkent MFY	1	t	110
4194	To`qqizboy MFY	1	t	110
4195	Tut MFY	1	t	110
4196	Xitoypayon MFY	1	t	110
4197	Xolvoyi MFY	1	t	110
4198	Xolvoyi QFY	1	t	110
4199	Yangi hayot MFY	1	t	110
4200	Zarafshon MFY	1	t	110
4201	Arabxona MFY	1	t	111
4202	Azamat MFY	1	t	111
4203	Azamat QFY	1	t	111
4204	Beshbola MFY	1	t	111
4205	Beshkapa MFY	1	t	111
4206	Baxrin MFY	1	t	111
4207	Bokon MFY	1	t	111
4208	Borlos MFY	1	t	111
4209	Boylata MFY	1	t	111
4210	Boytubi MFY	1	t	111
4211	Buronxuja MFY	1	t	111
4212	Buston MFY	1	t	111
4213	Chagatoy MFY	1	t	111
4214	Chakar MFY	1	t	111
4215	Chayjavul MFY	1	t	111
4216	Chimkurg`on MFY	1	t	111
4217	Chinortepa MFY	1	t	111
4218	Chordara QFY	1	t	111
4219	Dehqonobod MFY	1	t	111
4220	Damarik MFY	1	t	111
4221	Do`stlik MFY	1	t	111
4222	Fayziobod QFY	1	t	111
4223	g` G`ulom MFY	1	t	111
4224	Ishtixon MFY	1	t	111
4225	J.Mahmudov MFY	1	t	111
4226	K. Qarshiev MFY	1	t	111
4227	Qatag`on MFY	1	t	111
4228	Kattakang`li MFY	1	t	111
4229	Qayirma MFY	1	t	111
4230	Qirqyigit MFY	1	t	111
4231	Qiyot MFY	1	t	111
4232	Qoraqishloq MFY	1	t	111
4233	Kubay MFY	1	t	111
4234	Kuktepa MFY	1	t	111
4235	Kuljamol MFY	1	t	111
4236	Qung`irot MFY	1	t	111
4237	Kurilish MFY	1	t	111
4238	Kurli QFY	1	t	111
4239	Kutarma MFY	1	t	111
4240	Minglar MFY	1	t	111
4241	Mirishkor MFY	1	t	111
4242	Mirzakul MFY	1	t	111
4243	Mitan SHFY	1	t	111
4244	Moxpar MFY	1	t	111
4245	Namuna MFY	1	t	111
4246	Odil MFY	1	t	111
4247	Orlot MFY	1	t	111
4248	O`zbekiston MFY	1	t	111
4249	Qoraqo`yli MFY	1	t	111
4250	Ravot MFY	1	t	111
4251	Ravot QFY	1	t	111
4252	Safoxo`ja MFY	1	t	111
4253	Sh`yxlar MFY	1	t	111
4254	Shayxlarkent MFY	1	t	111
4255	Shayxislom MFY	1	t	111
4256	Sugat MFY	1	t	111
4257	Tallak MFY	1	t	111
4258	Tinibek MFY	1	t	111
4259	Toytuyok MFY	1	t	111
4260	Tupor MFY	1	t	111
4261	Urtakishlok QFY	1	t	111
4262	O`zbekqo`rg`on MFY	1	t	111
4263	Haqiqat QFY	1	t	111
4264	Xalqobod MFY	1	t	111
4265	Xalqobod QFY	1	t	111
4266	Xazar bobo MFY	1	t	111
4267	Xonaqa MFY	1	t	111
4268	Yangi Ravot MFY	1	t	111
4269	Yangikent MFY	1	t	111
4270	Yugontepa MFY	1	t	111
4271	Zarband MFY	1	t	111
4272	Zarband QFY	1	t	111
4273	Alijon MFY	1	t	112
4274	Andoksoy MFY	1	t	112
4275	Balandchordara MFY	1	t	112
4276	Balandravot MFY	1	t	112
4277	Bog`ot MFY	1	t	112
4278	Burgansoy MFY	1	t	112
4279	Chagatoy MFY	1	t	112
4280	Charog`on MFY	1	t	112
4281	Chiganok MFY	1	t	112
4282	Chuyanchi MFY	1	t	112
4283	Durbesh QFY	1	t	112
4284	Do`stlik MFY	1	t	112
4285	Do`stlik MFY	1	t	112
4286	Fayzikent MFY	1	t	112
4287	Girdikurgon QFY	1	t	112
4288	Javlon MFY	1	t	112
4289	Jizmonsoy MFY	1	t	112
4290	Jonkil MFY	1	t	112
4291	Jumaboy QFY	1	t	112
4292	Jumaboy MFY	1	t	112
4293	Kadan MFY	1	t	112
4294	Karadaryo MFY	1	t	112
4295	Kattakurpa QFY	1	t	112
4296	Kattakurpa MFY	1	t	112
4297	Kattaming QFY	1	t	112
4298	Kattaming MFY	1	t	112
4299	Kichikmundiyon QFY	1	t	112
4300	Qirg`iz MFY	1	t	112
4301	Qiyot MFY	1	t	112
4302	Koksoy MFY	1	t	112
4303	Korakulcha MFY	1	t	112
4304	Kumok MFY	1	t	112
4305	Kumushkent MFY	1	t	112
4306	Kumushkirgok MFY	1	t	112
4307	Kushbegi MFY	1	t	112
4308	Kushkuton MFY	1	t	112
4309	Qushtepa QFY	1	t	112
4310	Qushtepa MFY	1	t	112
4311	Qushxovuz MFY	1	t	112
4312	M.Ulug`bek MFY	1	t	112
4313	Melixo`ja MFY	1	t	112
4314	Madrasa MFY	1	t	112
4315	Moybuloq MFY	1	t	112
4316	Moybuloq QFY	1	t	112
4317	Mullakurpa MFY	1	t	112
4318	Mullatog`ay MFY	1	t	112
4319	Muminxo`ja MFY	1	t	112
4320	Mundiyon MFY	1	t	112
4321	Murodkosimov MFY	1	t	112
4322	Navbaxor MFY	1	t	112
4323	Navoiy MFY	1	t	112
4324	Nayman MFY	1	t	112
4325	Nisbat MFY	1	t	112
4326	Nomozpolvon MFY	1	t	112
4327	Olmazor MFY	1	t	112
4328	Omonboy QFY	1	t	112
4329	Omonboykuprik MFY	1	t	112
4330	Omonkalxat MFY	1	t	112
4331	Oyjon MFY	1	t	112
4332	Payshanba SHFY	1	t	112
4333	Polvontepa MFY	1	t	112
4334	Sebuston MFY	1	t	112
4335	Saraykurg`on MFY	1	t	112
4336	Saroykur`gon QFY	1	t	112
4337	Shurak MFY	1	t	112
4338	Suv hovuzi SHFY	1	t	112
4339	Tarnov MFY	1	t	112
4340	Tavaron MFY	1	t	112
4341	Uyshun MFY	1	t	112
4342	Valijon MFY	1	t	112
4343	Vayrot MFY	1	t	112
4344	Yakkabog` MFY	1	t	112
4345	Yangi hayot MFY	1	t	112
4346	Yangiqiyot MFY	1	t	112
4347	Yangiqo`rg`oncha MFY	1	t	112
4348	Yangiobod MFY	1	t	112
4349	Yangirabot MFY	1	t	112
4350	Yaniqo`rg`oncha QFY	1	t	112
4351	Yodgorxo`ja MFY	1	t	112
4352	Yonboshsoy MFY	1	t	112
4353	Yovi MFY	1	t	112
4354	Zarqo`rg`on MFY	1	t	112
4355	Er machit MFY	1	t	113
4356	Abdulla Qahhor MFY	1	t	113
4357	Alisher Navoiy MFY	1	t	113
4358	Amir Temur MFY	1	t	113
4359	Arabxona MFY	1	t	113
4360	Bahoriston MFY	1	t	113
4361	Baland chordara MFY	1	t	113
4362	Chordara MFY	1	t	113
4363	Do`stlik MFY	1	t	113
4364	G`arib Machit MFY	1	t	113
4365	Ingichka SHFY	1	t	113
4366	Islom Shoir MFY	1	t	113
4367	Kuchaxur MFY	1	t	113
4368	Kunjipay MFY	1	t	113
4369	Meli Razzoqov MFY	1	t	113
4370	Miyonkol MFY	1	t	113
4371	Muxammad Daminov MFY	1	t	113
4372	Narzullo Tog`aev MFY	1	t	113
4373	Navbahor MFY	1	t	113
4374	Nizomiddin Zokirov MFY	1	t	113
4375	Noqis MFY	1	t	113
4376	Nurobod MFY	1	t	113
4377	Ochildi Murod Miriy MFY	1	t	113
4378	Oq oltin MFY	1	t	113
4379	O`rikzor MFY	1	t	113
4380	Qorirovot MFY	1	t	113
4381	Rahima Islomova MFY	1	t	113
4382	Safar Xushnazarov MFY	1	t	113
4383	Sarmazor MFY	1	t	113
4384	Siplon MFY	1	t	113
4385	So`fi Olloyor MFY	1	t	113
4386	Umar Norov MFY	1	t	113
4387	Usmon Nosir MFY	1	t	113
4388	Xaydarchaman MFY	1	t	113
4389	Xojikurbon MFY	1	t	113
4390	Zarifobod MFY	1	t	113
4391	Boypurushli MFY	1	t	114
4392	Boyto`p MFY	1	t	114
4393	Bozorjoy MFY	1	t	114
4394	Bulok MFY	1	t	114
4395	Bulokboshi MFY	1	t	114
4396	Chinok MFY	1	t	114
4397	Chorlok MFY	1	t	114
4398	Do`stlik MFY	1	t	114
4399	Jonbulok MFY	1	t	114
4400	Jush QFY	1	t	114
4401	Jush ota MFY	1	t	114
4402	Katta Okmachit MFY	1	t	114
4403	Kiykim MFY	1	t	114
4404	Koratosh MFY	1	t	114
4405	Kovunchi MFY	1	t	114
4406	Kurgon MFY	1	t	114
4407	Kurolos MFY	1	t	114
4408	Kushrabot QFY	1	t	114
4409	Kushrabot MFY	1	t	114
4410	Kushtamgoli MFY	1	t	114
4411	Kuvkalla MFY	1	t	114
4412	Mayintepa MFY	1	t	114
4413	Minishkor MFY	1	t	114
4414	Mustakillik MFY	1	t	114
4415	Novkat MFY	1	t	114
4416	Okchopsoy MFY	1	t	114
4417	Okmachit MFY	1	t	114
4418	Oktepa QFY	1	t	114
4419	Ozod MFY	1	t	114
4420	Pangat MFY	1	t	114
4421	Pichot QFY	1	t	114
4422	Pichot MFY	1	t	114
4423	Shovo MFY	1	t	114
4424	Shovona	1	t	114
4425	Soxibkor QFY	1	t	114
4426	Tegirmonovul MFY	1	t	114
4427	Toz MFY	1	t	114
4428	Urganji QFY	1	t	114
4429	Urganji MFY	1	t	114
4430	Urtasoy MFY	1	t	114
4431	Xonnazar MFY	1	t	114
4432	Yangikishlok MFY	1	t	114
4433	Yu.Saroy MFY	1	t	114
4434	Yukori Jush MFY	1	t	114
4435	Zarkent MFY	1	t	114
4436	Zarmitan QFY	1	t	114
4437	A. Navoiy MFY	1	t	115
4438	A.Navoiy MFY	1	t	115
4439	A.Rasulov MFY	1	t	115
4440	A.Temur MFY	1	t	115
4441	A.Xaknazarov MFY	1	t	115
4442	Arabxona MFY	1	t	115
4443	Beklar MFY	1	t	115
4444	Birlik MFY	1	t	115
4445	Bolgali MFY	1	t	115
4446	Shakar QFY	1	t	115
4447	Charxin MFY	1	t	115
4448	Chaykal MFY	1	t	115
4449	Chorbog` MFY	1	t	115
4450	Dedan MFY	1	t	115
4451	Do`stlik MFY	1	t	115
4452	Guliston MFY	1	t	115
4453	I.Shoir QFY	1	t	115
4454	I.Shoir MFY	1	t	115
4455	Islomobod MFY	1	t	115
4456	Istiqlol MFY	1	t	115
4457	Iymon MFY	1	t	115
4458	Kadim QFY	1	t	115
4459	Korakul QFY	1	t	115
4460	Korasiyrok QFY	1	t	115
4461	Kosogoron QFY	1	t	115
4462	Kozikent MFY	1	t	115
4463	Koziyokli MFY	1	t	115
4464	Ko`k-ota MFY	1	t	115
4465	Magit MFY	1	t	115
4466	Maydakozok MFY	1	t	115
4467	Mirbozor SHFY	1	t	115
4468	Muqimiy MFY	1	t	115
4469	Mushkent MFY	1	t	115
4470	Mustaqillik MFY	1	t	115
4471	N.Urinov MFY	1	t	115
4472	Narpay MFY	1	t	115
4473	Navro`z MFY	1	t	115
4474	Nog`araxona MFY	1	t	115
4475	Nug`ay MFY	1	t	115
4476	o`Abduraximov MFY	1	t	115
4477	Olti ug`il QFY	1	t	115
4478	Olti ug`il MFY	1	t	115
4479	Oq-oltin MFY	1	t	115
4480	O`zbekiston MFY	1	t	115
4481	O`zbekkenti MFY	1	t	115
4482	R.Olchin MFY	1	t	115
4483	Salovat MFY	1	t	115
4484	Sarbozor MFY	1	t	115
4485	shahar mfylari	1	t	115
4486	Sohibkor MFY	1	t	115
4487	T.Roziqov MFY	1	t	115
4488	Tepa MFY	1	t	115
4489	Tepaqo`rg`on MFY	1	t	115
4490	Tinchlik MFY	1	t	115
4491	Tortuvli MFY	1	t	115
4492	Toshko`prik MFY	1	t	115
4493	Totkent MFY	1	t	115
4494	To`ron MFY	1	t	115
4495	X. Aliqulov MFY	1	t	115
4496	Xalqobod MFY	1	t	115
4497	Xo`jakarzon MFY	1	t	115
4498	Xo`jaqo`rg`on MFY	1	t	115
4499	Yangi ariq MFY	1	t	115
4500	Yangiqo`rg`on QFY	1	t	115
4501	Yangirabod QFY	1	t	115
4502	Zirabulok MFY	1	t	115
4503	Zoir ota MFY	1	t	115
4504	Agron MFY	1	t	116
4505	Amir-Temur MFY	1	t	116
4506	Arab-ota MFY	1	t	116
4507	Boshkuduk MFY	1	t	116
4508	Do`stlik MFY	1	t	116
4509	Eshat MFY	1	t	116
4510	Girdikurg`on MFY	1	t	116
4511	Jarkuduk MFY	1	t	116
4512	Jarquduq QFY	1	t	116
4513	Jom QFY	1	t	116
4514	Jom MFY	1	t	116
4515	K?chk?ldik MFY	1	t	116
4516	Kalta MFY	1	t	116
4517	Kilichli MFY	1	t	116
4518	Mehnatkash MFY	1	t	116
4519	Navbahor MFY	1	t	116
4520	Navruz MFY	1	t	116
4521	Nurbulok MFY	1	t	116
4522	Nurbuloq QFY	1	t	116
4523	Nurdum MFY	1	t	116
4524	Oksoy MFY	1	t	116
4525	Olga MFY	1	t	116
4526	Omondara MFY	1	t	116
4527	Pulatchi MFY	1	t	116
4528	Qo`rg`oncha MFY	1	t	116
4529	Sepki MFY	1	t	116
4530	Sarikul MFY	1	t	116
4531	Saroy MFY	1	t	116
4532	Sazag`on QFY	1	t	116
4533	Sazag`on MFY	1	t	116
4534	Sharq-Yulduzi MFY	1	t	116
4535	Shaxar mfylari	1	t	116
4536	Shurobod MFY	1	t	116
4537	T.Usanov MFY	1	t	116
4538	Tegirmonboshi MFY	1	t	116
4539	Tepakul MFY	1	t	116
4540	Tim QFY	1	t	116
4541	Tutli QFY	1	t	116
4542	Ulus QFY	1	t	116
4543	Ulus MFY	1	t	116
4544	Urtabuz MFY	1	t	116
4545	Xalkobod MFY	1	t	116
4546	Xazarmali MFY	1	t	116
4547	A.Navoiy QFY	1	t	117
4548	Amur Temur MFY	1	t	117
4549	Arpa MFY	1	t	117
4550	Avazali MFY	1	t	117
4551	Boshdarxon MFY	1	t	117
4552	Bozorjoy MFY	1	t	117
4553	Charbog` 2 MFY	1	t	117
4554	Dahbed MFY	1	t	117
4555	Dahbed SHFY	1	t	117
4556	Galaravot MFY	1	t	117
4557	Ko`ksoqol MFY	1	t	117
4558	Kumushkent MFY	1	t	117
4559	Loyish MFY	1	t	117
4560	Loyish SHFY	1	t	117
4561	Moykovok MFY	1	t	117
4562	Mustaqillik MFY	1	t	117
4563	Navoiy MFY	1	t	117
4564	Navro`z MFY	1	t	117
4565	Oqdaryo MFY	1	t	117
4566	Oytamg`ali MFY	1	t	117
4567	O`zbekiston MFY	1	t	117
4568	Paxtaobod MFY	1	t	117
4569	Po`latdarxon MFY	1	t	117
4570	Primknt MFY	1	t	117
4571	Primkent QFY	1	t	117
4572	Qorateri QFY	1	t	117
4573	Rayimqo`lov MFY	1	t	117
4574	Sarka MFY	1	t	117
4575	Shermatov MFY	1	t	117
4576	Sug`onchi MFY	1	t	117
4577	Temirak MFY	1	t	117
4578	Uchtepa MFY	1	t	117
4579	Uzunqishloq MFY	1	t	117
4580	Yangihayot MFY	1	t	117
4581	Yangikent QFY	1	t	117
4582	Yangiobod MFY	1	t	117
4583	Yangiqishloq MFY	1	t	117
4584	Yangiqo`rg`on MFY	1	t	117
4585	Yangiqo`rg`on QFY	1	t	117
4586	Yangiravot-1MFY	1	t	117
4587	Yangiravot-2 MFY	1	t	117
4588	Zarafshon QFY	1	t	117
4589	A Navoiy MFY	1	t	118
4590	Sarbozor MFY	1	t	118
4591	A Primov MFY	1	t	118
4592	A Yassaviy MFY	1	t	118
4593	Aliobod MFY	1	t	118
4594	Beshqo`rg`on MFY	1	t	118
4595	Bahor MFY	1	t	118
4596	Baxrin MFY	1	t	118
4597	Birlashgan QFY	1	t	118
4598	Birlashuv MFY	1	t	118
4599	Boshcho`rosh MFY	1	t	118
4600	Bo`ri MFY	1	t	118
4601	Bunyodkor MFY	1	t	118
4602	Chelak SHFY	1	t	118
4603	Cholmo`yin MFY	1	t	118
4604	Choporoshli QFY	1	t	118
4605	Choshtepa MFY	1	t	118
4606	Choshtepa QFY	1	t	118
4607	Dehqonobod MFY	1	t	118
4608	Darvishiq MFY	1	t	118
4609	Do`stlarobod MFY	1	t	118
4610	Do`stlik MFY	1	t	118
4611	Emalach MFY	1	t	118
4612	Ernazarqo`rg`on MFY	1	t	118
4613	Farovon MFY	1	t	118
4614	Fidokor MFY	1	t	118
4615	g`allakor MFY	1	t	118
4616	G`oyibota MFY	1	t	118
4617	Go`zal MFY	1	t	118
4618	Guliston MFY	1	t	118
4619	Guliston QFY	1	t	118
4620	I Ergashev MFY	1	t	118
4621	Ilg`or MFY	1	t	118
4622	Istiqlol MFY	1	t	118
4623	Juvozxona MFY	1	t	118
4624	Kattasaydov MFY	1	t	118
4625	Ko`kdala QFY	1	t	118
4626	Ko`ktepa MFY	1	t	118
4627	Ko`lto`sin MFY	1	t	118
4628	Ko`paki MFY	1	t	118
4629	Kulto`sin QFY	1	t	118
4630	M Ulug`bek MFY	1	t	118
4631	Madaniyat MFY	1	t	118
4632	Maniobod MFY	1	t	118
4633	Mustaqillik MFY	1	t	118
4634	Muxammadi MFY	1	t	118
4635	Nakurt MFY	1	t	118
4636	Navbahor MFY	1	t	118
4637	Navro`z MFY	1	t	118
4638	Olmazor MFY	1	t	118
4639	Oqqo`rg`on MFY	1	t	118
4640	Oqqo`rg`on QFY	1	t	118
4641	Oytamg`ali QFY	1	t	118
4642	O`rtasaydov QFY	1	t	118
4643	O`zbekiston MFY	1	t	118
4644	Polvonariq MFY	1	t	118
4645	Qahramon MFY	1	t	118
4646	Qirqovul MFY	1	t	118
4647	Qorasuv QFY	1	t	118
4648	Qumchuq MFY	1	t	118
4649	Rayim MFY	1	t	118
4650	Sanoat QFY	1	t	118
4651	Sho`rtepa MFY	1	t	118
4652	Sorisuv MFY	1	t	118
4653	T Axmedov MFY	1	t	118
4654	T Jo`raev MFY	1	t	118
4655	Tamoyrot MFY	1	t	118
4656	Toshhavuz MFY	1	t	118
4657	Toxirshayx MFY	1	t	118
4658	To`polos MFY	1	t	118
4659	Turkibola MFY	1	t	118
4660	X.Ismoil MFY	1	t	118
4661	Xolqobod MFY	1	t	118
4662	Xosa MFY	1	t	118
4663	Xo`jaobod MFY	1	t	118
4664	Zarafshon MFY	1	t	118
4665	A.Temur MFY	1	t	119
4666	Agron MFY	1	t	119
4667	Anhor QFY	1	t	119
4668	Arabxona QFY	1	t	119
4669	Beklar MFY	1	t	119
4670	Beshbola MFY	1	t	119
4671	Beshqahramon QFY	1	t	119
4672	Beshnayman MFY	1	t	119
4673	Bakkol MFY	1	t	119
4674	Balxiyon MFY	1	t	119
4675	Baxor MFY	1	t	119
4676	Baxshiboy MFY	1	t	119
4677	Bobur nomli MFY	1	t	119
4678	Bogishamol MFY	1	t	119
4679	Bogonali MFY	1	t	119
4680	Bolatosh QFY	1	t	119
4681	Boldir MFY	1	t	119
4682	Boltali MFY	1	t	119
4683	Buston MFY	1	t	119
4684	Buyuk turon MFY	1	t	119
4685	Chandir MFY	1	t	119
4686	Chandirobod MFY	1	t	119
4687	Charxin MFY	1	t	119
4688	Charxin SHFY	1	t	119
4689	Chimboy QFY	1	t	119
4690	Chimboy MFY	1	t	119
4691	Chortut MFY	1	t	119
4692	Dimishkibola QFY	1	t	119
4693	Durmonsoy MFY	1	t	119
4694	Durmontepa QFY	1	t	119
4695	Do`stlik MFY	1	t	119
4696	Elbek MFY	1	t	119
4697	Esaboy MFY	1	t	119
4698	Eski Juma MFY	1	t	119
4699	Furkat MFY	1	t	119
4700	Galatut MFY	1	t	119
4701	Go`zalkent QFY	1	t	119
4702	Go`zalkent MFY	1	t	119
4703	Gulakandoz MFY	1	t	119
4704	Guliston MFY	1	t	119
4705	Gulobod MFY	1	t	119
4706	Gumbaz MFY	1	t	119
4707	Ilm MFY	1	t	119
4708	Imomjon kadimiy yodgorligi MFY	1	t	119
4709	Iskandari MFY	1	t	119
4710	Jagalboyli MFY	1	t	119
4711	Jaul Kosim MFY	1	t	119
4712	K.Rajabov MFY	1	t	119
4713	Kamolot MFY	1	t	119
4714	Karabuyin MFY	1	t	119
4715	Katta-Nayman MFY	1	t	119
4716	Kichik Naymancha MFY	1	t	119
4717	Koksoy MFY	1	t	119
4718	Koraguppa MFY	1	t	119
4719	Korasuv MFY	1	t	119
4720	Kukoni MFY	1	t	119
4721	Qush Chinor MFY	1	t	119
4722	Kushkuduk MFY	1	t	119
4723	Mehnat MFY	1	t	119
4724	Madaniy yurish MFY	1	t	119
4725	Mangitobod MFY	1	t	119
4726	Mirzatut MFY	1	t	119
4727	Mustakillik MFY	1	t	119
4728	Namuna QFY	1	t	119
4729	Navbaxor MFY	1	t	119
4730	Navoiy MFY	1	t	119
4731	Navruz MFY	1	t	119
4732	Nayman MFY	1	t	119
4733	Nomozgox MFY	1	t	119
4734	Novchandir MFY	1	t	119
4735	Ok mangit MFY	1	t	119
4736	Oq oltin MFY	1	t	119
4737	Oltikaxramon	1	t	119
4738	Oshik ota MFY	1	t	119
4739	Parcha Chandir MFY	1	t	119
4740	Parchakora MFY	1	t	119
4741	Paxtachi MFY	1	t	119
4742	Paxtakor MFY	1	t	119
4743	Pulatchi QFY	1	t	119
4744	Pulatchi MFY	1	t	119
4745	Qaravultepa MFY	1	t	119
4746	Qarshiobod MFY	1	t	119
4747	Qator terak MFY	1	t	119
4748	Ravot MFY	1	t	119
4749	Samarqand MFY	1	t	119
4750	Sanchikul MFY	1	t	119
4751	Sanchiqul QFY	1	t	119
4752	Saribosh QFY	1	t	119
4753	Sazagon MFY	1	t	119
4754	Sh.Rashidov MFY	1	t	119
4755	Shombuloq MFY	1	t	119
4756	Sinchi MFY	1	t	119
4757	Temir yo`l MFY	1	t	119
4758	Temirxo`ja MFY	1	t	119
4759	Tinchlik MFY	1	t	119
4760	Torarik MFY	1	t	119
4761	Torarik QFY	1	t	119
4762	Toz Qulton MFY	1	t	119
4763	Tukboy MFY	1	t	119
4764	Turkman MFY	1	t	119
4765	Turon MFY	1	t	119
4766	Turt Aygir MFY	1	t	119
4767	Turt tom MFY	1	t	119
4768	Uch tepa MFY	1	t	119
4769	Ulug`bek MFY	1	t	119
4770	Un ikki MFY	1	t	119
4771	Urta Charxin MFY	1	t	119
4772	Usku MFY	1	t	119
4773	Utarchi MFY	1	t	119
4774	Xavuzak MFY	1	t	119
4775	Xindiboy MFY	1	t	119
4776	Xonchorbog` MFY	1	t	119
4777	Yangi avlod MFY	1	t	119
4778	Yangikishlok MFY	1	t	119
4779	Yangiobod MFY	1	t	119
4780	Yangiravot MFY	1	t	119
4781	Yangisanoat MFY	1	t	119
4782	Yuqori bog`onali MFY	1	t	119
4783	Zangiboy MFY	1	t	119
4784	Zormon MFY	1	t	119
4785	Alisher Navoiy MFY	1	t	120
4786	Amir Temur MFY	1	t	120
4787	Amirobod MFY	1	t	120
4788	Bobon MFY	1	t	120
4789	Bodoy MFY	1	t	120
4790	Bog`oloni MFY	1	t	120
4791	Boltali MFY	1	t	120
4792	Bo`ston MFY	1	t	120
4793	Burqut MFY	1	t	120
4794	Chashma MFY	1	t	120
4795	Chorgo`sha MFY	1	t	120
4796	Choshtepa MFY	1	t	120
4797	Dabus qal`a MFY	1	t	120
4798	Do`ng MFY	1	t	120
4799	Do`stobod QFY	1	t	120
4800	Eshmatjobi MFY	1	t	120
4801	Farovon yo`ldoshobod	1	t	120
4802	Go`ro`g`li MFY	1	t	120
4803	Guliston MFY	1	t	120
4804	Ismoilobod MFY	1	t	120
4805	Istiqbol MFY	1	t	120
4806	Istiqlol MFY	1	t	120
4807	Jahonobod MFY	1	t	120
4808	Jona MFY	1	t	120
4809	Keshtali MFY	1	t	120
4810	Ko`rpa MFY	1	t	120
4811	Mirkent MFY	1	t	120
4812	Mirsiddiq Hashmat	1	t	120
4813	Mirza Salimiy MFY	1	t	120
4814	Mirzo Ulug`bek MFY	1	t	120
4815	Mirzo Nodim MFY	1	t	120
4816	Mirzo Olim MFY	1	t	120
4817	Misit QFY	1	t	120
4818	Mojor MFY	1	t	120
4819	Nahripay MFY	1	t	120
4820	Nayman MFY	1	t	120
4821	Niyozjobi MFY	1	t	120
4822	Nurafshon MFY	1	t	120
4823	Oqtepa MFY	1	t	120
4824	O`rta MFY	1	t	120
4825	Pastburqut MFY	1	t	120
4826	Poyonigumbaz MFY	1	t	120
4827	Po`latchi QFY	1	t	120
4828	Qarnab QFY	1	t	120
4829	Qirguli MFY	1	t	120
4830	Qodiris MFY	1	t	120
4831	Qoratepa MFY	1	t	120
4832	Qoraunos MFY	1	t	120
4833	Qo`shhovuz MFY	1	t	120
4834	Quvondiq MFY	1	t	120
4835	Quyibog` QFY	1	t	120
4836	Sadr ziyo MFY	1	t	120
4837	Sardoba MFY	1	t	120
4838	Saroy MFY	1	t	120
4839	Shamsnazar MFY	1	t	120
4840	Sohil bo`yi MFY	1	t	120
4841	Sotiboldi MFY	1	t	120
4842	Sultonobod QFY	1	t	120
4843	Suluvqo`rg`on MFY	1	t	120
4844	Tadbirkor MFY	1	t	120
4845	Taraqqiyot MFY	1	t	120
4846	Tinchlik MFY	1	t	120
4847	Toshko`prik MFY	1	t	120
4848	To`g`olon MFY	1	t	120
4849	Ukrash MFY	1	t	120
4850	Urg`uch MFY	1	t	120
4851	Urganji MFY	1	t	120
4852	Hayitelbegi MFY	1	t	120
4853	Xayrobod QFY	1	t	120
4854	Xudoyberdi MFY	1	t	120
4855	Xumor QFY	1	t	120
4856	Yangiobod MFY	1	t	120
4857	Zarafshon MFY	1	t	120
4858	Ziyovuddin SHFY	1	t	120
4859	Andijoni MFY	1	t	121
4860	Angarolmos MFY	1	t	121
4861	Badal MFY	1	t	121
4862	Bo`zi MFY	1	t	121
4863	Buxori MFY	1	t	121
4864	Chaqqa MFY	1	t	121
4865	Chorshanba MFY	1	t	121
4866	Chumchuqli MFY	1	t	121
4867	Dehnav MFY	1	t	121
4868	Dashtakibolo QFY	1	t	121
4869	Dashtiso`xta MFY	1	t	121
4870	Gulbog` MFY	1	t	121
4871	Gulobod MFY	1	t	121
4872	Ipakchi MFY	1	t	121
4873	Jarqishloq MFY	1	t	121
4874	Jo`yisoy MFY	1	t	121
4875	Kattako`rgonariq QFY	1	t	121
4876	Konigil MFY	1	t	121
4877	Ko`saxo MFY	1	t	121
4878	Kulba MFY	1	t	121
4879	Kulbaipoyon QFY	1	t	121
4880	Markaziy Arabxona MFY	1	t	121
4881	Mirishkor MFY	1	t	121
4882	Mironqul MFY	1	t	121
4883	Navbog` MFY	1	t	121
4884	Navobod MFY	1	t	121
4885	Navobod MFY	1	t	121
4886	Navro`z MFY	1	t	121
4887	Navro`z MFY	1	t	121
4888	Nayzat?ppa MFY	1	t	121
4889	Obod MFY	1	t	121
4890	Ohalik QFY	1	t	121
4891	Oqmachit MFY	1	t	121
4892	O`rta Arabxona MFY	1	t	121
4893	O`rta Ohalik MFY	1	t	121
4894	O`rta Turkman MFY	1	t	121
4895	O`rtashiq MFY	1	t	121
4896	O`zbekkenti MFY	1	t	121
4897	Parrandachi MFY	1	t	121
4898	Past Oxalik MFY	1	t	121
4899	Pulimug`ob MFY	1	t	121
4900	Qavchinon MFY	1	t	121
4901	Qavchinonibolo MFY	1	t	121
4902	Qaynama QFY	1	t	121
4903	Qorasuv MFY	1	t	121
4904	Qoziariq MFY	1	t	121
4905	Qoziqo`rg`on MFY	1	t	121
4906	Qo`shko`pruk MFY	1	t	121
4907	Qo`shmachit MFY	1	t	121
4908	Qo`shtamg`ali MFY	1	t	121
4909	Qo`shtamg`ali QFY	1	t	121
4910	Qo`yi Arabxona MFY	1	t	121
4911	Qo`yi Chordara MFY	1	t	121
4912	Qo`yi Qaynama MFY	1	t	121
4913	Qo`yi Turkman MFY	1	t	121
4914	Qumzor MFY	1	t	121
4915	Rajabamin MFY	1	t	121
4916	Ravonak MFY	1	t	121
4917	Rustam MFY	1	t	121
4918	Sarimazor MFY	1	t	121
4919	Shalg`amon MFY	1	t	121
4920	Sho`rboi-1 MFY	1	t	121
4921	Sho`rboi-2 MFY	1	t	121
4922	Sho`rboicha MFY	1	t	121
4923	Sulfakabutak MFY	1	t	121
4924	Talibarzui bolo MFY	1	t	121
4925	Talibarzui poyon MFY	1	t	121
4926	Ulug`bek QFY	1	t	121
4927	Urganji MFY	1	t	121
4928	Xaymari bolo MFY	1	t	121
4929	Xaymari poyon MFY	1	t	121
4930	Xoja Axrori Vali-1 MFY	1	t	121
4931	Xoja Axrori Vali-2 MFY	1	t	121
4932	Yangiariq MFY	1	t	121
4933	Yangiariq MFY	1	t	121
4934	Yangiariq - 1 MFY	1	t	121
4935	Yangijoy MFY	1	t	121
4936	Yangiobod MFY	1	t	121
4937	Yangiravot MFY	1	t	121
4938	Yukori Turkman MFY	1	t	121
4939	Yuqori Arabxona MFY	1	t	121
4940	Yuqori Chordara MFY	1	t	121
4941	Yuqori Qaynama MFY	1	t	121
4942	Zahlik MFY	1	t	121
4943	Abdulla Qaxxor MFY	1	t	122
4944	Abdurahmon Jomiy MFY	1	t	122
4945	Abu Abdullo Rudakiy MFY	1	t	122
4946	Abu Rayxon B?runiy MFY	1	t	122
4947	Adolat MFY	1	t	122
4948	Aeroport MFY	1	t	122
4949	Afrosiyob MFY	1	t	122
4950	Al Buxoriy MFY	1	t	122
4951	Al Farobiy MFY	1	t	122
4952	Ali Kushchi MFY	1	t	122
4953	Ali zoda MFY	1	t	122
4954	Alisher Navoiy MFY	1	t	122
4955	Amir Temur MFY	1	t	122
4956	Anhor MFY	1	t	122
4957	Axillik MFY	1	t	122
4958	Axmad Yassaviy MFY	1	t	122
4959	Beklar MFY	1	t	122
4960	Bekxo MFY	1	t	122
4961	Besh chinor MFY	1	t	122
4962	Beshg`ujum MFY	1	t	122
4963	Baraka MFY	1	t	122
4964	Baxor MFY	1	t	122
4965	Birlik MFY	1	t	122
4966	Bog`i baland MFY	1	t	122
4967	Bog`i maydon MFY	1	t	122
4968	Bog`bonlar MFY	1	t	122
4969	Bog`dod MFY	1	t	122
4970	Bog`i baland-2 MFY	1	t	122
4971	Bog`i maydon 2 MFY	1	t	122
4972	Bog`i saroy MFY	1	t	122
4973	Bog`i shamol MFY	1	t	122
4974	Bog`i shifo MFY	1	t	122
4975	Bog`i Temur MFY	1	t	122
4976	Bog`ichinor MFY	1	t	122
4977	Bog`iston MFY	1	t	122
4978	Botir Zokirov MFY	1	t	122
4979	Bunyod MFY	1	t	122
4980	Bunyodkor MFY	1	t	122
4981	Buston MFY	1	t	122
4982	Chaqar MFY	1	t	122
4983	Chashma MFY	1	t	122
4984	Chilkuduk MFY	1	t	122
4985	Chilstun MFY	1	t	122
4986	Chorbog` MFY	1	t	122
4987	Chupon ota MFY	1	t	122
4988	D. Samarqandiy MFY	1	t	122
4989	D.Qalandarxona MFY	1	t	122
4990	Devori Kundalang MFY	1	t	122
4991	Dehqon MFY	1	t	122
4992	Dahbediy MFY	1	t	122
4993	Damarik-1 MFY	1	t	122
4994	Darg`om MFY	1	t	122
4995	Dari Zanjir MFY	1	t	122
4996	Dukchiyon MFY	1	t	122
4997	Do`stlik MFY	1	t	122
4998	Eski Qalandarxona MFY	1	t	122
4999	Eski Xazora MFY	1	t	122
5000	Farog`at MFY	1	t	122
5001	Farovonlik MFY	1	t	122
5002	Farxod shfy	1	t	122
5003	Furqat MFY	1	t	122
5004	G`afur G`ulom MFY	1	t	122
5005	G`iyosiddin Jamshid MFY	1	t	122
5006	Geofizika MFY	1	t	122
5007	Galaosiyo MFY	1	t	122
5008	Garmako MFY	1	t	122
5009	Gulbaxor MFY	1	t	122
5010	Guliston MFY	1	t	122
5011	Gullar bogi MFY	1	t	122
5012	Guri Amir MFY	1	t	122
5013	Ibn Sino MFY	1	t	122
5014	Ibrohim Xuja MFY	1	t	122
5015	Ilmobod MFY	1	t	122
5016	Ilxom MFY	1	t	122
5017	Imom Vose MFY	1	t	122
5018	Ipak yo`li MFY	1	t	122
5019	Islohot MFY	1	t	122
5020	Istiqlol MFY	1	t	122
5021	Istiqbol MFY	1	t	122
5022	Izvoshchilar MFY	1	t	122
5023	Joyi chukur MFY	1	t	122
5024	Kadriyat MFY	1	t	122
5025	Kaftarxona MFY	1	t	122
5026	Kaftarxona-2 MFY	1	t	122
5027	Kamolot MFY	1	t	122
5028	Karshi yuli MFY	1	t	122
5029	Katta arik MFY	1	t	122
5030	Kattakurgon MFY	1	t	122
5031	Kavarzor MFY	1	t	122
5032	Kavola MFY	1	t	122
5033	Kavola-3 MFY	1	t	122
5034	Kimyogarlar shfy	1	t	122
5035	Kir MFY	1	t	122
5036	Kuk maschid MFY	1	t	122
5037	Kuksaroy MFY	1	t	122
5038	Kul MFY	1	t	122
5039	Kundi Sufi MFY	1	t	122
5040	Kurgoncha MFY	1	t	122
5041	Kush bakkoli MFY	1	t	122
5042	Kush chinor MFY	1	t	122
5043	Kush Hovuz MFY	1	t	122
5044	Kuyi Xuja Soat MFY	1	t	122
5045	Lolazor-2 MFY	1	t	122
5046	Loxutiy MFY	1	t	122
5047	Luchchakon MFY	1	t	122
5048	M.Kungirokdor MFY	1	t	122
5049	Mevazor MFY	1	t	122
5050	Mexnat MFY	1	t	122
5051	Mexrobod MFY	1	t	122
5052	Madadkor MFY	1	t	122
5053	Madaniyat MFY	1	t	122
5054	Maroqand MFY	1	t	122
5055	Marxabo MFY	1	t	122
5056	Mash`al MFY	1	t	122
5057	Matonat MFY	1	t	122
5058	Maqsud Shayxzoda MFY	1	t	122
5059	Maysazor MFY	1	t	122
5060	Ming tut MFY	1	t	122
5061	Mir Said Baraka MFY	1	t	122
5062	Mirzo Ulugbek MFY	1	t	122
5063	Motrid MFY	1	t	122
5064	Muborak MFY	1	t	122
5065	Mulyon MFY	1	t	122
5066	Mulyon-2 MFY	1	t	122
5067	Mustakillik MFY	1	t	122
5068	Namozgoh MFY	1	t	122
5069	Navbaxor MFY	1	t	122
5070	Navbogchiyon MFY	1	t	122
5071	Navro`z MFY	1	t	122
5072	Navro`z-2 MFY	1	t	122
5073	Nayman MFY	1	t	122
5074	Nodirabegim MFY	1	t	122
5075	Nurafshon MFY	1	t	122
5076	Nurli kelajak MFY	1	t	122
5077	Nurli yul MFY	1	t	122
5078	Nurobod MFY	1	t	122
5079	Obi Rahmat MFY	1	t	122
5080	Obod MFY	1	t	122
5081	Oksaroy MFY	1	t	122
5082	Oltin Asr MFY	1	t	122
5083	Orzu MFY	1	t	122
5084	Panjob MFY	1	t	122
5085	Puli Mirzo MFY	1	t	122
5086	Qircha MFY	1	t	122
5087	Qumzor MFY	1	t	122
5088	Raim Shokirbekov MFY	1	t	122
5089	Raxmatobod MFY	1	t	122
5090	Rohat MFY	1	t	122
5091	Semurg` MFY	1	t	122
5092	Sevali MFY	1	t	122
5093	Sa`di Sheroziy MFY	1	t	122
5094	Sadaf MFY	1	t	122
5095	Sadriddin Ayniy MFY	1	t	122
5096	Safedi MFY	1	t	122
5097	Said mahalla MFY	1	t	122
5098	Sarbadorlar MFY	1	t	122
5099	Sarbon MFY	1	t	122
5100	Sattepo MFY	1	t	122
5101	Saxovat MFY	1	t	122
5102	Sharq Yulduzi MFY	1	t	122
5103	Sharq MFY	1	t	122
5104	Shaxriobod MFY	1	t	122
5105	Shirin MFY	1	t	122
5106	Shodlik MFY	1	t	122
5107	Shoyiboflar MFY	1	t	122
5108	Shukrona MFY	1	t	122
5109	Shuxrat MFY	1	t	122
5110	Siyobcha MFY	1	t	122
5111	So`lim shfy	1	t	122
5112	Sufi Roziq MFY	1	t	122
5113	Sugdiyona MFY	1	t	122
5114	Suzangaron MFY	1	t	122
5115	Temiryulchilar MFY	1	t	122
5116	Terakzor MFY	1	t	122
5117	Tadbirkorlar MFY	1	t	122
5118	Tazar MFY	1	t	122
5119	Tinchlik MFY	1	t	122
5120	Tojmahal MFY	1	t	122
5121	Tokzor MFY	1	t	122
5122	Tong MFY	1	t	122
5123	Toshkandiy MFY	1	t	122
5124	Tupxona MFY	1	t	122
5125	Turon MFY	1	t	122
5126	Tutzor MFY	1	t	122
5127	Urguti MFY	1	t	122
5128	Urikzor MFY	1	t	122
5129	Urta Xuja Soat MFY	1	t	122
5130	Uvaysiy MFY	1	t	122
5131	Vatanparvar MFY	1	t	122
5132	Xadicha Sulaymonova MFY	1	t	122
5133	Xalifa Ibrohim MFY	1	t	122
5134	Xalkobod MFY	1	t	122
5135	Xamid Olimjon MFY	1	t	122
5136	Xayotobod MFY	1	t	122
5137	Xazora MFY	1	t	122
5138	Hilol MFY	1	t	122
5139	Hofiz Sheroziy MFY	1	t	122
5140	Xo`ja Abdu Darun MFY	1	t	122
5141	Xo`ja Axrori Vali MFY	1	t	122
5142	Xo`ja Chorrux MFY	1	t	122
5143	Xo`ja gunjoyish MFY	1	t	122
5144	Xo`ja gunjoyish-2 MFY	1	t	122
5145	Xo`ja Qishloq MFY	1	t	122
5146	Xo`ja Soat MFY	1	t	122
5147	Xo`ja Yusuf MFY	1	t	122
5148	Xo`jandiy MFY	1	t	122
5149	Yangi Qo`rg`on MFY	1	t	122
5150	Yangi obod MFY	1	t	122
5151	Yangi Hayot MFY	1	t	122
5152	Yangi Xayrabod MFY	1	t	122
5153	Yominiy MFY	1	t	122
5154	Yoshlar MFY	1	t	122
5155	Yoshlik MFY	1	t	122
5156	Yuqori Xo`ja Soat MFY	1	t	122
5157	Yulduz MFY	1	t	122
5158	Zarafshon MFY	1	t	122
5159	Zarduzlar MFY	1	t	122
5160	Zargartepo MFY	1	t	122
5161	Ziyokorlar MFY	1	t	122
5162	Ziyolilar MFY	1	t	122
5163	Zominiy MFY	1	t	122
5164	Zulfiya MFY	1	t	122
5165	Adas MFY	1	t	123
5166	Adas QFY	1	t	123
5167	Bachki MFY	1	t	123
5168	Baxshitepa MFY	1	t	123
5169	Bog`izog`on QFY	1	t	123
5170	Bogizogon MFY	1	t	123
5171	Butboy MFY	1	t	123
5172	Chorboktepa MFY	1	t	123
5173	Davlatobod MFY	1	t	123
5174	Do`stlik MFY	1	t	123
5175	Eskijuma MFY	1	t	123
5176	Fayziobod MFY	1	t	123
5177	Gadoykushchi MFY	1	t	123
5178	Galabotir MFY	1	t	123
5179	Gulba MFY	1	t	123
5180	Gulba QFY	1	t	123
5181	Jalolobod MFY	1	t	123
5182	Jumabozor MFY	1	t	123
5183	Jumabozor QFY	1	t	123
5184	Katta Taylok MFY	1	t	123
5185	Kovchinon MFY	1	t	123
5186	Kurgoncha MFY	1	t	123
5187	Madaniyat MFY	1	t	123
5188	Madaniyat QFY	1	t	123
5189	Mulkiayoz MFY	1	t	123
5190	Nakkashon MFY	1	t	123
5191	Navzandak MFY	1	t	123
5192	Nayman-1 MFY	1	t	123
5193	Nayman-2 MFY	1	t	123
5194	Payshanbasiyob MFY	1	t	123
5195	Qo`rg`oncha QFY	1	t	123
5196	Ravot MFY	1	t	123
5197	Saribozor MFY	1	t	123
5198	Sariosiyo MFY	1	t	123
5199	Shopulot MFY	1	t	123
5200	Sochak-1 MFY	1	t	123
5201	Sochak-2 MFY	1	t	123
5202	Sochak-3 MFY	1	t	123
5203	Sochakibolo QFY	1	t	123
5204	Sochakipoyon-1 MFY	1	t	123
5205	Sochakipoyon-2 MFY	1	t	123
5206	Tepaqishloq MFY	1	t	123
5207	Tepaqishloq QFY	1	t	123
5208	Talliota MFY	1	t	123
5209	Tayloq QFY	1	t	123
5210	Ukrach MFY	1	t	123
5211	Uray-Elipok MFY	1	t	123
5212	O`rtaqishloq MFY	1	t	123
5213	O`zbekiston MFY	1	t	123
5214	Uzunqishloq MFY	1	t	123
5215	Vorsin MFY	1	t	123
5216	Xo`jaqishloq MFY	1	t	123
5217	Xo`jayuz MFY	1	t	123
5218	Yalang`och MFY	1	t	123
5219	Yangi Tayloq MFY	1	t	123
5220	Yangi Hayot MFY	1	t	123
5221	Yastepa MFY	1	t	123
5222	Yuqori Tayloq MFY	1	t	123
5223	Zarafshon MFY	1	t	123
5224	Etti uylik MFY	1	t	124
5225	A`loxotin MFY	1	t	124
5226	Algar MFY	1	t	124
5227	Andak MFY	1	t	124
5228	Bekravot MFY	1	t	124
5229	Beshbuloq QFY	1	t	124
5230	Beshkal MFY	1	t	124
5231	Beshkapa -1 MFY	1	t	124
5232	Beshkapa MFY	1	t	124
5233	Beshkapa-2 MFY	1	t	124
5234	Beshyog`och MFY	1	t	124
5235	Baxrin MFY	1	t	124
5236	Baxrin QFY	1	t	124
5237	Bog`ishamol MFY	1	t	124
5238	Boybul MFY	1	t	124
5239	Chagizmon MFY	1	t	124
5240	Chor-chinor MFY	1	t	124
5241	Chorraha MFY	1	t	124
5242	Choshtepa MFY	1	t	124
5243	Chumchuqli MFY	1	t	124
5244	Do`stlik MFY	1	t	124
5245	Do`stlik MFY	1	t	124
5246	G`o`s QFY	1	t	124
5247	Gijduvon MFY	1	t	124
5248	Gisht machti MFY	1	t	124
5249	Goyibota MFY	1	t	124
5250	Go`slik MFY	1	t	124
5251	Guliston MFY	1	t	124
5252	Guliston MFY	1	t	124
5253	Gulobod MFY	1	t	124
5254	Guzni MFY	1	t	124
5255	Hamza QFY	1	t	124
5256	Ilonli MFY	1	t	124
5257	Ilonli QFY	1	t	124
5258	Ipakli MFY	1	t	124
5259	Ishchan MFY	1	t	124
5260	Ispanza QFY	1	t	124
5261	Jarkishlok MFY	1	t	124
5262	Jartepa MFY	1	t	124
5263	Jartepa QFY	1	t	124
5264	Jayratepa MFY	1	t	124
5265	Jozmon MFY	1	t	124
5266	Juraptepa MFY	1	t	124
5267	K.Torinjak MFY	1	t	124
5268	K.Torinjak MFY	1	t	124
5269	Kenagas MFY	1	t	124
5270	Kamangaron MFY	1	t	124
5271	Kamangaroncha MFY	1	t	124
5272	Kamardon MFY	1	t	124
5273	Kayrokli MFY	1	t	124
5274	Kayrokli MFY	1	t	124
5275	Kingir MFY	1	t	124
5276	Kizilbosh MFY	1	t	124
5277	Koldivoyjar MFY	1	t	124
5278	Koratepa MFY	1	t	124
5279	Kulkishlok MFY	1	t	124
5280	Kulollik MFY	1	t	124
5281	Kutarma MFY	1	t	124
5282	Kuyi algar MFY	1	t	124
5283	Kuyi guzar MFY	1	t	124
5284	Kuyi Tegana MFY	1	t	124
5285	Quyiqishloq MFY	1	t	124
5286	Kuzichi MFY	1	t	124
5287	Mergancha MFY	1	t	124
5288	Mangitobod MFY	1	t	124
5289	Mazortepa MFY	1	t	124
5290	Mirzaboglon MFY	1	t	124
5291	Mirzakishlok MFY	1	t	124
5292	Mirzaqishloq QFY	1	t	124
5293	Mugol MFY	1	t	124
5294	Muminobod-1 MFY	1	t	124
5295	Muminobod-2 MFY	1	t	124
5296	Murotkishlok MFY	1	t	124
5297	Navbog MFY	1	t	124
5298	Nisbot MFY	1	t	124
5299	Okmachit MFY	1	t	124
5300	Omonqo`tan MFY	1	t	124
5301	O`ramas QFY	1	t	124
5302	P. Kalangar MFY	1	t	124
5303	Paxmob MFY	1	t	124
5304	Pochvon MFY	1	t	124
5305	Pochvon QFY	1	t	124
5306	Qorotepa QFY	1	t	124
5307	Raxmatobod MFY	1	t	124
5308	Sanchikul MFY	1	t	124
5309	Sanchikul MFY	1	t	124
5310	Sariqtepa MFY	1	t	124
5311	Satang MFY	1	t	124
5312	Savgon MFY	1	t	124
5313	Shahar mfylari	1	t	124
5314	Soy guzar MFY	1	t	124
5315	Soygus MFY	1	t	124
5316	So`fiyon MFY	1	t	124
5317	Sufi MFY	1	t	124
5318	Terak MFY	1	t	124
5319	Tersak MFY	1	t	124
5320	Tarokli MFY	1	t	124
5321	Tosharik MFY	1	t	124
5322	Turtkul MFY	1	t	124
5323	Ukrach MFY	1	t	124
5324	Uramas MFY	1	t	124
5325	Urokboyjar MFY	1	t	124
5326	Urta guzar MFY	1	t	124
5327	Uzun MFY	1	t	124
5328	Vagashti MFY	1	t	124
5329	Vatak MFY	1	t	124
5330	Vatkan-Kuzibek MFY	1	t	124
5331	Xuja guzar MFY	1	t	124
5332	Xujabaland MFY	1	t	124
5333	Xujayduk MFY	1	t	124
5334	Yalpoqtepa MFY	1	t	124
5335	Yangiariq QFY	1	t	124
5336	Yu. Qalangar MFY	1	t	124
5337	Yuqori Tegana MFY	1	t	124
5338	Zinak MFY	1	t	124
5339	A.Navoiy QFY	1	t	125
5340	Angor MFY	1	t	125
5341	Angor QFY	1	t	125
5342	Baxor MFY	1	t	125
5343	Chinobod MFY	1	t	125
5344	Dehqonbirlashuv MFY	1	t	125
5345	Dehqonittifok MFY	1	t	125
5346	Do`stlik MFY	1	t	125
5347	Do`stlik QFY	1	t	125
5348	Gilambob MFY	1	t	125
5349	Gilambob MFY	1	t	125
5350	Guliston MFY	1	t	125
5351	Gulzor MFY	1	t	125
5352	Ilg`or MFY	1	t	125
5353	Istiqlol QFY	1	t	125
5354	Karvon MFY	1	t	125
5355	Kattakum MFY	1	t	125
5356	Kayran MFY	1	t	125
5357	Kayran QFY	1	t	125
5358	Qo`shtegirmon MFY	1	t	125
5359	Madaniyat MFY	1	t	125
5360	Markaz MFY	1	t	125
5361	Navoiy MFY	1	t	125
5362	Navro`z MFY	1	t	125
5363	Navshaxar MFY	1	t	125
5364	Ozod Buxoro MFY	1	t	125
5365	O`zbekiston MFY	1	t	125
5366	Qorabog` MFY	1	t	125
5367	Qorasuv MFY	1	t	125
5368	Tallashkon MFY	1	t	125
5369	Tallimaron MFY	1	t	125
5370	Tallimaron QFY	1	t	125
5371	To`lkin MFY	1	t	125
5372	Ulug`bek MFY	1	t	125
5373	Xomkon MFY	1	t	125
5374	Xujanko MFY	1	t	125
5375	Y. Oxunboboev MFY	1	t	125
5376	Yangi Turmush MFY	1	t	125
5377	Yangiobod MFY	1	t	125
5378	Yangiobod QFY	1	t	125
5379	Yuqori Tallashqon MFY	1	t	125
5380	Yuqori Xo`jakiya MFY	1	t	125
5381	Zang QFY	1	t	125
5382	Zartepa MFY	1	t	125
5383	Avlod QFY	1	t	126
5384	Alachapon (Jamoatchi) MFY	1	t	126
5385	Ariq usti MFY	1	t	126
5386	Avlod MFY	1	t	126
5387	Bibishirin MFY	1	t	126
5388	Bog`ibolo MFY	1	t	126
5389	Boysun QFY	1	t	126
5390	Chilonzor MFY	1	t	126
5391	Chorchinor MFY	1	t	126
5392	Dexibolo (Jamoatchi) MFY	1	t	126
5393	Darband MFY	1	t	126
5394	Darband QFY	1	t	126
5395	Dashtig`oz MFY	1	t	126
5396	Duoba MFY	1	t	126
5397	Gaza MFY	1	t	126
5398	Inkabot MFY	1	t	126
5399	Kofrun MFY	1	t	126
5400	Kuchkak MFY	1	t	126
5401	Machay QFY	1	t	126
5402	Munchok MFY	1	t	126
5403	Mustakillik MFY	1	t	126
5404	N`a`zamov MFY	1	t	126
5405	Obi MFY	1	t	126
5406	O`rta Machay MFY	1	t	126
5407	Pasurxi MFY	1	t	126
5408	Poygaboshi MFY	1	t	126
5409	Pulhokim MFY	1	t	126
5410	Qizilnavr (Jamoatchi) MFY	1	t	126
5411	Qorabo`yin MFY	1	t	126
5412	Qo`rg`oncha MFY	1	t	126
5413	Qo`rgoncha QFY	1	t	126
5414	Quduqsoy MFY	1	t	126
5415	Rabot MFY	1	t	126
5416	Rabot QFY	1	t	126
5417	Sangchil MFY	1	t	126
5418	Sariosiyo MFY	1	t	126
5419	Sayrob MFY	1	t	126
5420	Sayrob QFY	1	t	126
5421	Sho`rob (Jamoatchi)	1	t	126
5422	Sho`rsoy MFY	1	t	126
5423	Tangumush MFY	1	t	126
5424	Tuda (Jamoatchi) MFY	1	t	126
5425	Tuzbozor MFY	1	t	126
5426	Xo`jabulg`on MFY	1	t	126
5427	Yu.Qodirov MFY	1	t	126
5428	Yuqori machay MFY	1	t	126
5429	Bobotog` (Jamoatchi) MFY	1	t	127
5430	Mingbuloq MFY	1	t	127
5431	Sh.Norqobilov MFY	1	t	127
5432	A.Ikromov MFY	1	t	127
5433	A.Jomiy MFY	1	t	127
5434	A.Shukurov MFY	1	t	127
5435	A.Turdiev MFY	1	t	127
5436	Abbos Malik MFY	1	t	127
5437	Anbarsoy QFY	1	t	127
5438	Anorbuloq (Jamoatchi) MFY	1	t	127
5439	B.G`ulomov (sina 1) MFY	1	t	127
5440	B.Yusupov MFY	1	t	127
5441	Bandixon (Jamoatchi) MFY	1	t	127
5442	Baynalminal MFY	1	t	127
5443	Binokor QFY	1	t	127
5444	Chagam (Jamoatchi) MFY	1	t	127
5445	Chambil MFY	1	t	127
5446	Chim MFY	1	t	127
5447	Chorgul MFY	1	t	127
5448	Chukurqishloq MFY	1	t	127
5449	Chuntosh MFY	1	t	127
5450	Denov QFY	1	t	127
5451	Dashtichinor MFY	1	t	127
5452	Davlatsoy MFY	1	t	127
5453	Daxana QFY MFY	1	t	127
5454	Daxana MFY	1	t	127
5455	Dug`ob (Jamoatchi) MFY	1	t	127
5456	Dunyotepa MFY	1	t	127
5457	Do`stlik QFY	1	t	127
5458	Do`stlik MFY	1	t	127
5459	E.Mirzaxmedov MFY	1	t	127
5460	Elobod MFY	1	t	127
5461	Farg`ona QFY	1	t	127
5462	Guliston MFY	1	t	127
5463	Guliston MFY	1	t	127
5464	Gulobod MFY	1	t	127
5465	I.Ismoilov (sina 2) MFY	1	t	127
5466	Ibn Sino MFY	1	t	127
5467	Istikbol MFY	1	t	127
5468	Jamatak MFY	1	t	127
5469	Jart?pa MFY	1	t	127
5470	Jiydabuloq (Jamoatchi) MFY	1	t	127
5471	K.Karimov MFY	1	t	127
5472	K.Sayfullaev (sina 3) MFY	1	t	127
5473	K.Xandalov MFY	1	t	127
5474	Kenagas QFY	1	t	127
5475	Katta-Qarshi MFY	1	t	127
5476	Qaytmas MFY	1	t	127
5477	Kiyovsuv (Jamoatchi) MFY	1	t	127
5478	Kiziljar MFY	1	t	127
5479	Kiziljar QFY	1	t	127
5480	Korabogtepa MFY	1	t	127
5481	Korakuz MFY	1	t	127
5482	Koralang MFY	1	t	127
5483	Koraxon MFY	1	t	127
5484	Kovunlisoy MFY	1	t	127
5485	Kuchakli MFY	1	t	127
5486	Kukabulok MFY	1	t	127
5487	Lagmonota MFY	1	t	127
5488	Lochin MFY	1	t	127
5489	Lolazor MFY	1	t	127
5490	Lupon MFY	1	t	127
5491	M.Sh.Oybek MFY	1	t	127
5492	Minora MFY	1	t	127
5493	Muqumiy MFY	1	t	127
5494	Namozgox MFY	1	t	127
5495	Navbaxor MFY	1	t	127
5496	Navro`z MFY	1	t	127
5497	Obodon MFY	1	t	127
5498	Olovuddin MFY	1	t	127
5499	Ostona MFY	1	t	127
5500	Oxlar MFY	1	t	127
5501	Oxtom MFY	1	t	127
5502	Ozod MFY	1	t	127
5503	O`rtaqishloq MFY	1	t	127
5504	O`zgarish MFY	1	t	127
5505	Pastkiziljar MFY	1	t	127
5506	Paxtakurash MFY	1	t	127
5507	Pistamozor QFY	1	t	127
5508	Pojir (Jamoatchi) MFY	1	t	127
5509	Qizilgul MFY	1	t	127
5510	S.Bekmurodov MFY	1	t	127
5511	S.Raximov MFY	1	t	127
5512	Sebzor MFY	1	t	127
5513	Sarixalka (Jamoatchi) MFY	1	t	127
5514	Sh.Rashidov MFY	1	t	127
5515	Shamoli MFY	1	t	127
5516	Shaxrinav MFY	1	t	127
5517	Sina QFY	1	t	127
5518	Surnaytepa MFY	1	t	127
5519	T.Tilavov (Jamoatchi) MFY	1	t	127
5520	Terak (Jamoatchi) MFY	1	t	127
5521	Tasmasoy MFY	1	t	127
5522	Tolqishloq MFY	1	t	127
5523	Tortuvli QFY	1	t	127
5524	U.Qoraev MFY	1	t	127
5525	U.Nabiev MFY	1	t	127
5526	O`rta qishloq MFY	1	t	127
5527	Ushor MFY	1	t	127
5528	O`zbekiston MFY	1	t	127
5529	X.Maxmudov MFY	1	t	127
5530	X.Murodov MFY	1	t	127
5531	X.Ostonaqulov MFY	1	t	127
5532	X.X.Niyoziy MFY	1	t	127
5533	Xayrabod QFY	1	t	127
5534	Xazorbog` QFY	1	t	127
5535	Xitoyan MFY	1	t	127
5536	Xolchayon QFY	1	t	127
5537	Xolchayon MFY	1	t	127
5538	Xujakulsin (Jamoatchi) MFY	1	t	127
5539	Xujaxalki MFY	1	t	127
5540	Y.Oxunboboev MFY	1	t	127
5541	Yangi hayot MFY	1	t	127
5542	Yangi hazarbog` MFY	1	t	127
5543	Yangibog` QFY	1	t	127
5544	Yangiqishloq MFY	1	t	127
5545	Yangikuch MFY	1	t	127
5546	Yangiobod QFY	1	t	127
5547	Yangiobod MFY	1	t	127
5548	Yangiobod MFY	1	t	127
5549	Yangiobod .1 MFY	1	t	127
5550	Yangiobod .2 MFY	1	t	127
5551	Yangizamon QFY	1	t	127
5552	Yurchi QFY	1	t	127
5553	Yurchi MFY	1	t	127
5554	Z.M.Bobur MFY	1	t	127
5555	Zaxartepa MFY	1	t	127
5556	A.Navoiy MFY	1	t	128
5557	A.Navoiy MFY	1	t	128
5558	Avlod MFY	1	t	128
5559	Beshbuloq MFY	1	t	128
5560	Bobotog` MFY	1	t	128
5561	Bobotog` MFY	1	t	128
5562	Bobur MFY	1	t	128
5563	Boymoqli MFY	1	t	128
5564	Chorjo`y MFY	1	t	128
5565	Chorjo`y QFY	1	t	128
5566	Dehqonobod MFY	1	t	128
5567	Dehqonobod QFY	1	t	128
5568	Dam MFY	1	t	128
5569	Do`stlik MFY	1	t	128
5570	Eskiqishloq MFY	1	t	128
5571	g`ur-g`ur MFY	1	t	128
5572	Garang MFY	1	t	128
5573	Guliston MFY	1	t	128
5574	Gulxovuz MFY	1	t	128
5575	I.Turopov MFY	1	t	128
5576	Ismoil tepa MFY	1	t	128
5577	Istiqlol MFY	1	t	128
5578	Jarqurg`on QFY	1	t	128
5579	Jinjaktepa MFY	1	t	128
5580	Kakaydi QFY	1	t	128
5581	Kamar MFY	1	t	128
5582	Kuldovli MFY	1	t	128
5583	Kunchiqish MFY	1	t	128
5584	Kushtepa MFY	1	t	128
5585	Loyqand MFY	1	t	128
5586	Mehnat rohat MFY	1	t	128
5587	Mehnatobod MFY	1	t	128
5588	Markaziy MFY	1	t	128
5589	Maslahat tepa MFY	1	t	128
5590	Mingchinor MFY	1	t	128
5591	Minor MFY	1	t	128
5592	Minor QFY	1	t	128
5593	Mopr MFY	1	t	128
5594	Mustakillik MFY	1	t	128
5595	N.Boymurodov MFY	1	t	128
5596	Namuna MFY	1	t	128
5597	Navro`z MFY	1	t	128
5598	Oqqurg`on MFY	1	t	128
5599	Oqqurg`on QFY	1	t	128
5600	Oqtepa MFY	1	t	128
5601	Oqtepa MFY	1	t	128
5602	Oqtepa MFY	1	t	128
5603	O`zbekiston MFY	1	t	128
5604	Paxtaobod MFY	1	t	128
5605	Paxtazavod MFY	1	t	128
5606	Qahramon MFY	1	t	128
5607	Qiron MFY	1	t	128
5608	Qorabo`ra MFY	1	t	128
5609	Qoraqursoq MFY	1	t	128
5610	Qorayantoq MFY	1	t	128
5611	Qorayog`och MFY	1	t	128
5612	Qumqishloq MFY	1	t	128
5613	Sh.Yulduzi QFY	1	t	128
5614	Soqchi MFY	1	t	128
5615	Surxon QFY	1	t	128
5616	T.Shoburov MFY	1	t	128
5617	U.Xudoyberdiev MFY	1	t	128
5618	Ulug`bek MFY	1	t	128
5619	Ulug`bek MFY	1	t	128
5620	H.Olimjon MFY	1	t	128
5621	Xalqabod MFY	1	t	128
5622	Xayitobod MFY	1	t	128
5623	Xo`jaqishloq MFY	1	t	128
5624	Yangi usul MFY	1	t	128
5625	Yangiariq MFY	1	t	128
5626	Yangiobod MFY	1	t	128
5627	Yangiqishloq MFY	1	t	128
5628	Zartepa MFY	1	t	128
5629	Etimqum MFY	1	t	129
5630	Bektepa MFY	1	t	129
5631	Bahoriston MFY	1	t	129
5632	Bandixon MFY	1	t	129
5633	Bandixon QFY	1	t	129
5634	Birdamlik MFY	1	t	129
5635	Bog`iston MFY	1	t	129
5636	Buston QFY	1	t	129
5637	Buston MFY	1	t	129
5638	Chinor MFY	1	t	129
5639	Chorvador QFY	1	t	129
5640	Do`stlik MFY	1	t	129
5641	Gilambob MFY	1	t	129
5642	Gulbog` MFY	1	t	129
5643	Guliston MFY	1	t	129
5644	Gulobod MFY	1	t	129
5645	Gulzor MFY	1	t	129
5646	Istara MFY	1	t	129
5647	Istiqlol MFY	1	t	129
5648	Karmaki MFY	1	t	129
5649	Kirshak QFY	1	t	129
5650	Kirshak MFY	1	t	129
5651	Korasuv MFY	1	t	129
5652	Kunchikish MFY	1	t	129
5653	Kunchikish MFY	1	t	129
5654	M?xnatobod QFY	1	t	129
5655	Mustaqillik MFY	1	t	129
5656	Navbahor MFY	1	t	129
5657	Navruz MFY	1	t	129
5658	Okjar MFY	1	t	129
5659	Olmazor QFY	1	t	129
5660	Oqqo`ton MFY	1	t	129
5661	Oxunbobo?v MFY	1	t	129
5662	O`rgilsoy MFY	1	t	129
5663	Paxtakor QFY	1	t	129
5664	Polvontosh MFY	1	t	129
5665	Qaldirg`och MFY	1	t	129
5666	Qizil qoloq MFY	1	t	129
5667	Qiziriq QFY	1	t	129
5668	Qong`isoy MFY	1	t	129
5669	Qo`sh qo`ton MFY	1	t	129
5670	Rabatak MFY	1	t	129
5671	Sarik SHFY	1	t	129
5672	Saroy MFY	1	t	129
5673	Shodlik MFY	1	t	129
5674	Shreder MFY	1	t	129
5675	Takiya MFY	1	t	129
5676	Tinchlik MFY	1	t	129
5677	Xalkobod MFY	1	t	129
5678	Xomkon MFY	1	t	129
5679	Xo`jaipok MFY	1	t	129
5680	Yakka terak MFY	1	t	129
5681	Yangi turmush MFY	1	t	129
5682	Yangi hayot QFY	1	t	129
5683	Yangi hayot MFY	1	t	129
5684	Yangi yo`l QFY	1	t	129
5685	Yangi yo`l MFY	1	t	129
5686	Yangiobod MFY	1	t	129
5687	Zevar MFY	1	t	129
5688	Zarbdor MFY	1	t	129
5689	A.Jo`raev MFY	1	t	130
5690	Achamoyli MFY	1	t	130
5691	Arigoshgan MFY	1	t	130
5692	Arpapoya MFY	1	t	130
5693	Arslonboyli QFY	1	t	130
5694	Arslonboyli MFY	1	t	130
5695	Azlarsoy MFY	1	t	130
5696	Bobolochin MFY	1	t	130
5697	Bobotog` MFY	1	t	130
5698	Bogaro MFY	1	t	130
5699	Boymoqli MFY	1	t	130
5700	Buston MFY	1	t	130
5701	Chayontepa MFY	1	t	130
5702	Chukirli MFY	1	t	130
5703	Do`stlik MFY	1	t	130
5704	G`alaba MFY	1	t	130
5705	Guliston MFY	1	t	130
5706	Gultepa MFY	1	t	130
5707	Imom tepa MFY	1	t	130
5708	Islomobod MFY	1	t	130
5709	Istiqlol MFY	1	t	130
5710	Jaloir QFY	1	t	130
5711	Jaloir MFY	1	t	130
5712	Jarkishlok MFY	1	t	130
5713	Jiydali MFY	1	t	130
5714	K.Yuldoshev MFY	1	t	130
5715	Ketmon QFY	1	t	130
5716	Karsokli MFY	1	t	130
5717	Kattakul MFY	1	t	130
5718	Kindiktepa MFY	1	t	130
5719	Kuganli MFY	1	t	130
5720	Qumqurg`on MFY	1	t	130
5721	M.Qoraboev MFY	1	t	130
5722	M.Xujamkulov MFY	1	t	130
5723	Mexrobod MFY	1	t	130
5724	Munchoktepa MFY	1	t	130
5725	Mustakillik MFY	1	t	130
5726	Neftchi MFY	1	t	130
5727	Navbaxor MFY	1	t	130
5728	Oqsoy MFY	1	t	130
5729	Oqtom MFY	1	t	130
5730	Oqjar QFY	1	t	130
5731	Oqqopchig`ay QFY	1	t	130
5732	O`zbekiston 5 yiligi MFY	1	t	130
5733	O`zbekiston QFY	1	t	130
5734	Pastxam MFY	1	t	130
5735	Paxtaobod MFY	1	t	130
5736	Qumqo`rg`on QFY	1	t	130
5737	Sherozi MFY	1	t	130
5738	T.Muqimov MFY	1	t	130
5739	Tebat MFY	1	t	130
5740	Tarvuzpoya MFY	1	t	130
5741	Tayfang MFY	1	t	130
5742	Tuda MFY	1	t	130
5743	Ulug`bek MFY	1	t	130
5744	UYaS MFY	1	t	130
5745	Xalaki MFY	1	t	130
5746	Xalkobod MFY	1	t	130
5747	Xuja kishlok MFY	1	t	130
5748	Xujamulki MFY	1	t	130
5749	Xurriyat MFY	1	t	130
5750	Yangi avlod MFY	1	t	130
5751	Yangi kishlok MFY	1	t	130
5752	Yangi shaxar MFY	1	t	130
5753	Yangier MFY	1	t	130
5754	Yangiobod MFY	1	t	130
5755	Yangixayot MFY	1	t	130
5756	Yuqori kakaydi QFY	1	t	130
5757	A.Ikromov MFY	1	t	131
5758	A.Navoiy MFY	1	t	131
5759	At-Termiziy MFY	1	t	131
5760	Avjun MFY	1	t	131
5761	Beshqo`ton QFY	1	t	131
5762	Boldir MFY	1	t	131
5763	Boldir QFY	1	t	131
5764	Bo`ston (Jamoatchi) MFY	1	t	131
5765	Ch.Quvondiqov-1 MFY	1	t	131
5766	Ch.Quvondiqov-2 MFY	1	t	131
5767	Chegarachi MFY	1	t	131
5768	Dehibolo-Nazariy MFY	1	t	131
5769	Dehqonobod MFY	1	t	131
5770	Darband MFY	1	t	131
5771	Do`stlik MFY	1	t	131
5772	Duoba MFY	1	t	131
5773	E.Jo`raev MFY	1	t	131
5774	Fayziobod MFY	1	t	131
5775	Gagarin MFY	1	t	131
5776	Guliston MFY	1	t	131
5777	Guliston QFY	1	t	131
5778	Mustaqillik MFY	1	t	131
5779	Muzrabot MFY	1	t	131
5780	Muzrabot QFY	1	t	131
5781	N.Mengliev MFY	1	t	131
5782	Navbahor QFY	1	t	131
5783	Navro`z MFY	1	t	131
5784	Obodon QFY	1	t	131
5785	Olachapon (Jamoatchi) MFY	1	t	131
5786	Oltinko`l MFY	1	t	131
5787	Paxtakor MFY	1	t	131
5788	Q.Qurbonova MFY	1	t	131
5789	Qahramon MFY	1	t	131
5790	Qizilolma MFY	1	t	131
5791	Qora-kamar QFY	1	t	131
5792	Qozoyoqli MFY	1	t	131
5793	Sh.Boboev MFY	1	t	131
5794	Sho`rob MFY	1	t	131
5795	Sho`rob QFY	1	t	131
5796	Soppollitepa MFY	1	t	131
5797	X.Jo`raev MFY	1	t	131
5798	Xalqobod QFY MFY	1	t	131
5799	Yangier MFY	1	t	131
5800	Yangiobod MFY	1	t	131
5801	Z.Nozimov MFY	1	t	131
5802	Z.Qo`ldoshev MFY	1	t	131
5803	Botosh MFY	1	t	132
5804	Ipok MFY	1	t	132
5805	A.Bo`taev MFY	1	t	132
5806	Besh bola pahlavon MFY	1	t	132
5807	Barkamol avlod MFY	1	t	132
5808	Bibizaynab MFY	1	t	132
5809	Chep MFY	1	t	132
5810	Chep QFY	1	t	132
5811	Chinor MFY	1	t	132
5812	Do`goba QFY	1	t	132
5813	Dugoba MFY	1	t	132
5814	Ekraz MFY	1	t	132
5815	Gulchechak MFY	1	t	132
5816	Guliston MFY	1	t	132
5817	Jindibuloq MFY	1	t	132
5818	Jiyanbobo MFY	1	t	132
5819	Jobu MFY	1	t	132
5820	Jobu-1 MFY	1	t	132
5821	Kaptarxona MFY	1	t	132
5822	Karsagan MFY	1	t	132
5823	Korlik MFY	1	t	132
5824	Ko`sh archa MFY	1	t	132
5825	M.Omonov MFY	1	t	132
5826	Madaniyat MFY	1	t	132
5827	Markaz MFY	1	t	132
5828	Marmin MFY	1	t	132
5829	Mingchinor MFY	1	t	132
5830	Mirshodi QFY	1	t	132
5831	Mirshodi MFY	1	t	132
5832	Mo`minkul MFY	1	t	132
5833	Must.10-yilligi MFY	1	t	132
5834	Navro`z MFY	1	t	132
5835	Obshir (Jamoatchi) MFY	1	t	132
5836	Oltinsoy QFY	1	t	132
5837	Oq-oltin QFY	1	t	132
5838	Oqarbulok MFY	1	t	132
5839	Oqarbulok QFY	1	t	132
5840	Ovchi MFY	1	t	132
5841	Qiziltepa MFY	1	t	132
5842	Qoratepa MFY	1	t	132
5843	Qorliq QFY	1	t	132
5844	Qumpaykal MFY	1	t	132
5845	Qurama-1 MFY	1	t	132
5846	Qurama-2 MFY	1	t	132
5847	Sayrak MFY	1	t	132
5848	Shakar.qamish MFY	1	t	132
5849	Shoxcha MFY	1	t	132
5850	To`xtamish MFY	1	t	132
5851	Vaxshivor QFY	1	t	132
5852	Vaxshivor-1 MFY	1	t	132
5853	Vaxshivor-2 MFY	1	t	132
5854	Xalqobod MFY	1	t	132
5855	Xayrandara MFY	1	t	132
5856	Xidirsho MFY	1	t	132
5857	Xo`jaipok MFY	1	t	132
5858	Xo`jasoat QFY	1	t	132
5859	Xo`jasoat-2 MFY	1	t	132
5860	Yakka tut MFY	1	t	132
5861	Yangi qurilish MFY	1	t	132
5862	Yangiariq MFY	1	t	132
5863	Yangiobod MFY	1	t	132
5864	Zardaqul MFY	1	t	132
5865	A.Navoiy MFY	1	t	133
5866	Aeroport MFY	1	t	133
5867	Barlos MFY	1	t	133
5868	Birlik	1	t	133
5869	Birlik MFY	1	t	133
5870	Bodomzor MFY	1	t	133
5871	Bodomzor QFY	1	t	133
5872	Bog`isamarqand (Jamoatchi) MFY	1	t	133
5873	Buyrapo`sh MFY	1	t	133
5874	Chinor MFY	1	t	133
5875	Daragiston (Jamoatchi) MFY	1	t	133
5876	Do`stlik MFY	1	t	133
5877	Do`stlik MFY	1	t	133
5878	Erkin MFY	1	t	133
5879	Erkin QFY	1	t	133
5880	Erman MFY	1	t	133
5881	Esoqi MFY	1	t	133
5882	Fozilko`chdi MFY	1	t	133
5883	G`alaba MFY	1	t	133
5884	g`ayrat MFY	1	t	133
5885	Galabutta MFY	1	t	133
5886	Galabutta MFY	1	t	133
5887	Gazarak QFY	1	t	133
5888	Gazarik MFY	1	t	133
5889	Gulshan MFY	1	t	133
5890	Kenguzar MFY	1	t	133
5891	Ko`lob MFY	1	t	133
5892	M.Ulug`bek MFY	1	t	133
5893	Madaniyat MFY	1	t	133
5894	Madaniyat QFY	1	t	133
5895	Navro`z MFY	1	t	133
5896	Navro`z QFY	1	t	133
5897	Nilova MFY	1	t	133
5898	Nilu (Jamoatchi) MFY	1	t	133
5899	Olmazor MFY	1	t	133
5900	Oxunbobev QFY	1	t	133
5901	Oxunboboev MFY	1	t	133
5902	Oxunboboev MFY	1	t	133
5903	Oxunbobov MFY	1	t	133
5904	O`zbekiston MFY	1	t	133
5905	O`zgarish MFY	1	t	133
5906	Paxtakor MFY	1	t	133
5907	Pistamozor MFY	1	t	133
5908	Qorasuv MFY	1	t	133
5909	Qo`shchinor MFY	1	t	133
5910	Qo`shchinor QFY	1	t	133
5911	Qulmozor MFY	1	t	133
5912	S.Raximov MFY	1	t	133
5913	Sangardak MFY	1	t	133
5914	Sangardak QFY	1	t	133
5915	Sarijar MFY	1	t	133
5916	Sarixo`y MFY	1	t	133
5917	Shoqishloq MFY	1	t	133
5918	Shoximardon MFY	1	t	133
5919	So`fiyon MFY	1	t	133
5920	Tolpakchinor MFY	1	t	133
5921	Tamshush MFY\r\n	1	t	138
5922	Tirgaron MFY	1	t	133
5923	Tokchiyon MFY	1	t	133
5924	Torto`li MFY	1	t	133
5925	Xovzqoq MFY	1	t	133
5926	Xufar MFY	1	t	133
5927	Xurvatan MFY	1	t	133
5928	Y.Oxunbobo?v MFY	1	t	133
5929	Yangihayot MFY	1	t	133
5930	Yangiobod MFY	1	t	133
5931	Yangiqishloq MFY	1	t	133
5932	Yangiturmush MFY	1	t	133
5933	A.Navoiy MFY	1	t	134
5934	A.Temur MFY	1	t	134
5935	Amu-sohili MFY	1	t	134
5936	At-Termiziy MFY	1	t	134
5937	Ayritom MFY	1	t	134
5938	Chegara MFY	1	t	134
5939	Do`stlik MFY	1	t	134
5940	Gulbahor MFY	1	t	134
5941	Guliston MFY	1	t	134
5942	Istiqlol MFY	1	t	134
5943	Jo`yijangal MFY	1	t	134
5944	Kokildor-ota MFY	1	t	134
5945	M.Eshtemirov MFY	1	t	134
5946	Manguzar MFY	1	t	134
5947	Mustaqilik MFY	1	t	134
5948	Namuna MFY	1	t	134
5949	Navro`z MFY	1	t	134
5950	Orol MFY	1	t	134
5951	Parandachilik MFY	1	t	134
5952	Patakesar MFY	1	t	134
5953	Pattakesar QFY	1	t	134
5954	Paxtaobod QFY	1	t	134
5955	Qahramon MFY	1	t	134
5956	Qoraxon MFY	1	t	134
5957	Qo`ng`irot MFY	1	t	134
5958	Quyoshli yurt MFY	1	t	134
5959	Sh.Rashidov MFY	1	t	134
5960	Sharq MFY	1	t	134
5961	Soliobod MFY	1	t	134
5962	Tinchlik MFY	1	t	134
5963	Uchkizil MFY	1	t	134
5964	Uchqizil QFY	1	t	134
5965	Xalqabod MFY	1	t	134
5966	Xotinrabot QFY	1	t	134
5967	Yangi ariq QFY	1	t	134
5968	Yangi hayot MFY	1	t	134
5969	A.Jomiy MFY	1	t	135
5970	A.Navoiy MFY	1	t	135
5971	Alpomish MFY	1	t	135
5972	Amu Soxillari MFY	1	t	135
5973	Baynalminal MFY	1	t	135
5974	Bog`ishamol MFY	1	t	135
5975	Bo`ston MFY	1	t	135
5976	Do`stlik MFY	1	t	135
5977	Farxod MFY	1	t	135
5978	Garm MFY	1	t	135
5979	Guliston MFY	1	t	135
5980	Ibn.Sino MFY	1	t	135
5981	Ishchilar MFY	1	t	135
5982	Jayxun MFY	1	t	135
5983	Juyjangal MFY	1	t	135
5984	Katta-bog MFY	1	t	135
5985	Mexrobod MFY	1	t	135
5986	Ma`rifat MFY	1	t	135
5987	Navruz MFY	1	t	135
5988	Ozodlik MFY	1	t	135
5989	O`zbekiston MFY	1	t	135
5990	Pattakesar MFY	1	t	135
5991	R.Uzoqova MFY	1	t	135
5992	Shifokor MFY	1	t	135
5993	Shodlik MFY	1	t	135
5994	Surxon soxili MFY	1	t	135
5995	Temir yulchi MFY	1	t	135
5996	Tuprokkurgon MFY	1	t	135
5997	Uchkun MFY	1	t	135
5998	Yulduz MFY	1	t	135
5999	Beshkapa MFY	1	t	136
6000	Bobotog` QFY	1	t	136
6001	Chaqar MFY	1	t	136
6002	Chinor MFY	1	t	136
6003	Chosh (Jamoatchi) MFY	1	t	136
6004	Dehqon MFY	1	t	136
6005	Do`stlik MFY	1	t	136
6006	Fayzabod MFY	1	t	136
6007	Fayzova MFY	1	t	136
6008	Fayzova QFY	1	t	136
6009	Guliston MFY	1	t	136
6010	Istiqlol MFY	1	t	136
6011	Jonchekka MFY	1	t	136
6012	Jonchekka QFY	1	t	136
6013	K.Jonchekka MFY	1	t	136
6014	Karsh (Jamoatchi) MFY	1	t	136
6015	M.Turmush MFY	1	t	136
6016	Mehnat MFY	1	t	136
6017	Maland (Jamoatchi MFY)	1	t	136
6018	Malandiyon MFY	1	t	136
6019	Mustaqillik MFY	1	t	136
6020	Mustaqillik MFY	1	t	136
6021	N.Ramazonov MFY	1	t	136
6022	Obizarang MFY	1	t	136
6023	Oqmachit MFY	1	t	136
6024	Oqostona MFY	1	t	136
6025	Oqostona QFY	1	t	136
6026	Oqtumshuq MFY	1	t	136
6027	O`lanqul MFY	1	t	136
6028	O`zbekiston MFY	1	t	136
6029	Qarashi MFY	1	t	136
6030	Serharakat MFY	1	t	136
6031	Tolpakchinor QFY	1	t	136
6032	Tojikobod MFY	1	t	136
6033	Toltug`ay MFY	1	t	136
6034	Tomchi (Jamoatchi) MFY	1	t	136
6035	U.Yusupov MFY	1	t	136
6036	Uzun QFY	1	t	136
6037	Uzunqishloq MFY	1	t	136
6038	X.Qaxramon MFY	1	t	136
6039	Xonjiza MFY	1	t	136
6040	Xonjiza QFY	1	t	136
6041	Xursand MFY	1	t	136
6042	Yangi obod MFY	1	t	136
6043	Yangi ro`zg`or MFY	1	t	136
6044	Yangi shahar MFY	1	t	136
6045	Yangikuch MFY	1	t	136
6046	Yangixayot MFY	1	t	136
6047	Yangiyo`l MFY	1	t	136
6048	Yor Hakimov MFY	1	t	136
6049	Yoshlik MFY	1	t	136
6050	Oqqo`rg`on QFY	1	t	137
6051	A. Ikromov MFY	1	t	137
6052	Ayinni MFY	1	t	137
6053	Balxiguzar MFY	1	t	137
6054	Boybuloq MFY	1	t	137
6055	Boyqishloq MFY	1	t	137
6056	Bo`ston QFY	1	t	137
6057	Chag`atoy MFY	1	t	137
6058	Chinobod MFY	1	t	137
6059	Chinobod QFY	1	t	137
6060	Chorbog` MFY	1	t	137
6061	Cho`mishli MFY	1	t	137
6062	Cho`yinchi MFY	1	t	137
6063	Chuqurko`l MFY	1	t	137
6064	Do`stlik MFY	1	t	137
6065	G`alaba MFY	1	t	137
6066	g`ambur MFY	1	t	137
6067	g`o`rin Gilambob MFY	1	t	137
6068	g`urjak MFY	1	t	137
6069	g`urjak-2 MFY	1	t	137
6070	Galaguzar MFY	1	t	137
6071	Guliston MFY	1	t	137
6072	Hakimobod MFY	1	t	137
6073	Istiqbol MFY	1	t	137
6074	Katta xayot MFY	1	t	137
6075	Kilkon MFY	1	t	137
6076	Laylagon MFY	1	t	137
6077	Mehnatobod MFY	1	t	137
6078	Navbog` MFY	1	t	137
6079	Navbur MFY	1	t	137
6080	Oqqo`rg`on MFY	1	t	137
6081	Oqtepa MFY	1	t	137
6082	Oxunboboev MFY	1	t	137
6083	Paxtaobod MFY	1	t	137
6084	Poshxurt MFY	1	t	137
6085	Qishloqbozor MFY	1	t	137
6086	Qizil olma MFY	1	t	137
6087	Qorabog` MFY	1	t	137
6088	Qulluqsho MFY	1	t	137
6089	Rabatak QFY	1	t	137
6090	Seplon MFY	1	t	137
6091	Seplon QFY	1	t	137
6092	Sariqamish MFY	1	t	137
6093	Sariqamish QFY	1	t	137
6094	Sherobod MFY	1	t	137
6095	Tallashqon QFY	1	t	137
6096	Taroqli MFY	1	t	137
6097	Uch yog`och MFY	1	t	137
6098	Vandob (Jamoatchi) MFY	1	t	137
6099	Xo`jaqiya-1 MFY	1	t	137
6100	Xo`jaqiya-2 MFY	1	t	137
6101	Xo`jgi MFY	1	t	137
6102	Yangi turmush QFY	1	t	137
6103	Yangiariq MFY	1	t	137
6104	Yoshlik MFY	1	t	137
6105	Zarabog` MFY	1	t	137
6106	Zarabog`QFY	1	t	137
6107	5 yillik MFY	1	t	138
6108	8-mart. MFY	1	t	138
6109	A.Navoiy MFY	1	t	138
6110	Baxshitepa 1 MFY	1	t	138
6111	Baxshitepa MFY	1	t	138
6112	Baxtlit?pa QFY	1	t	138
6113	Bobotog` MFY	1	t	138
6114	Bobur MFY	1	t	138
6115	Bo`ston MFY	1	t	138
6116	Dalvarzin 1 MFY	1	t	138
6117	Dalvarzin 2 MFY	1	t	138
6118	Dalvarzin QFY	1	t	138
6119	Do`stlik MFY	1	t	138
6120	Elboyon MFY	1	t	138
6121	Elboyon SHFY	1	t	138
6122	Elobod QFY	1	t	138
6123	Guliston MFY	1	t	138
6124	Ibn Sino MFY	1	t	138
6125	Jaloir QFY	1	t	138
6126	Joloir MFY	1	t	138
6127	Joyilma MFY	1	t	138
6128	Kakan MFY	1	t	138
6129	Kakaydi MFY	1	t	138
6130	Konobod MFY	1	t	138
6131	Ko`klam MFY	1	t	138
6132	Kultepa 1 MFY	1	t	138
6133	Kultepa MFY	1	t	138
6134	Laylakxona MFY	1	t	138
6135	Navro`z MFY	1	t	138
6136	Obodon MFY	1	t	138
6137	Olatemir MFY	1	t	138
6138	Oqkamar MFY	1	t	138
6139	Oqqo`rg`on MFY	1	t	138
6140	Oqtumshuq MFY	1	t	138
6141	Oxunboboev QFY	1	t	138
6142	Oynakul MFY	1	t	138
6143	Ozod MFY	1	t	138
6144	O`rmoncha (Jamoatchi) MFY	1	t	138
6145	Polvontosh MFY	1	t	138
6146	Qorariq MFY	1	t	138
6147	Qo`ldosh MFY	1	t	138
6148	Qo`ldosh QFY	1	t	138
6149	Qo`shtegirmon MFY	1	t	138
6150	Serg`ayrat MFY	1	t	138
6151	Saksonkappa MFY	1	t	138
6152	Saurtera MFY	1	t	138
6153	Savur QFY	1	t	138
6154	Shakarko`l MFY	1	t	138
6155	Shaldiroq MFY	1	t	138
6156	Sho`rchi QFY	1	t	138
6157	Sovjiranbobo MFY	1	t	138
6158	Soxibkor QFY	1	t	138
6159	Tolli MFY	1	t	138
6160	Tula MFY	1	t	138
6161	Xayrobod MFY	1	t	138
6162	Xojibobo MFY	1	t	138
6163	Xurlik MFY	1	t	138
6164	Yakkabog` MFY	1	t	138
6165	Yalti MFY	1	t	138
6166	Yangiariq MFY	1	t	138
6167	Yangibozor QFY	1	t	138
6168	Yorug`lik MFY	1	t	138
6169	Yoshgayrat MFY	1	t	138
6170	Zarbdor MFY	1	t	138
6171	1-Boyovut QFY	1	t	139
6172	A. Temur MFY	1	t	139
6173	A.Navoiy-1 MFY	1	t	139
6174	B. Umurzokov MFY	1	t	139
6175	Bekat MFY	1	t	139
6176	Beruniy MFY	1	t	139
6177	Boyovut SHFY	1	t	139
6178	Bunyodkor MFY	1	t	139
6179	Dehqonobod QFY	1	t	139
6180	Darvozakir QFY	1	t	139
6181	Do`stlik MFY	1	t	139
6182	Do`stlik MFY	1	t	139
6183	Do`stlik QFY	1	t	139
6184	Farhod MFY	1	t	139
6185	Gallakor QFY	1	t	139
6186	Gulbog MFY	1	t	139
6187	Istiqlol MFY	1	t	139
6188	J.Usmonov QFY	1	t	139
6189	Jo`langar MFY	1	t	139
6190	Laylakkul QFY	1	t	139
6191	Ma`naviyat MFY	1	t	139
6192	Madaniyat QFY	1	t	139
6193	Madaniyat MFY	1	t	139
6194	Markaz MFY	1	t	139
6195	Mingchinor QFY	1	t	139
6196	Mirishkor MFY	1	t	139
6197	Muqumiy MFY	1	t	139
6198	N. Mahmudov MFY	1	t	139
6199	Navbahor MFY	1	t	139
6200	Navoiy-2 MFY	1	t	139
6201	Navoiy-3 MFY	1	t	139
6202	Navro`z MFY	1	t	139
6203	Olmazor QFY	1	t	139
6204	Olmazor MFY	1	t	139
6205	Ozodlik MFY	1	t	139
6206	O`zbekiston MFY	1	t	139
6207	Paxtakor MFY	1	t	139
6208	Qarapchi MFY	1	t	139
6209	S`ayniy MFY	1	t	139
6210	Sarmich MFY	1	t	139
6211	Sh.Rashidov MFY	1	t	139
6212	Shirin QFY	1	t	139
6213	Sovotobod MFY	1	t	139
6214	Tinchlik QFY	1	t	139
6215	U. Yusupov MFY	1	t	139
6216	Uchturgon MFY	1	t	139
6217	Umurzoqobod MFY	1	t	139
6218	Usmonobod QFY	1	t	139
6219	Usmonobod MFY	1	t	139
6220	Yangibo`ston MFY	1	t	139
6221	Yangiobod MFY	1	t	139
6222	Etti urug` MFY	1	t	140
6223	A .Turdiev QFY	1	t	140
6224	A.Qahhor MFY	1	t	140
6225	A.Sultonov MFY	1	t	140
6226	A.Yassaviy MFY	1	t	140
6227	Beshbuloq MFY	1	t	140
6228	Beshbuloq QFY	1	t	140
6229	Baxmal MFY	1	t	140
6230	Birlashgan MFY	1	t	140
6231	Birlashgan MFY	1	t	140
6232	Boyovut MFY	1	t	140
6233	Chortok MFY	1	t	140
6234	Chortoq QFY	1	t	140
6235	Chorvador MFY	1	t	140
6236	Dehqonobod SHFY	1	t	140
6237	Do`stlik MFY	1	t	140
6238	Do`stlik MFY	1	t	140
6239	Furqat MFY	1	t	140
6240	G.Yunusov MFY	1	t	140
6241	Islomobod MFY	1	t	140
6242	Islomobod MFY	1	t	140
6243	M.Zokirov MFY	1	t	140
6244	Mevazor MFY	1	t	140
6245	Madaniyat MFY	1	t	140
6246	Mustaqillik MFY	1	t	140
6247	Navoiy MFY	1	t	140
6248	Oq oltin MFY	1	t	140
6249	Oltin O`rda QFY	1	t	140
6250	Oltin Tepa QFY	1	t	140
6251	Sh.Eshonqulov MFY	1	t	140
6252	Shark haqiqati MFY	1	t	140
6253	Soxilobod QFY	1	t	140
6254	Soyibobod QFY	1	t	140
6255	T`azizov MFY	1	t	140
6256	Tajribakor MFY	1	t	140
6257	Turkiston MFY	1	t	140
6258	Turkovul MFY	1	t	140
6259	Uyuvli MFY	1	t	140
6260	O`zbekiston MFY	1	t	140
6261	O`zbekiston MFY	1	t	140
6262	O`zbekiston MFY	1	t	140
6263	X.Olimjon 1-MFY	1	t	140
6264	X.Olimjon 2-MFY	1	t	140
6265	Xalqobod MFY	1	t	140
6266	Xumo QFY	1	t	140
6267	Yangi Hayot MFY	1	t	140
6268	Yulduz - 1 MFY	1	t	140
6269	Zarbdor MFY	1	t	140
6270	Zarbdor QFY	1	t	140
6271	Ahillik MFY	1	t	141
6272	Baxor QFY	1	t	141
6273	Bo`ston MFY	1	t	141
6274	Do`stlik QFY	1	t	141
6275	Farxod MFY	1	t	141
6276	Istiqlol MFY	1	t	141
6277	Madaniyat MFY	1	t	141
6278	Muqimiy MFY	1	t	141
6279	Namuna MFY	1	t	141
6280	Navbaxor MFY	1	t	141
6281	Sayqal MFY	1	t	141
6282	Sh.Rashidov MFY	1	t	141
6283	T`axmedov MFY	1	t	141
6284	Taraqqiyot MFY	1	t	141
6285	U.Yusupov MFY	1	t	141
6286	Ulug`obod QFY	1	t	141
6287	Yangi hayot MFY	1	t	141
6288	Beruniy MFY	1	t	142
6289	Birlashgan QFY	1	t	142
6290	Bog`iston MFY	1	t	142
6291	Boxoriston QFY	1	t	142
6292	Dehqonobod MFY	1	t	142
6293	Do`ngariq MFY	1	t	142
6294	Juvonsiyroq MFY	1	t	142
6295	M.Ulug`bek MFY	1	t	142
6296	Mexnatobod QFY	1	t	142
6297	Mirzacho`l QFY	1	t	142
6298	Navbaxor QFY	1	t	142
6299	Navro`z MFY	1	t	142
6300	Nurafshon QFY	1	t	142
6301	Oqoltin MFY	1	t	142
6302	Oqoltin QFY	1	t	142
6303	Oydin MFY	1	t	142
6304	T`ahmedov MFY	1	t	142
6305	Toshkent MFY	1	t	142
6306	Toshkent QFY	1	t	142
6307	U.Yusupov MFY	1	t	142
6308	Yangi hayot-9 MFY	1	t	142
6309	Yangiovul MFY	1	t	142
6310	Yangihayot MFY	1	t	142
6311	Yo`ldoshobod QFY	1	t	142
6312	A.Ikromov MFY	1	t	143
6313	A.Navoiy MFY	1	t	143
6314	A.Yassaviy MFY	1	t	143
6315	Ahillik QFY	1	t	143
6316	Andijon QFY	1	t	143
6317	Bog`iston MFY	1	t	143
6318	Bo`ston QFY	1	t	143
6319	Do`stlik MFY	1	t	143
6320	Farg`ona SHFY	1	t	143
6321	G.G`ulom MFY	1	t	143
6322	G.G`ulom MFY	1	t	143
6323	G`alaba MFY	1	t	143
6324	Mustaqillik MFY	1	t	143
6325	Obod MFY	1	t	143
6326	S.Rahimov MFY	1	t	143
6327	Sardoba SHFY	1	t	143
6328	Shodlik QFY	1	t	143
6329	Sobirobod MFY	1	t	143
6330	U.Yusupov MFY	1	t	143
6331	Uchtom MFY	1	t	143
6332	Yangi hayot MFY	1	t	143
6333	Z.Bobur MFY	1	t	143
6334	Zarafshon MFY	1	t	143
6335	"Axchob" MFY	1	t	144
6336	"Baxmal" MFY	1	t	144
6337	"Boltoy" MFY	1	t	144
6338	"Do`stlik" MFY	1	t	144
6339	"Gulbuloq" MFY	1	t	144
6340	"Guliston" MFY	1	t	144
6341	"Istiqlol" QFY	1	t	144
6342	"Ittifoq" MFY	1	t	144
6343	"Ittifoq" QFY	1	t	144
6344	"Kalpe" MFY	1	t	144
6345	"Mustaqillik" MFY	1	t	144
6346	"Namuna" MFY	1	t	144
6347	"Navqiron" MFY	1	t	144
6348	"Nurmatobod" MFY	1	t	144
6349	"Nurota" QFY	1	t	144
6350	"Obodon" MFY	1	t	144
6351	"Olg`abos" MFY	1	t	144
6352	"Otamakon" MFY	1	t	144
6353	"O`zbekiston" MFY	1	t	144
6354	"O`zbekiston" QFY	1	t	144
6355	"Parpi ota" MFY	1	t	144
6356	"Paxtakon" MFY	1	t	144
6357	"Paxtaobod" MFY	1	t	144
6358	"Paymard" MFY	1	t	144
6359	"Qorjou" MFY	1	t	144
6360	"Qozoqovul" MFY	1	t	144
6361	"Qumovul" MFY	1	t	144
6362	"Qurultoy" MFY	1	t	144
6363	"Robot" MFY	1	t	144
6364	"Sentob" MFY	1	t	144
6365	"Saritepa" MFY	1	t	144
6366	"Sayxun" SHFY	1	t	144
6367	"Sh. Rashidov" MFY	1	t	144
6368	"Shal-Kushek" MFY	1	t	144
6369	"Shodlik" MFY	1	t	144
6370	"Sho`ro`zak" MFY	1	t	144
6371	"Sho`ro`zak" SHFY	1	t	144
6372	"Soxil" SHFY	1	t	144
6373	"Turkovul" MFY	1	t	144
6374	"Turon" MFY	1	t	144
6375	"Uchqun" MFY	1	t	144
6376	"Xisor" MFY	1	t	144
6377	"Yangi-Hayot" MFY	1	t	144
6378	"Yangi-Hayot" QFY	1	t	144
6379	"Yoshlik" MFY	1	t	144
6380	"Yulduz" MFY	1	t	144
6381	"Zarbdor" MFY	1	t	144
6382	"Zarbdor-1" MFY	1	t	144
6383	Baxmal MFY	1	t	145
6384	Birlashgan MFY	1	t	145
6385	Bog`ishamol MFY	1	t	145
6386	Bo`ston MFY	1	t	145
6387	Cho`lquvar QFY	1	t	145
6388	Chubor MFY	1	t	145
6389	Do`stlik MFY	1	t	145
6390	F.Xo`jaev MFY	1	t	145
6391	Guliston QFY	1	t	145
6392	Gulzor QFY	1	t	145
6393	Gumbaz MFY	1	t	145
6394	Manas MFY	1	t	145
6395	Navoiy MFY	1	t	145
6396	Navro`z MFY	1	t	145
6397	Paxtakor MFY	1	t	145
6398	Paxtaobod SHFY	1	t	145
6399	Qo`rg`ontepa QFY	1	t	145
6400	Ravot MFY	1	t	145
6401	S.Raximov MFY	1	t	145
6402	Ulug`bek MFY	1	t	145
6403	Ulug`bek MFY	1	t	145
6404	H.Olimjon MFY	1	t	145
6405	Xalqobod MFY	1	t	145
6406	Yangiobod QFY	1	t	145
6407	Yangiqishloq QFY	1	t	145
6408	Zomin MFY	1	t	145
6409	Zominlik MFY	1	t	145
6410	Bekjonov MFY	1	t	146
6411	Balki yogoch eli MFY	1	t	146
6412	Baxor-1 MFY	1	t	146
6413	Baxor-3 MFY	1	t	146
6414	Baxt shaxar	1	t	146
6415	Bogora MFY	1	t	146
6416	Boruxov MFY	1	t	146
6417	C.Raximov MFY	1	t	146
6418	Chultukay QFY	1	t	146
6419	Dehqonobod MFY	1	t	146
6420	Dehqonobod MFY	1	t	146
6421	Do`stlik-2 MFY	1	t	146
6422	Do`stlik-6 MFY	1	t	146
6423	Furqat MFY	1	t	146
6424	Kozokovul MFY	1	t	146
6425	Quyosh MFY	1	t	146
6426	Malik QFY	1	t	146
6427	Malik MFY	1	t	146
6428	Navbaxor MFY	1	t	146
6429	Navoiy MFY	1	t	146
6430	Navro`z MFY	1	t	146
6431	Navro`z-3 MFY	1	t	146
6432	Oq-yo`l MFY	1	t	146
6433	Paxtakor MFY	1	t	146
6434	Paxtakor-4 MFY	1	t	146
6435	Paxtazor QFY	1	t	146
6436	R. Jurabaev MFY	1	t	146
6437	S.Raximov MFY	1	t	146
6438	Samarqand MFY	1	t	146
6439	Sh.Jumabaev MFY	1	t	146
6440	Sh.Rashidov MFY	1	t	146
6441	Shirin-5 MFY	1	t	146
6442	Sholikor QFY	1	t	146
6443	Sholikor MFY	1	t	146
6444	Sirdaryo QFY	1	t	146
6445	Sirdaryo MFY	1	t	146
6446	Sirdaryo shaxar	1	t	146
6447	Tinchlik-1 MFY	1	t	146
6448	Turkiston MFY	1	t	146
6449	Turon QFY	1	t	146
6450	U.Yusupov QFY	1	t	146
6451	Ulug`bek MFY	1	t	146
6452	O`zbekiston MFY	1	t	146
6453	Haqiqat QFY	1	t	146
6454	Haqiqat MFY	1	t	146
6455	Haqiqat-2 MFY	1	t	146
6456	Haqiqat-7 MFY	1	t	146
6457	Xalkobod QFY	1	t	146
6458	Hamza MFY	1	t	146
6459	Yangiobod MFY	1	t	146
6460	Yoshlar MFY	1	t	146
6461	Yoshlik-2 MFY	1	t	146
6462	Yoshlik-4 MFY	1	t	146
6463	Ziyokor MFY	1	t	146
6464	Amur Temur MFY	1	t	147
6465	ashi MFY	1	t	147
6466	Binokor QFY	1	t	147
6467	Bog`iston MFY	1	t	147
6468	Boymurodobod MFY	1	t	147
6469	Chamanzor QFY	1	t	147
6470	Chamanzor MFY	1	t	147
6471	Chambil MFY	1	t	147
6472	Chiroy MFY	1	t	147
6473	Do`stlik MFY	1	t	147
6474	Do`stlik MFY	1	t	147
6475	Farxod QFY	1	t	147
6476	Fayziobod MFY	1	t	147
6477	Gulbaxor QFY	1	t	147
6478	Gulbaxor MFY	1	t	147
6479	Islom MFY	1	t	147
6480	Istiqlol MFY	1	t	147
6481	Karvonsaroy-1 MFY	1	t	147
6482	Karvonsaroy-2 MFY	1	t	147
6483	Kaxramon QFY	1	t	147
6484	Qayirma MFY	1	t	147
6485	Kayirma MFY	1	t	147
6486	Koraqum MFY	1	t	147
6487	Kukoni .Karapchi MFY	1	t	147
6488	Qo`shqand MFY	1	t	147
6489	Kuzi-Takaev MFY	1	t	147
6490	Mustaqillik MFY	1	t	147
6491	Navoiy MFY	1	t	147
6492	Navoiy MFY	1	t	147
6493	Navro`z MFY	1	t	147
6494	Okchangal MFY	1	t	147
6495	Parchayuz MFY	1	t	147
6496	Pastki-Kayirma MFY	1	t	147
6497	Paxtakor QFY	1	t	147
6498	Rugund MFY	1	t	147
6499	Sharkobod MFY	1	t	147
6500	Soxibkor QFY	1	t	147
6501	Soxibkor MFY	1	t	147
6502	Tinchlik MFY	1	t	147
6503	Turkiston QFY	1	t	147
6504	Turkiston MFY	1	t	147
6505	Uvok MFY	1	t	147
6506	O`zbekiston Tukinchiligi MFY	1	t	147
6507	Xovos Sh.FY	1	t	147
6508	Xovotog` QFY	1	t	147
6509	Xusnobod QFY	1	t	147
6510	Zafarobod QFY	1	t	147
6511	A.Qodiriy MFY	1	t	148
6512	A.Temur MFY	1	t	148
6513	Do`stlik MFY	1	t	148
6514	Farhod MFY	1	t	148
6515	M.Ulugbek MFY	1	t	148
6516	Nurobod MFY	1	t	148
6517	A.Jomiy MFY	1	t	149
6518	Binokor MFY	1	t	149
6519	Ma`rifat MFY	1	t	149
6520	Navro`zobod MFY	1	t	149
6521	Obod yurt MFY	1	t	149
6522	Shodlik MFY	1	t	149
6523	T.Malik ify	1	t	149
6524	Z.Bobur MFY	1	t	149
6525	8-mart MFY	1	t	150
6526	Beruniy MFY	1	t	150
6527	Bobotog MFY	1	t	150
6528	Bogi Surx MFY	1	t	150
6529	Buston MFY	1	t	150
6530	Chigirik kurgoni MFY	1	t	150
6531	Chinniobod MFY	1	t	150
6532	Chotkol MFY	1	t	150
6533	Chotkol-1 MFY	1	t	150
6534	Dorilfunun MFY	1	t	150
6535	Do`stlik MFY	1	t	150
6536	g`Gulom MFY	1	t	150
6537	Geolog MFY	1	t	150
6538	Grum MFY	1	t	150
6539	Gulbog MFY	1	t	150
6540	Gulzor MFY	1	t	150
6541	Guzal MFY	1	t	150
6542	Hakkarman MFY	1	t	150
6543	Istiqlol MFY	1	t	150
6544	Jigariston MFY	1	t	150
6545	Karvon MFY	1	t	150
6546	Kimyogar-051 MFY	1	t	150
6547	Korabog MFY	1	t	150
6548	Kotogon MFY	1	t	150
6549	Krasnogorsk qo`rg`oni MFY	1	t	150
6550	KuktErak MFY	1	t	150
6551	LashkErak MFY	1	t	150
6552	Maydon MFY	1	t	150
6553	Mustakillik MFY	1	t	150
6554	Mustakillik-2 MFY	1	t	150
6555	Navbaxor MFY	1	t	150
6556	Navruz-1 MFY	1	t	150
6557	Navruz-2 MFY	1	t	150
6558	Nishbosh MFY	1	t	150
6559	Nurchi MFY	1	t	150
6560	Nurobod MFY	1	t	150
6561	Oblik MFY	1	t	150
6562	Obod MFY	1	t	150
6563	Opartak MFY	1	t	150
6564	Ozodlik MFY	1	t	150
6565	Said-ota MFY	1	t	150
6566	Samarchug MFY	1	t	150
6567	Soglom MFY	1	t	150
6568	TarakQiyot MFY	1	t	150
6569	Tolbulok MFY	1	t	150
6570	Ulugb?k MFY	1	t	150
6571	Yangi Bogi Surx MFY	1	t	150
6572	Yangi Gushsoy MFY	1	t	150
6573	Yangi Xayot MFY	1	t	150
6574	Yangiobod MFY	1	t	150
6575	Yoshlik MFY	1	t	150
6576	Zarubuloq MFY	1	t	150
6577	A.Mirzaev MFY	1	t	151
6578	A.Qozoqboev MFY	1	t	151
6579	Achamayli MFY	1	t	151
6580	Bekobod QFY	1	t	151
6581	Berdiboy MFY	1	t	151
6582	Beshyuz MFY	1	t	151
6583	Baxoriston MFY(jamoatchi)	1	t	151
6584	Baxoriston QFY	1	t	151
6585	Bobur Mirzo MFY	1	t	151
6586	Bog`ishomol MFY	1	t	151
6587	Bo`ston MFY	1	t	151
6588	Chanoq QFY	1	t	151
6589	Dexqonobod MFY	1	t	151
6590	Dalvarzin QFY	1	t	151
6591	Do`stlik MFY	1	t	151
6592	Farxod MFY	1	t	151
6593	Guliston MFY	1	t	151
6594	Guliston QFY	1	t	151
6595	Gulzor MFY	1	t	151
6596	Isfara MFY	1	t	151
6597	Istiqlol MFY	1	t	151
6598	Jumabozor QFY	1	t	151
6599	Mexnatobod QFY	1	t	151
6600	Madaniyat QFY	1	t	151
6601	Mallaboy MFY	1	t	151
6602	Nayman MFY	1	t	151
6603	Nazarboy MFY	1	t	151
6604	Oltin vodiy MFY	1	t	151
6605	Oqtepa MFY	1	t	151
6606	Oxunbobo?v QFY	1	t	151
6607	O`rikzor MFY	1	t	151
6608	O`zbekiston MFY	1	t	151
6609	O`zbekobod MFY	1	t	151
6610	Parchayuz MFY	1	t	151
6611	Pastki kerayit MFY	1	t	151
6612	Paxtakor MFY	1	t	151
6613	Pushkin QFY	1	t	151
6614	Qiyot QFY	1	t	151
6615	Qolg`ansir MFY	1	t	151
6616	Qora qo`yli MFY	1	t	151
6617	Qo`qoni MFY	1	t	151
6618	Qo`rg`on MFY	1	t	151
6619	Qushchi MFY	1	t	151
6620	Qushtamg`ali MFY	1	t	151
6621	Saryuz MFY	1	t	151
6622	Savrak MFY	1	t	151
6623	Shova MFY	1	t	151
6624	Terakzor MFY	1	t	151
6625	Taqachi MFY	1	t	151
6626	Turkman MFY	1	t	151
6627	Turon MFY(jamoatchi)	1	t	151
6628	Uyas MFY	1	t	151
6629	Xamza MFY	1	t	151
6630	Xonobod MFY(jamoatchi)	1	t	151
6631	Xos MFY	1	t	151
6632	Yangi Hayot QFY	1	t	151
6633	Yangibozor MFY	1	t	151
6634	Yoshlik MFY	1	t	151
6635	Yoshlik-2 MFY	1	t	151
6636	Zafar SHFY	1	t	151
6637	Ziyoli MFY	1	t	151
6638	Amentchi MFY	1	t	152
6639	A.Navoiy MFY	1	t	152
6640	Abbasov MFY	1	t	152
6641	Al-Xorazmiy MFY	1	t	152
6642	Andijon MFY	1	t	152
6643	Bobur MFY	1	t	152
6644	Bog`i shamol MFY	1	t	152
6645	Buloq ariq MFY	1	t	152
6646	Do`stlik MFY	1	t	152
6647	Farg`ona MFY	1	t	152
6648	Farxod MFY	1	t	152
6649	Jomiy MFY	1	t	152
6650	M.Turg`unboeva MFY	1	t	152
6651	Muqumiy MFY	1	t	152
6652	Mustaqillik MFY	1	t	152
6653	Muxammedov MFY	1	t	152
6654	Navro`z MFY	1	t	152
6655	Nurli yul MFY	1	t	152
6656	O`zbekiston MFY	1	t	152
6657	Paxtakor MFY	1	t	152
6658	Q.Farmanov MFY	1	t	152
6659	Q.To`rdiev MFY	1	t	152
6660	Rudakiy MFY	1	t	152
6661	S`ayniy MFY	1	t	152
6662	S.Raximov MFY	1	t	152
6663	Samarqand MFY	1	t	152
6664	Sh.Qo`ziboev MFY	1	t	152
6665	Shirin MFY	1	t	152
6666	Sirdaryo MFY	1	t	152
6667	Tinchlik MFY	1	t	152
6668	Turkiston MFY	1	t	152
6669	X.Olimjon MFY	1	t	152
6670	Yangi xayot MFY	1	t	152
6671	Yoshlik MFY	1	t	152
6672	Zafar MFY	1	t	152
6673	Achamayli Fayz-Baraka	1	t	153
6674	Achamayli MFY	1	t	153
6675	Beshkapa MFY	1	t	153
6676	Bo`ka MFY	1	t	153
6677	Bo`ka sh Madaniyat MFY	1	t	153
6678	Bo`ka sh. Guliston MFY	1	t	153
6679	Bo`ka sh. Navruz MFY	1	t	153
6680	Bo`ka sh. O`zbek MFY	1	t	153
6681	Bo`ka sh. Toshloq MFY	1	t	153
6682	Bo`ka sh. Yangiobod MFY	1	t	153
6683	Bo`ka sh.Do`stlik MFY	1	t	153
6684	Bo`ka sh.Yangihayot MFY	1	t	153
6685	Bo`ston QFY	1	t	153
6686	Buston MFY	1	t	153
6687	Chig`atoy QFY	1	t	153
6688	Cho`lobod MFY	1	t	153
6689	Dashtobod MFY	1	t	153
6690	Guliston MFY	1	t	153
6691	Guliston MFY	1	t	153
6692	Jag`albayli MFY	1	t	153
6693	Katta ravot MFY	1	t	153
6694	Kiyikchi MFY	1	t	153
6695	Kukorol MFY	1	t	153
6696	Kukorol QFY	1	t	153
6697	Mirzabek MFY	1	t	153
6698	Namuna QFY	1	t	153
6699	Navobod MFY	1	t	153
6700	Oltish MFY	1	t	153
6701	O`rta tepa MFY	1	t	153
6702	Parkent MFY	1	t	153
6703	Qoraq-uyli MFY	1	t	153
6704	Qoraq-uyli QFY	1	t	153
6705	Qoraquduq MFY	1	t	153
6706	Qo`chqors-uygan MFY	1	t	153
6707	Qo`ldoshtepa MFY	1	t	153
6708	Qo`shtepa QFY	1	t	153
6709	Quldiroq MFY	1	t	153
6710	Ramadon MFY	1	t	153
6711	Ravot MFY	1	t	153
6712	Ravot MFY	1	t	153
6713	Ravot QFY	1	t	153
6714	Samarqand MFY	1	t	153
6715	Turon QFY	1	t	153
6716	Xo`jaqurg`on MFY	1	t	153
6717	Yangiobod MFY	1	t	153
6718	Yangiqo`rg`on MFY	1	t	153
6719	Zafarobod MFY	1	t	153
6720	Achchisay MFY	1	t	154
6721	Alg`abas MFY	1	t	154
6722	Ashirbek MFY	1	t	154
6723	Aydarali MFY	1	t	154
6724	Besh-tut MFY	1	t	154
6725	Barraj MFY	1	t	154
6726	Birlik MFY	1	t	154
6727	Bog`iston MFY	1	t	154
6728	Boladala MFY	1	t	154
6729	Bo`ston MFY	1	t	154
6730	Bo`stonliq MFY	1	t	154
6731	Burchmullo MFY	1	t	154
6732	Chimboyliq MFY	1	t	154
6733	Chimboyliq MFY	1	t	154
6734	Chimgan MFY	1	t	154
6735	Chinor MFY	1	t	154
6736	Chorbog MFY	1	t	154
6737	Dadaboev MFY	1	t	154
6738	Daxana MFY	1	t	154
6739	Dumaloq MFY	1	t	154
6740	g`azalkent MFY	1	t	154
6741	Iskandar MFY	1	t	154
6742	Iskandar MFY	1	t	154
6743	Istiqlol MFY	1	t	154
6744	Jaxonobod MFY	1	t	154
6745	Kichiksoy MFY	1	t	154
6746	Ko`kto`nli MFY	1	t	154
6747	Ma`rifat MFY	1	t	154
6748	Markaziy MFY	1	t	154
6749	Navro`z MFY	1	t	154
6750	Novobod MFY	1	t	154
6751	Nurchilar MFY	1	t	154
6752	Ozodbosh MFY	1	t	154
6753	Pargos MFY	1	t	154
6754	Pargos MFY	1	t	154
6755	Pskom MFY	1	t	154
6756	Qoraboy MFY	1	t	154
6757	Qoramanas MFY	1	t	154
6758	Qoramozor MFY	1	t	154
6759	Qoronqul MFY	1	t	154
6760	Qo`shqo`rg`on MFY	1	t	154
6761	Qo`shqo`rg`on MFY	1	t	154
6762	Qurbonov MFY	1	t	154
6763	S. Raximov MFY	1	t	154
6764	S. Xondoyliqiy MFY	1	t	154
6765	Sarbo MFY	1	t	154
6766	Sari-Kanli MFY	1	t	154
6767	Sijjak MFY	1	t	154
6768	Soyliq MFY	1	t	154
6769	Talpin MFY	1	t	154
6770	Tovoqsoy MFY	1	t	154
6771	To`labi MFY	1	t	154
6772	Uyenkulsay MFY	1	t	154
6773	Uzun MFY	1	t	154
6774	Xondoyliq MFY	1	t	154
6775	Xo`jakent MFY	1	t	154
6776	Xo`jakent MFY	1	t	154
6777	Xumsan MFY	1	t	154
6778	Xumsan MFY	1	t	154
6779	Yakkatut MFY	1	t	154
6780	Yangiaul MFY	1	t	154
6781	Yangimahalla MFY	1	t	154
6782	A.g`aniev MFY	1	t	155
6783	A.Mirkomilov MFY	1	t	155
6784	A.Navoiy MFY	1	t	155
6785	A.Navoiy-Navro`z MFY	1	t	155
6786	A.Shorahmedov MFY	1	t	155
6787	A.Temur MFY	1	t	155
6788	Abdujalilbob MFY	1	t	155
6789	Achchi-soy MFY	1	t	155
6790	Ahillik MFY	1	t	155
6791	Ahmad Yassaviy MFY	1	t	155
6792	Alim buva MFY	1	t	155
6793	Aloqa MFY	1	t	155
6794	Avliyo ota MFY	1	t	155
6795	B.Nishonov MFY	1	t	155
6796	Bel-ariq MFY	1	t	155
6797	Baliqchi (jamoatchi) MFY	1	t	155
6798	Birlik (jamoatchi) MFY	1	t	155
6799	Bog`ishamol MFY	1	t	155
6800	Bog`zor MFY	1	t	155
6801	Bo`ston MFY	1	t	155
6802	Bo`z-suv QFY	1	t	155
6803	Chig`atoy MFY	1	t	155
6804	Chig`atoy-Oqt?pa QFY	1	t	155
6805	Chinor MFY	1	t	155
6806	Chosh tepa QFY	1	t	155
6807	Chuvalachi MFY	1	t	155
6808	Chuvalachi QFY MFY	1	t	155
6809	Dehqonobod MFY	1	t	155
6810	Daliguzar MFY	1	t	155
6811	Darxon MFY	1	t	155
6812	Diydor MFY	1	t	155
6813	Do`stlik MFY	1	t	155
6814	Erkin MFY	1	t	155
6815	Erkin QFY	1	t	155
6816	Eshonguzar MFY	1	t	155
6817	Eshonguzar QFY	1	t	155
6818	Eski qal`a MFY	1	t	155
6819	Farobiy MFY	1	t	155
6820	Fayz MFY	1	t	155
6821	g`isht-ko`prik MFY	1	t	155
6822	Gul tepa MFY	1	t	155
6823	Guliston QFY	1	t	155
6824	Gulobod MFY	1	t	155
6825	Gulzor MFY	1	t	155
6826	Halimko`p MFY	1	t	155
6827	Harakat MFY	1	t	155
6828	Hiyobon MFY	1	t	155
6829	Huvaydo MFY	1	t	155
6830	I.Bahromov MFY	1	t	155
6831	I.Yakubov MFY	1	t	155
6832	Ibrat MFY	1	t	155
6833	Ibrat MFY	1	t	155
6834	Iftihor MFY	1	t	155
6835	Ilg`or MFY	1	t	155
6836	Iqbol (jamoatchi) MFY	1	t	155
6837	Iqbol MFY	1	t	155
6838	Istiqlol MFY	1	t	155
6839	Istiqlolning 5 yilligi (jamoatchi) MFY	1	t	155
6840	Jaloir MFY	1	t	155
6841	Kensoy MFY	1	t	155
6842	Kalas MFY	1	t	155
6843	Katta-chinor MFY	1	t	155
6844	Katta-tepa MFY	1	t	155
6845	Ko`k - terak QFY MFY	1	t	155
6846	Ko`k-terak MFY	1	t	155
6847	Ko`ksaroy MFY	1	t	155
6848	Ko`ksaroy QFY	1	t	155
6849	Ko`xi-nur MFY	1	t	155
6850	M.Fozilov MFY	1	t	155
6851	M.Ma.murov MFY	1	t	155
6852	M.Musaev MFY	1	t	155
6853	M.Yo`ldosh?va MFY	1	t	155
6854	Mevazor MFY	1	t	155
6855	Madaniyat (jamoatchi) MFY	1	t	155
6856	Madaniyat-Oybek MFY	1	t	155
6857	Majnuntol MFY	1	t	155
6858	Masalboy QFY	1	t	155
6859	Mustaqillik MFY	1	t	155
6860	N`amin MFY	1	t	155
6861	N.Odilova MFY	1	t	155
6862	Namdanak MFY	1	t	155
6863	Nayman MFY	1	t	155
6864	Nazarbek MFY	1	t	155
6865	Nazarbek QFY	1	t	155
6866	Nurafshon MFY	1	t	155
6867	Nurafshon MFY	1	t	155
6868	Nurobod MFY	1	t	155
6869	Obod MFY	1	t	155
6870	Obodlik MFY	1	t	155
6871	Olmazor MFY	1	t	155
6872	Oltintepa MFY	1	t	155
6873	Oq-tom MFY	1	t	155
6874	Oq-tosh MFY	1	t	155
6875	Oqibat MFY	1	t	155
6876	Oydin xayot MFY	1	t	155
6877	O`ratepa (jamoatchi) MFY	1	t	155
6878	O`rikzor MFY	1	t	155
6879	O`rta MFY	1	t	155
6880	O`rtaovul MFY	1	t	155
6881	O`rtaovul QFY	1	t	155
6882	O`zgarish QFY	1	t	155
6883	Past-Darxon MFY	1	t	155
6884	Qahramon MFY	1	t	155
6885	Qashqarlik MFY	1	t	155
6886	Qatortol QFY	1	t	155
6887	Qir-ariq MFY	1	t	155
6888	Qir-guzar MFY	1	t	155
6889	Qizg`aldoq QFY	1	t	155
6890	Qorabo`rik MFY	1	t	155
6891	Qorako`sa MFY	1	t	155
6892	Qorasaroy MFY	1	t	155
6893	Qorasuv MFY	1	t	155
6894	Qoravoy to`pi (jamoatchi) MFY	1	t	155
6895	Qum-ariq MFY	1	t	155
6896	Qurilish MFY	1	t	155
6897	Quruvchi MFY	1	t	155
6898	Qush-qo`ndi MFY	1	t	155
6899	Quyoshli MFY	1	t	155
6900	R.Dadaxo`ja?v MFY	1	t	155
6901	Rahbar obod MFY	1	t	155
6902	Ramadon MFY	1	t	155
6903	S.Rahimov MFY	1	t	155
6904	Sabzavot MFY	1	t	155
6905	Sag`bon MFY	1	t	155
6906	Sahovat MFY	1	t	155
6907	Sanoat MFY	1	t	155
6908	Sarka MFY	1	t	155
6909	Shamsiobod MFY	1	t	155
6910	Shirin MFY	1	t	155
6911	Shodlik MFY	1	t	155
6912	Sirg`ali MFY	1	t	155
6913	Sohibkor MFY	1	t	155
6914	Sohibkor MFY	1	t	155
6915	Sort?pa MFY	1	t	155
6916	Tariq-t?shar MFY	1	t	155
6917	Tarnov MFY	1	t	155
6918	Tinchlik MFY	1	t	155
6919	Tokzor MFY	1	t	155
6920	Toshkent MFY	1	t	155
6921	To`qayzor (jamoatchi) MFY	1	t	155
6922	To`qimachi MFY	1	t	155
6923	Turkiston MFY	1	t	155
6924	Turkiston QFY	1	t	155
6925	Turopobod MFY	1	t	155
6926	Tutzor MFY	1	t	155
6927	Uch sada MFY	1	t	155
6928	Ulug`bek (jamoatchi) MFY	1	t	155
6929	X`abdulla?v MFY	1	t	155
6930	X.Umarov MFY	1	t	155
6931	Xasanboy guzar MFY	1	t	155
6932	Xasanboy MFY	1	t	155
6933	Xasanboy QFY	1	t	155
6934	Xonobod MFY	1	t	155
6935	Xonobod QFY	1	t	155
6936	Xo`ja mozor MFY	1	t	155
6937	Y.Karimov MFY	1	t	155
6938	Y.Oxunbobo?v MFY	1	t	155
6939	Yangi hayot MFY	1	t	155
6940	Yunus obod QFY	1	t	155
6941	Z.Jalilov MFY	1	t	155
6942	Z.Po`latov MFY	1	t	155
6943	Z.Zokirova MFY	1	t	155
6944	Zangiota QFY	1	t	155
6945	Zarafshon (jamoatchi) MFY	1	t	155
6946	Zarbdor MFY	1	t	155
6947	Zargar MFY	1	t	155
6948	Zax - ariq MFY	1	t	155
6949	Ziyo (jamoatchi) MFY	1	t	155
6950	Tuzel QFY	1	t	156
6951	Uymovut MFY	1	t	156
6952	A.Navoiy MFY	1	t	156
6953	Akademiklar (jamoatchi) MFY	1	t	156
6954	Alisherobod MFY	1	t	156
6955	Amir Temur MFY	1	t	156
6956	Arg`in MFY	1	t	156
6957	Arg`in MFY	1	t	156
6958	Beruniy MFY	1	t	156
6959	Bahor MFY	1	t	156
6960	Baytqo`rg`on MFY	1	t	156
6961	Baytqo`rg`on QFY	1	t	156
6962	Birlik (jamoatchi) MFY	1	t	156
6963	Birlik MFY	1	t	156
6964	Bobur MFY	1	t	156
6965	Botanika MFY	1	t	156
6966	Boyjigit MFY	1	t	156
6967	Bo`ston MFY	1	t	156
6968	Chingeldi MFY	1	t	156
6969	Chinobod MFY	1	t	156
6970	Chinobod QFY	1	t	156
6971	Darxon MFY	1	t	156
6972	Do`rmon MFY	1	t	156
6973	Do`stlik MFY	1	t	156
6974	Do`stlik MFY	1	t	156
6975	Do`stlik MFY	1	t	156
6976	g`afur g`ulom MFY	1	t	156
6977	G?ofizika MFY	1	t	156
6978	Guliston . 1 MFY	1	t	156
6979	Guliston MFY	1	t	156
6980	Guliston MFY	1	t	156
6981	Gulzor . 1 MFY	1	t	156
6982	Gulzor . 2 MFY	1	t	156
6983	Islomobod MFY	1	t	156
6984	Istiqlol MFY	1	t	156
6985	Jarboshi (jamoatchi) MFY	1	t	156
6986	Kodiriya GES (jamoatchi) MFY	1	t	156
6987	Ko`prik boshi MFY	1	t	156
6988	M.Ulug`bek MFY	1	t	156
6989	Mevazor MFY	1	t	156
6990	Mexnat MFY	1	t	156
6991	Madaniyat MFY	1	t	156
6992	Matkabulov QFY	1	t	156
6993	May MFY	1	t	156
6994	May QFY	1	t	156
6995	Mirzo Ulug`bek MFY	1	t	156
6996	Mustaqillik MFY	1	t	156
6997	Muxtor MFY	1	t	156
6998	Navbahor MFY	1	t	156
6999	Navro`z MFY	1	t	156
7000	Normuxamedov MFY	1	t	156
7001	Nurafshon MFY	1	t	156
7002	Nurobod MFY	1	t	156
7003	Obod MFY	1	t	156
7004	Oq oltin MFY	1	t	156
7005	Oq-qovoq QFY	1	t	156
7006	Otamuxamedov MFY	1	t	156
7007	Oybek MFY	1	t	156
7008	O`nqo`rg`on . 1 MFY	1	t	156
7009	O`nqo`rg`on MFY	1	t	156
7010	O`nqo`rg`on QFY	1	t	156
7011	O`tkir MFY	1	t	156
7012	Pastki yuz MFY	1	t	156
7013	Po`lat qadam MFY	1	t	156
7014	Qibray SHFY	1	t	156
7015	Qichoq QFY	1	t	156
7016	Qipchoq MFY	1	t	156
7017	Qizil Shalola MFY	1	t	156
7018	Qurilish MFY	1	t	156
7019	S.Raximov MFY	1	t	156
7020	Selekeiya MFY	1	t	156
7021	Salor GES MFY	1	t	156
7022	Salor SHFY	1	t	156
7023	Sh.Rashidov MFY	1	t	156
7024	Sheraliev MFY	1	t	156
7025	Sharq MFY	1	t	156
7026	Shodlik MFY	1	t	156
7027	Shodlik MFY	1	t	156
7028	Sohibkor MFY	1	t	156
7029	Taraqqiy MFY	1	t	156
7030	Toshisti MFY	1	t	156
7031	Tovkentepa MFY	1	t	156
7032	To`qaytepa MFY	1	t	156
7033	Tuzel MFY	1	t	156
7034	Uzumzor MFY	1	t	156
7035	X`amirov MFY	1	t	156
7036	Xosildor MFY	1	t	156
7037	Yalang`och ota MFY	1	t	156
7038	Yangiobod MFY	1	t	156
7039	Yangiobod QFY MFY	1	t	156
7040	Yangixayot MFY	1	t	156
7041	Yangixayot MFY	1	t	156
7042	Yangiyo`l MFY	1	t	156
7043	Yonariq MFY	1	t	156
7044	Yonariq QFY	1	t	156
7045	Yoshlik MFY	1	t	156
7046	Yuqori yuz MFY	1	t	156
7047	Zebuniso MFY	1	t	156
7048	1-sonli Ishchilar MFY	1	t	157
7049	2-sonli Yangi xayot MFY	1	t	157
7050	3-sonli Oxunbobo?v MFY	1	t	157
7051	5-sonli F.Xujaev nomli MFY	1	t	157
7052	Abay MFY(jamoat)	1	t	157
7053	An-Don-Su MFY	1	t	157
7054	Beruniy MFY	1	t	157
7055	Balikchi MFY	1	t	157
7056	Birlik MFY	1	t	157
7057	Chakmok MFY	1	t	157
7058	Do`stlik MFY	1	t	157
7059	Do`stlik-1 MFY	1	t	157
7060	Galabotir MFY(jamoat)	1	t	157
7061	Gul MFY	1	t	157
7062	Gul QFY	1	t	157
7063	I.Yunusov MFY(jamoat)	1	t	157
7064	Istiqlol QFY	1	t	157
7065	Ittifoq MFY(jamoat)	1	t	157
7066	Jumag`ul MFY(jamoat)	1	t	157
7067	Ketmontepa QFY	1	t	157
7068	Kushek MFY(jamoat)	1	t	157
7069	Mevazor MFY(jamoat)	1	t	157
7070	Mashrab nomli 4-son MFY	1	t	157
7071	Maydontol QFY	1	t	157
7072	Ming Chinor MFY	1	t	157
7073	Nurboy ota MFY	1	t	157
7074	Otajonov MFY	1	t	157
7075	O`jakent MFY(jamoat)	1	t	157
7076	O`zbekiston QFY	1	t	157
7077	Paxtachi MFY	1	t	157
7078	Paxtazor MFY	1	t	157
7079	Qo`rg`oncha QFY	1	t	157
7080	Seregli MFY(jamoat)	1	t	157
7081	Surum MFY	1	t	157
7082	Tinchlik MFY(jamoat)	1	t	157
7083	Toshloq QFY	1	t	157
7084	Toshovul QFY	1	t	157
7085	Tukboy MFY	1	t	157
7086	Vatan MFY(jamoat) MFY	1	t	157
7087	Xamza MFY	1	t	157
7088	Xuja MFY	1	t	157
7089	Xujapiskan MFY	1	t	157
7090	Yangi xayot MFY	1	t	157
7091	Yangix ayot QFY	1	t	157
7092	Yilkichi MFY	1	t	157
7093	Yulduz MFY	1	t	157
7094	Achchi QFY	1	t	158
7095	Birlik MFY	1	t	158
7096	Boyg`uli MFY	1	t	158
7097	Buka (jamoatchi) MFY	1	t	158
7098	Dexkonobod (jamoatchi) MFY	1	t	158
7099	Do`stlik QFY	1	t	158
7100	Eltamgali (jamoatchi) MFY	1	t	158
7101	Eltamgali QFY	1	t	158
7102	Erkinlik QFY	1	t	158
7103	Jag`alboyli MFY	1	t	158
7104	Kalyas MFY	1	t	158
7105	Kanka (jamoatchi) MFY	1	t	158
7106	Kaxramon MFY	1	t	158
7107	Kiziltut MFY	1	t	158
7108	Kurik (jamoatchi) MFY	1	t	158
7109	Kushtepa MFY	1	t	158
7110	Kushtamgali MFY	1	t	158
7111	Madaniyat MFY	1	t	158
7112	Mamut (jamoatchi) MFY	1	t	158
7113	Mustakillik MFY	1	t	158
7114	Navbaxor MFY	1	t	158
7115	Navoiy MFY(jamoatchi)	1	t	158
7116	Navruz MFY	1	t	158
7117	Olimkent QFY	1	t	158
7118	Oqqo`rg`on QFY	1	t	158
7119	Oxunboboev MFY	1	t	158
7120	Oytamg`ali QFY	1	t	158
7121	Qo`rg`oncha MFY	1	t	158
7122	Qo`rg`ontepa MFY	1	t	158
7123	S.Raximov MFY	1	t	158
7124	S.Raximov MFY(jamoatchi)	1	t	158
7125	S.Sezgizboev MFY	1	t	158
7126	Saidaobod MFY(jamoatchi)	1	t	158
7127	Samarkand MFY(jamoatchi)	1	t	158
7128	Shoxruxiya QFY	1	t	158
7129	Suvti MFY	1	t	158
7130	Tolovul MFY	1	t	158
7131	Tortuvli MFY	1	t	158
7132	Toshto`g`on QFY	1	t	158
7133	Usta Normat MFY	1	t	158
7134	Xalkaobod MFY	1	t	158
7135	Xamzaobod MFY	1	t	158
7136	Xonobod MFY	1	t	158
7137	Xosildor MFY	1	t	158
7138	Yangi tulkin (jamoatchi) MFY	1	t	158
7139	Yoshlik MFY	1	t	158
7140	Zafar QFY	1	t	158
7141	Zarafshon MFY	1	t	158
7142	Zarbdor QFY	1	t	158
7143	A`avloniy MFY	1	t	159
7144	A.Ikromov MFY	1	t	159
7145	A.Kaxxor MFY	1	t	159
7146	A.Kodiriy MFY	1	t	159
7147	A.Navoiy MFY	1	t	159
7148	A.Yassaviy MFY	1	t	159
7149	Bobur MFY	1	t	159
7150	Buston MFY	1	t	159
7151	Chambil MFY	1	t	159
7152	Chulpon MFY	1	t	159
7153	Do`stlik MFY	1	t	159
7154	Furkat MFY	1	t	159
7155	g`Gulom MFY	1	t	159
7156	GRE MFY	1	t	159
7157	Gultepa MFY	1	t	159
7158	Ibn-Sino MFY	1	t	159
7159	Kalmakir MFY	1	t	159
7160	Kamalak MFY	1	t	159
7161	Kimyogar MFY	1	t	159
7162	Koinot MFY	1	t	159
7163	Kurpasoy MFY	1	t	159
7164	M.Ulugbek MFY	1	t	159
7165	Mukumiy MFY	1	t	159
7166	Mustakillik MFY	1	t	159
7167	Namuna MFY	1	t	159
7168	Navruz MFY	1	t	159
7169	Olmalik ovul MFY	1	t	159
7170	Olmalik soy MFY	1	t	159
7171	Oltin MFY	1	t	159
7172	Oxunboboev MFY	1	t	159
7173	Oydin MFY	1	t	159
7174	Ramazon MFY	1	t	159
7175	Sufi Ollayor MFY	1	t	159
7176	Terekli MFY	1	t	159
7177	Tinchlik MFY	1	t	159
7178	Toshkent MFY	1	t	159
7179	U.Nosir MFY	1	t	159
7180	U.Yusupov MFY	1	t	159
7181	Uvaysiy MFY	1	t	159
7182	Uzbekiston MFY	1	t	159
7183	X.Olimjon MFY	1	t	159
7184	Xamza MFY	1	t	159
7185	Yulduz MFY	1	t	159
7186	Adolat MFY	1	t	160
7187	Alisher MFY(jamoat asosida)	1	t	160
7188	Azim ota MFY(jamoat asosida)	1	t	160
7189	Baxt MFY	1	t	160
7190	Birlik MFY	1	t	160
7191	Birlik MFY(jamoat asosida)	1	t	160
7192	Birlik QFY	1	t	160
7193	Bo`ston MFY	1	t	160
7194	Bo`ston MFY(jamoat asosida)	1	t	160
7195	Buloq MFY(jamoat asosida)	1	t	160
7196	Chetsuv MFY(jamoat asosida)	1	t	160
7197	Chinor MFY(jamoat asosida)	1	t	160
7198	Chuvildoq MFY(jamoat asosida)	1	t	160
7199	Do`stlik MFY	1	t	160
7200	Do`stlik QFY	1	t	160
7201	Do`tlik MFY(jamoat asosida)	1	t	160
7202	Eyval?k MFY(jamoat asosida)	1	t	160
7203	g`alla-Quduq MFY	1	t	160
7204	Go`shsoy MFY	1	t	160
7205	Guliston MFY	1	t	160
7206	Gulobod MFY(jamoat asosida)	1	t	160
7207	Ilg`or MFY(jamoat asosida)	1	t	160
7208	Iloq MFY	1	t	160
7209	Ko`ksaroy MFY	1	t	160
7210	Markaziy qo`rg`on MFY(jamoat asosida)	1	t	160
7211	Mo`minobod MFY(jamoat asosida)	1	t	160
7212	Mustaqillik MFY	1	t	160
7213	Namuna MFY	1	t	160
7214	Navbahor MFY	1	t	160
7215	Nog`oyqo`rg`on MFY(jamoat asosida)	1	t	160
7216	Obiz MFY(jamoat asosida)	1	t	160
7217	Olmazor MFY(jamoat asosida)	1	t	160
7218	Orzu MFY	1	t	160
7219	Oxunboboev MFY	1	t	160
7220	Oybuloq MFY(jamoat asosida)	1	t	160
7221	Ozodlik MFY(jamoat asosida)	1	t	160
7222	Ozodlik QFY	1	t	160
7223	O`bayd MFY(jamoat asosida)	1	t	160
7224	O`zar MFY(jamoat asosida)	1	t	160
7225	O`zbekiston MFY(jamoat asosida)	1	t	160
7226	Qayirma MFY(jamoat asosida)	1	t	160
7227	Qiziloy MFY	1	t	160
7228	Qorabaliq MFY(jamoat asosida)	1	t	160
7229	Qorasuvyoqa MFY(jamoat asosida)	1	t	160
7230	Qoraxitoy QFY	1	t	160
7231	Qo`rg`on MFY	1	t	160
7232	Qurama QFY	1	t	160
7233	Quyun MFY(jamoat asosida)	1	t	160
7234	Serkaqirildi MFY(jamoat asosida)	1	t	160
7235	Sanam MFY	1	t	160
7236	Sarijayloq MFY(jamoat asosida)	1	t	160
7237	Sartamg`ali MFY(jamoat asosida)	1	t	160
7238	Shodlik MFY	1	t	160
7239	Shodmalik MFY(jamoat asosida)	1	t	160
7240	Shoshtepa MFY(jamoat asosida)	1	t	160
7241	Shovg`oz MFY(jamoat asosida)	1	t	160
7242	Susam MFY(jamoat asosida)	1	t	160
7243	Susam QFY	1	t	160
7244	Talov MFY(jamoat asosida)	1	t	160
7245	Talov QFY	1	t	160
7246	Tangatopdi MFY(jamoat asosida)	1	t	160
7247	Toshariq MFY(jamoat asosida)	1	t	160
7248	Toshsoy MFY(jamoat asosida)	1	t	160
7249	Tut MFY	1	t	160
7250	Umid MFY	1	t	160
7251	Ungut MFY(jamoat asosida)	1	t	160
7252	Uvak MFY(jamoat asosida)	1	t	160
7253	Uvak QFY	1	t	160
7254	Vatan MFY	1	t	160
7255	Xonobod MFY	1	t	160
7256	Yalpoqtepa MFY(jamoat asosida)	1	t	160
7257	Yangi-Hayot MFY	1	t	160
7258	Yangibo`ston MFY(jamoat asosida)	1	t	160
7259	Yangilik MFY	1	t	160
7260	Yangiobod MFY	1	t	160
7261	Yangiobod MFY(jamoat asosida)	1	t	160
7262	Yangiqishlog`iloq MFY(jamoat asosida)	1	t	160
7263	Yonariq MFY	1	t	160
7264	Yoshlik MFY	1	t	160
7265	Beshkappa MFY	1	t	161
7266	Bodomtepa MFY	1	t	161
7267	Bog`bon MFY	1	t	161
7268	Boshqizilsoy QFY	1	t	161
7269	Boyqozon MFY	1	t	161
7270	Bo`ston MFY	1	t	161
7271	Bo`ston QFY	1	t	161
7272	Bulokboshi MFY	1	t	161
7273	Bursilik MFY	1	t	161
7274	Changi QFY	1	t	161
7275	Chinor MFY	1	t	161
7276	Chinorli MFY	1	t	161
7277	Chukkayma MFY	1	t	161
7278	Gulbog MFY	1	t	161
7279	Gulbog` MFY	1	t	161
7280	Guliston MFY	1	t	161
7281	Istikbol MFY	1	t	161
7282	Kulichi MFY	1	t	161
7283	Kumushkon MFY	1	t	161
7284	Kungay MFY	1	t	161
7285	Kuruksoy MFY	1	t	161
7286	Kushshukur MFY	1	t	161
7287	Kuyosh MFY	1	t	161
7288	Markaziy MFY	1	t	161
7289	Mozorxoji MFY	1	t	161
7290	Nevich MFY	1	t	161
7291	Navruz MFY	1	t	161
7292	Nomdanak QFY	1	t	161
7293	Novdak MFY	1	t	161
7294	Objuvoz MFY	1	t	161
7295	Oktepa MFY	1	t	161
7296	Olmazor MFY	1	t	161
7297	Oybek MFY	1	t	161
7298	O`rta MFY	1	t	161
7299	Parkent QFY	1	t	161
7300	Qirg`izovul MFY	1	t	161
7301	Qoraqalpoq QFY	1	t	161
7302	Qo`rg`on MFY	1	t	161
7303	Qo`rg`ontepa MFY	1	t	161
7304	Samarobod MFY	1	t	161
7305	Samsarak-Navbaxor MFY	1	t	161
7306	Shampan-Sanganak MFY	1	t	161
7307	Shaxak MFY	1	t	161
7308	Soy MFY	1	t	161
7309	Soy MFY	1	t	161
7310	So`qoq QFY	1	t	161
7311	Surxi MFY	1	t	161
7312	Teman MFY	1	t	161
7313	Teman MFY	1	t	161
7314	Tojiboy Rizaev MFY	1	t	161
7315	Uchok MFY	1	t	161
7316	Ulug`bek MFY	1	t	161
7317	Xisarak QFY	1	t	161
7318	Xuja MFY	1	t	161
7319	Yangi MFY	1	t	161
7320	Yangiobod MFY	1	t	161
7321	Yukori MFY	1	t	161
7322	Yuqori MFY	1	t	161
7323	Yuqori MFY	1	t	161
7324	Zarkent QFY	1	t	161
7325	Bekobod MFY	1	t	162
7326	Birlik MFY	1	t	162
7327	Chimkurgon MFY	1	t	162
7328	Cho`loqqo`rg`on MFY	1	t	162
7329	Do`ngqo`rg`on QFY	1	t	162
7330	Do`stlik MFY	1	t	162
7331	g`ayrat MFY	1	t	162
7332	Guliston MFY	1	t	162
7333	Kelovchi QFY	1	t	162
7334	Koriz QFY	1	t	162
7335	Kulota MFY	1	t	162
7336	Kultepa MFY	1	t	162
7337	Lolaarik MFY	1	t	162
7338	Maylobod MFY	1	t	162
7339	Mingtepa MFY	1	t	162
7340	Mitan MFY	1	t	162
7341	Mo`minobod MFY	1	t	162
7342	Murotali QFY	1	t	162
7343	Mustakillik MFY	1	t	162
7344	Namuna MFY	1	t	162
7345	Navoiy MFY	1	t	162
7346	Novkent MFY	1	t	162
7347	Oktom MFY	1	t	162
7348	Oqt?pa QFY	1	t	162
7349	Oxunbobo?v MFY	1	t	162
7350	Oybek MFY	1	t	162
7351	Paxtapunkt MFY	1	t	162
7352	Said QFY	1	t	162
7353	Saidobod MFY	1	t	162
7354	Suvti MFY	1	t	162
7355	Xolikberdi MFY	1	t	162
7356	Yangiobod MFY	1	t	162
7357	Zominovul MFY	1	t	162
7358	 	1	t	163
7359	A Yulbarisov MFY	1	t	163
7360	Angor k.FY	1	t	163
7361	Aranshi MFY	1	t	163
7362	Argin-Kirgizovul MFY	1	t	163
7363	Bektemir MFY	1	t	163
7364	Beshboy MFY	1	t	163
7365	Bagish MFY	1	t	163
7366	Birlik MFY	1	t	163
7367	Birlik MFY	1	t	163
7368	Bobir MFY	1	t	163
7369	Boykurgon MFY	1	t	163
7370	Boyovul MFY	1	t	163
7371	Burgalik MFY	1	t	163
7372	Chivintepa MFY	1	t	163
7373	Chukurovul MFY	1	t	163
7374	Dexkonobod MFY	1	t	163
7375	Darxan MFY	1	t	163
7376	Do`stlik k.FY	1	t	163
7377	Do`stlik MFY	1	t	163
7378	Do`stlik MFY	1	t	163
7379	Evalak MFY	1	t	163
7380	Galabotir 1 MFY	1	t	163
7381	Guliston MFY	1	t	163
7382	Guzar MFY	1	t	163
7383	Istiqlol k.FY	1	t	163
7384	Jaloir MFY	1	t	163
7385	Jangaboy MFY	1	t	163
7386	Kaytmas MFY	1	t	163
7387	Konchi MFY	1	t	163
7388	Korakalpok MFY	1	t	163
7389	Korasuv k.FY	1	t	163
7390	Korasuv MFY	1	t	163
7391	Kuchluk MFY	1	t	163
7392	Kukm-uyin MFY	1	t	163
7393	Kukonovul MFY	1	t	163
7394	Kukonovul MFY	1	t	163
7395	Kulkora MFY	1	t	163
7396	Kumarik MFY	1	t	163
7397	Kumovul QFY	1	t	163
7398	Kundizak MFY	1	t	163
7399	Kuramaovul MFY	1	t	163
7400	Kutib yulduzi MFY	1	t	163
7401	Mash`al MFY	1	t	163
7402	Mayramkul MFY	1	t	163
7403	Mikrarayon MFY	1	t	163
7404	Mingtepa MFY	1	t	163
7405	Mukimiy MFY	1	t	163
7406	Mustakillik MFY	1	t	163
7407	Mustakillik MFY	1	t	163
7408	Mutal ota MFY	1	t	163
7409	Namuna MFY	1	t	163
7410	Navoiy k.FY	1	t	163
7411	Navoiy MFY	1	t	163
7412	Navoiy MFY	1	t	163
7413	Navruz MFY	1	t	163
7414	Navruz MFY	1	t	163
7415	Nomdanak MFY	1	t	163
7416	o` Sharafutdinov MFY	1	t	163
7417	Ok ota k.FY	1	t	163
7418	Olti ugil MFY	1	t	163
7419	Oppok MFY	1	t	163
7420	Oybek MFY	1	t	163
7421	Paxtakor k.FY MFY	1	t	163
7422	Paxtakor MFY	1	t	163
7423	Paxtaobod k.FY	1	t	163
7424	Rovatak MFY	1	t	163
7425	Saidovul MFY	1	t	163
7426	Sholikor MFY	1	t	163
7427	TarakQiyot MFY	1	t	163
7428	Tinchlik MFY	1	t	163
7429	Toshlok MFY	1	t	163
7430	Turkiston MFY	1	t	163
7431	Tuyabugiz QFY	1	t	163
7432	Uchkun MFY	1	t	163
7433	Uchokli MFY	1	t	163
7434	Urtabuz MFY	1	t	163
7435	Urtaovul MFY	1	t	163
7436	Urtasaroy k.FY	1	t	163
7437	Urtasaroy MFY	1	t	163
7438	Usmon ota MFY	1	t	163
7439	Uygur MFY	1	t	163
7440	X Olimjon MFY	1	t	163
7441	Yangi turmush MFY	1	t	163
7442	Yangi turmush MFY	1	t	163
7443	Yangi xayot MFY	1	t	163
7444	Yangilik MFY	1	t	163
7445	Yangiobod MFY	1	t	163
7446	Yangiobod MFY	1	t	163
7447	Yangixayot QFY	1	t	163
7448	Yangixayot MFY	1	t	163
7449	Yangiyul MFY	1	t	163
7450	Yorik MFY	1	t	163
7451	Yukoriovul MFY	1	t	163
7452	Yungichkoli k.FY	1	t	163
7453	Yungichkoli MFY	1	t	163
7454	Uymovut MFY(jamoatchi)	1	t	164
7455	A.Navoiy MFY	1	t	164
7456	A.Temur MFY(jamoatchi)	1	t	164
7457	Abil ota MFY(jamoatchi)	1	t	164
7458	Abzalobod MFY(jamoatchi)	1	t	164
7459	Achamayli MFY(jamoatchi)	1	t	164
7460	Archazor MFY(jamoatchi)	1	t	164
7461	Avgon MFY	1	t	164
7462	Axillik MFY(jamoatchi)	1	t	164
7463	Besh-kapa MFY	1	t	164
7464	Besh-kapa MFY	1	t	164
7465	Birlik MFY(jamoatchi)	1	t	164
7466	Bog`bon MFY(jamoatchi)	1	t	164
7467	Chinmasjid MFY(jamoatchi)	1	t	164
7468	Chinoz QFY	1	t	164
7469	Dexkonobod MFY(jamoatchi)	1	t	164
7470	Do`stlik MFY(jamoatchi)	1	t	164
7471	Do`stlik MFY	1	t	164
7472	Do`stlik MFY	1	t	164
7473	Do`stlik MFY(jamoatchi)	1	t	164
7474	Do`stlik MFY(jamoatchi)	1	t	164
7475	Erkin MFY(jamoatchi)	1	t	164
7476	Eshonobod QFY	1	t	164
7477	Eski Toshkent QFY	1	t	164
7478	Furkat MFY(jamoatchi)	1	t	164
7479	Gayrat MFY(jamoatchi)	1	t	164
7480	Guliston MFY(jamoatchi)	1	t	164
7481	Gulzaraobod MFY	1	t	164
7482	I.Sharipov MFY	1	t	164
7483	Ishchilar sh MFY(jamoatchi)	1	t	164
7484	Ishchilar shaxarchasi MFY	1	t	164
7485	Islomobod MFY	1	t	164
7486	Isloxat QFY	1	t	164
7487	Ittifok MFY(jamoatchi)	1	t	164
7488	Kerdara MFY(jamoatchi)	1	t	164
7489	Kanalobod MFY(jamoatchi)	1	t	164
7490	Kattatepalik MFY(jamoatchi)	1	t	164
7491	Kaxramon MFY(jamoatchi)	1	t	164
7492	Kaxramon MFY(jamoatchi)	1	t	164
7493	Kayragoch MFY(jamoatchi)	1	t	164
7494	Kora k-uyli MFY(jamoatchi)	1	t	164
7495	Kozi MFY	1	t	164
7496	Ko`tarma QFY	1	t	164
7497	Kurik MFY(jamoatchi)	1	t	164
7498	Kutarma MFY	1	t	164
7499	M.Pulatov MFY(jamoatchi)	1	t	164
7500	Mevazor MFY(jamoatchi)	1	t	164
7501	Madaniyat MFY	1	t	164
7502	Markaz MFY	1	t	164
7503	Markaz MFY(jamoatchi)	1	t	164
7504	Mukimiy MFY(jamoatchi)	1	t	164
7505	Navoiy MFY	1	t	164
7506	Navoiy MFY(jamoatchi)	1	t	164
7507	Navruz MFY(jamoatchi)	1	t	164
7508	Naxipov MFY(jamoatchi)	1	t	164
7509	Norkuziev MFY(jamoatchi)	1	t	164
7510	Obi xayot MFY(jamoatchi)	1	t	164
7511	Oq oltin MFY	1	t	164
7512	Olmazor SHFY	1	t	164
7513	Olmos MFY(jamoatchi)	1	t	164
7514	Oxunboboev MFY	1	t	164
7515	Oxunboboev MFY(jamoatchi)	1	t	164
7516	Oydin MFY(jamoatchi)	1	t	164
7517	O`zbekiston QFY	1	t	164
7518	Paxtaobod MFY	1	t	164
7519	Qir MFY(jamoatchi)	1	t	164
7520	Ramadon MFY(jamoatchi)	1	t	164
7521	Rasulobod MFY	1	t	164
7522	S`ayniy MFY(jamoatchi)	1	t	164
7523	S`ayniy MFY(jamoatchi)	1	t	164
7524	S.Raximov MFY	1	t	164
7525	S.Segizboev MFY(jamoatchi)	1	t	164
7526	Safar ota MFY(jamoatchi)	1	t	164
7527	Samarkand MFY(jamoatchi)	1	t	164
7528	Shevchenko MFY(jamoatchi)	1	t	164
7529	Sutbulok MFY	1	t	164
7530	Sutchilar MFY(jamoatchi)	1	t	164
7531	Tilla topgan MFY(jamoatchi)	1	t	164
7532	Tillaobod MFY(jamoatchi)	1	t	164
7533	Tinchlik MFY(jamoatchi)	1	t	164
7534	Turkiston QFY	1	t	164
7535	U.Nosir MFY(jamoatchi)	1	t	164
7536	U.Nosir MFY(jamoatchi)	1	t	164
7537	U.Yusupov MFY(jamoatchi)	1	t	164
7538	Uchkun MFY(jamoatchi)	1	t	164
7539	Uzbekiston MFY(jamoatchi)	1	t	164
7540	Uzumzor MFY(jamoatchi)	1	t	164
7541	X.Olimjon MFY(jamoatchi)	1	t	164
7542	Xamza MFY	1	t	164
7543	Xamza MFY(jamoatchi)	1	t	164
7544	Xamza MFY(jamoatchi)	1	t	164
7545	Xolikov MFY(jamoatchi)	1	t	164
7546	Xudoyberganov MFY(jamoatchi)	1	t	164
7547	Xuja MFY	1	t	164
7548	Yangi Chinoz SHFY	1	t	164
7549	Yangi Mahalla MFY	1	t	164
7550	Yangi obod MFY(jamoatchi)	1	t	164
7551	Yangi obod MFY(jamoatchi)	1	t	164
7552	Yangi xayot MFY(jamoatchi)	1	t	164
7553	Yangiobod MFY	1	t	164
7554	Yollama QFY	1	t	164
7555	Yollama MFY(jamoatchi)	1	t	164
7556	Yoshlik MFY	1	t	164
7557	Yoshlik MFY(jamoatchi)	1	t	164
7558	Yovvosh MFY(jamoatchi)	1	t	164
7559	Yu.Karimov MFY(jamoatchi)	1	t	164
7560	Yul tushgan MFY(jamoatchi)	1	t	164
7561	.Lola. MFY	1	t	165
7562	A.Temur MFY	1	t	165
7563	A.Yassaviy MFY	1	t	165
7564	Adolat MFY	1	t	165
7565	Baxor MFY	1	t	165
7566	Baxt MFY	1	t	165
7567	Birlik MFY	1	t	165
7568	Bobur MFY	1	t	165
7569	Chinor MFY	1	t	165
7570	Do`stlik MFY	1	t	165
7571	G`alaba MFY	1	t	165
7572	Guliston MFY	1	t	165
7573	Gulzor MFY	1	t	165
7574	Iftixor MFY	1	t	165
7575	Ikbol MFY	1	t	165
7576	Ishonch MFY	1	t	165
7577	Istiqlol MFY	1	t	165
7578	Kabutar MFY	1	t	165
7579	Kamalak MFY	1	t	165
7580	Kamolot MFY	1	t	165
7581	Kimyogar MFY	1	t	165
7582	Kuyosh MFY	1	t	165
7583	Ma`rifat MFY	1	t	165
7584	Madaniyat MFY	1	t	165
7585	Mir Alisher MFY	1	t	165
7586	Mirgolib MFY	1	t	165
7587	Muruvvat MFY	1	t	165
7588	Navbaxor MFY	1	t	165
7589	Navro`z MFY	1	t	165
7590	Nur MFY	1	t	165
7591	Semurg MFY	1	t	165
7592	Sharq MFY	1	t	165
7593	Shodlik MFY	1	t	165
7594	Tinchlik MFY	1	t	165
7595	Turon MFY	1	t	165
7596	Ulugbek MFY	1	t	165
7597	Umid MFY	1	t	165
7598	V.Xaydarov MFY	1	t	165
7599	X.Maksudov MFY	1	t	165
7600	Xamza MFY	1	t	165
7601	Xayot guli MFY	1	t	165
7602	Xumo MFY	1	t	165
7603	Yoshlik MFY	1	t	165
7604	Yulduz MFY	1	t	165
7605	A.Yassaviy MFY	1	t	166
7606	Arganchi QFY	1	t	166
7607	Baliqchi MFY	1	t	166
7608	Baxor MFY	1	t	166
7609	Birlik MFY	1	t	166
7610	Bolta MFY	1	t	166
7611	Bordonkul MFY	1	t	166
7612	Bordonkul QFY	1	t	166
7613	Chirchiq MFY	1	t	166
7614	Chumchuqjar MFY	1	t	166
7615	Darxan MFY	1	t	166
7616	Daulboy MFY	1	t	166
7617	Do`stlik MFY	1	t	166
7618	Do`stlik MFY	1	t	166
7619	Do`stlik MFY	1	t	166
7620	Gulbog` MFY	1	t	166
7621	Guliston MFY	1	t	166
7622	Istiqlol QFY	1	t	166
7623	Ittifoq MFY	1	t	166
7624	Iyk ota MFY	1	t	166
7625	Jalol tepa MFY	1	t	166
7626	Jambul QFY	1	t	166
7627	Judruq MFY	1	t	166
7628	Jumabozor MFY	1	t	166
7629	Junsiz MFY	1	t	166
7630	Kangli MFY	1	t	166
7631	Markaziy MFY	1	t	166
7632	Markaziy MFY	1	t	166
7633	Mirobod MFY	1	t	166
7634	Miyam- Kangli MFY	1	t	166
7635	Navoiy MFY	1	t	166
7636	Navoiy MFY	1	t	166
7637	Navro`z MFY	1	t	166
7638	Navro`z MFY	1	t	166
7639	Navro`z MFY	1	t	166
7640	Navro`z QFY	1	t	166
7641	Obodon MFY	1	t	166
7642	Oq- ovul QFY	1	t	166
7643	Oq-ovul MFY	1	t	166
7644	O`zbekiston MFY	1	t	166
7645	Qaytmas MFY	1	t	166
7646	Qizil soy MFY	1	t	166
7647	Qora su MFY	1	t	166
7648	Qoratuxum MFY	1	t	166
7649	Qoratuxum MFY	1	t	166
7650	Qursoy MFY	1	t	166
7651	Saksonota MFY	1	t	166
7652	Saksonota QFY	1	t	166
7653	Surank?ent QFY	1	t	166
7654	Tinchlik QFY	1	t	166
7655	Toshtug`izaq MFY	1	t	166
7656	To`qimboy MFY	1	t	166
7657	Usmonobod MFY	1	t	166
7658	Xitoy-tepa MFY	1	t	166
7659	Yangibozor QFY	1	t	166
7660	Yangiobod MFY	1	t	166
7661	Yashlik MFY	1	t	166
7662	A Ikromov MFY	1	t	167
7663	A.Navoiy MFY	1	t	167
7664	A.Ortikov QFY	1	t	167
7665	Axil MFY	1	t	167
7666	Baxor MFY	1	t	167
7667	Baytish MFY	1	t	167
7668	Bogbon MFY	1	t	167
7669	Boz suv shaxarcha MFY	1	t	167
7670	Chamanzor MFY	1	t	167
7671	Chang tepa MFY	1	t	167
7672	Chortok MFY	1	t	167
7673	Dexkonobod MFY	1	t	167
7674	Dangir MFY	1	t	167
7675	Darxon MFY	1	t	167
7676	Do`stlik MFY	1	t	167
7677	Do`stlik MFY	1	t	167
7678	E.Kovunchi QFY	1	t	167
7679	Epkendi MFY	1	t	167
7680	Farxod MFY	1	t	167
7681	Fayzobod MFY	1	t	167
7682	Galaba MFY	1	t	167
7683	Gulbaxor MFY	1	t	167
7684	Gulbaxor shaxarcha MFY	1	t	167
7685	Gulbog MFY	1	t	167
7686	Guliston MFY	1	t	167
7687	I.Urazov MFY	1	t	167
7688	Inogomov MFY	1	t	167
7689	Ishchilar shaxarchasi MFY	1	t	167
7690	Isloxat MFY	1	t	167
7691	Ittifok MFY	1	t	167
7692	Ittifok MFY	1	t	167
7693	Jambul MFY	1	t	167
7694	King kechik MFY	1	t	167
7695	Kirimkulov MFY	1	t	167
7696	Keskan MFY	1	t	167
7697	Kirsadik MFY	1	t	167
7698	Kora tepa MFY	1	t	167
7699	Kovunchi MFY	1	t	167
7700	KukalamzorMFY	1	t	167
7701	Kush tepa MFY	1	t	167
7702	Kush yogoch MFY	1	t	167
7703	Kush yogoch QFY	1	t	167
7704	Mezon MFY	1	t	167
7705	Madaniyat MFY	1	t	167
7706	Markaz MFY	1	t	167
7707	Mirishkor MFY	1	t	167
7708	Mirzababaev MFY	1	t	167
7709	Muqumiy MFY	1	t	167
7710	Mustakillik MFY	1	t	167
7711	Mustaqillik MFY	1	t	167
7712	N.Niyozov MFY	1	t	167
7713	Namuna MFY	1	t	167
7714	Navbaxor MFY	1	t	167
7715	Navbaxor QFY	1	t	167
7716	Navro`z MFY	1	t	167
7717	Navruz MFY	1	t	167
7718	Navruz MFY	1	t	167
7719	Niyozbosh QFY	1	t	167
7720	Nodirabegim MFY	1	t	167
7721	Nov MFY	1	t	167
7722	Nurobod MFY	1	t	167
7723	Oltinobod MFY	1	t	167
7724	Oxunbabaev MFY	1	t	167
7725	Oybek MFY	1	t	167
7726	Paxta MFY	1	t	167
7727	Pistalik MFY	1	t	167
7728	Ramadon MFY	1	t	167
7729	Said ota MFY	1	t	167
7730	Saida Sultonova MFY	1	t	167
7731	Samarkand MFY	1	t	167
7732	Shuralisoy MFY	1	t	167
7733	Shuralisoy QFY	1	t	167
7734	Tuyabugiz MFY	1	t	167
7735	U.Musaev QFY	1	t	167
7736	Umid MFY	1	t	167
7737	Uzbekiston bekati MFY	1	t	167
7738	Uzbekiston MFY	1	t	167
7739	Vatan MFY	1	t	167
7740	Xakikat MFY	1	t	167
7741	Xalkobod MFY	1	t	167
7742	Xalqobod QFY	1	t	167
7743	Xonkurogon MFY	1	t	167
7744	Xo`jaobod MFY	1	t	167
7745	Yangiobod MFY(jamoatchi)	1	t	167
7746	Yangiyo`l MFY	1	t	167
7747	Yoshlik MFY	1	t	167
7748	Z.M. Bobur MFY	1	t	167
7749	Abdurazzoq ota MFY	1	t	168
7750	Abduvay MFY	1	t	168
7751	Andarxon QFY	1	t	168
7752	Arikboshi MFY	1	t	168
7753	Besharik QFY	1	t	168
7754	Beshkapa MFY	1	t	168
7755	Beshsari QFY	1	t	168
7756	Baxmal MFY	1	t	168
7757	Boy MFY	1	t	168
7758	Bulokboshi MFY	1	t	168
7759	Buston MFY	1	t	168
7760	Chimboy MFY	1	t	168
7761	Chinobod MFY	1	t	168
7762	Chorbog MFY	1	t	168
7763	Chorbogturangi	1	t	168
7764	D.X.Olimjon MFY	1	t	168
7765	Dexkonobod MFY	1	t	168
7766	Dexkontuda MFY	1	t	168
7767	Dultali MFY	1	t	168
7768	Eshon MFY	1	t	168
7769	Fayziobod MFY	1	t	168
7770	Galcha MFY	1	t	168
7771	Gambay MFY	1	t	168
7772	K.Zarkaynar MFY	1	t	168
7773	Kapayangi MFY	1	t	168
7774	Kashkar QFY	1	t	168
7775	Kiyali MFY	1	t	168
7776	Kiyat-Sartol MFY	1	t	168
7777	Korabuyin MFY	1	t	168
7778	Korajiyda QFY	1	t	168
7779	Korakuyli MFY	1	t	168
7780	Korayantok MFY	1	t	168
7781	Kulalobod MFY	1	t	168
7782	Kum MFY	1	t	168
7783	Kurgoncha MFY	1	t	168
7784	Nabi MFY	1	t	168
7785	Navbaxor MFY	1	t	168
7786	Navkat MFY	1	t	168
7787	Obod MFY	1	t	168
7788	Oktovuk MFY	1	t	168
7789	P.Yangikurgon MFY	1	t	168
7790	Pastki Yakkatut MFY	1	t	168
7791	Rapkon QFY	1	t	168
7792	Shaxar MFY	1	t	168
7793	Shaytonkul MFY	1	t	168
7794	Shoberdi MFY	1	t	168
7795	Shodlikobod MFY	1	t	168
7796	Shur MFY	1	t	168
7797	Sobirtepa MFY	1	t	168
7798	Soylabi MFY	1	t	168
7799	Tolov MFY	1	t	168
7800	Tosharik MFY	1	t	168
7801	Tovul QFY	1	t	168
7802	Uttizzambar MFY	1	t	168
7803	Uzun MFY	1	t	168
7804	Vatan QFY	1	t	168
7805	Vorux-Dasht MFY	1	t	168
7806	Xalqlar Do`stligi MFY	1	t	168
7807	Ya.Kashkar MFY	1	t	168
7808	Yakkatut QFY	1	t	168
7809	Yangi MFY	1	t	168
7810	Yangi Rapqon MFY	1	t	168
7811	Yangi Xayot MFY	1	t	168
7812	Yu,Zarkaynar MFY	1	t	168
7813	Yu.Tovul MFY	1	t	168
7814	Amirobod MFY	1	t	169
7815	Amirobod QFY	1	t	169
7816	Bedarak MFY	1	t	169
7817	Bekobod MFY	1	t	169
7818	Bag`dod SHFY	1	t	169
7819	Bag`dod-2 MFY	1	t	169
7820	Bog`ishamol MFY	1	t	169
7821	Bordon MFY	1	t	169
7822	Chekmirzaobod MFY	1	t	169
7823	Cheksaroy MFY	1	t	169
7824	Cho`l-Yunus MFY	1	t	169
7825	Cho`rindi MFY	1	t	169
7826	Chuvalanchi MFY	1	t	169
7827	Chuvalanchi QFY	1	t	169
7828	Dasht MFY	1	t	169
7829	Do`rmancha MFY	1	t	169
7830	Do`rmancha QFY	1	t	169
7831	Do`stlik MFY	1	t	169
7832	Irg`oli MFY	1	t	169
7833	Ittifoq MFY	1	t	169
7834	Karimbobo MFY	1	t	169
7835	Konizar MFY	1	t	169
7836	Ko`g`oli MFY	1	t	169
7837	Mexnatobod MFY	1	t	169
7838	Matqulobod MFY	1	t	169
7839	Matqulobod QFY	1	t	169
7840	Mirishkor MFY	1	t	169
7841	Mirzaobod MFY	1	t	169
7842	Muqimiy MFY	1	t	169
7843	Muruvvat MFY	1	t	169
7844	Olchin MFY	1	t	169
7845	Oydinbuloq MFY	1	t	169
7846	O`zbekiston MFY	1	t	169
7847	Paxtaobod QFY	1	t	169
7848	Qaroqchitol MFY	1	t	169
7849	Qashqari MFY	1	t	169
7850	Qaxat MFY	1	t	169
7851	Qirqboldi MFY	1	t	169
7852	Qorako`l MFY	1	t	169
7853	Qoroqchitol QFY	1	t	169
7854	Qorovultepa MFY	1	t	169
7855	Qo`shchinor MFY	1	t	169
7856	Qo`shtegirmon 1 MFY	1	t	169
7857	Qo`shtegirmon 2 MFY	1	t	169
7858	Samandarak MFY	1	t	169
7859	Samarqand MFY	1	t	169
7860	Samarqand QFY	1	t	169
7861	Sho`roqir MFY	1	t	169
7862	Tinchlik QFY	1	t	169
7863	Tuvadoq MFY	1	t	169
7864	Ultarma MFY	1	t	169
7865	Ultarma QFY	1	t	169
7866	Xitoy MFY	1	t	169
7867	Xo`jakishlok MFY	1	t	169
7868	Yuqori Mirzaobod MFY	1	t	169
7869	Zafarobod QFY	1	t	169
7870	Alkor QFY	1	t	170
7871	Beglar MFY	1	t	170
7872	Begobod QFY	1	t	170
7873	Begobod MFY	1	t	170
7874	Beshterak QFY	1	t	170
7875	Beshterak MFY	1	t	170
7876	Buvayda QFY	1	t	170
7877	Buvimozor MFY	1	t	170
7878	Chumbogish MFY	1	t	170
7879	Chutaka MFY	1	t	170
7880	Dexkonobod MFY	1	t	170
7881	Dodxo MFY	1	t	170
7882	Elobod MFY	1	t	170
7883	Ibrat SHFY	1	t	170
7884	Ingirchok MFY	1	t	170
7885	Jalor MFY	1	t	170
7886	Jov MFY	1	t	170
7887	Kilovt?pa MFY	1	t	170
7888	Korakum MFY	1	t	170
7889	Kum MFY	1	t	170
7890	Kungirot QFY	1	t	170
7891	Kurgoncha MFY	1	t	170
7892	Kurgonobod QFY	1	t	170
7893	Maslaxat MFY	1	t	170
7894	Nayman MFY	1	t	170
7895	Okkurgon QFY	1	t	170
7896	Oktepa MFY	1	t	170
7897	Oltinkurgon MFY	1	t	170
7898	Oyim MFY	1	t	170
7899	Ozod MFY	1	t	170
7900	Pishagar MFY	1	t	170
7901	Ponsod MFY	1	t	170
7902	Poshshopirim MFY	1	t	170
7903	Shur kishlok MFY	1	t	170
7904	Shur MFY	1	t	170
7905	Tepalik MFY	1	t	170
7906	Tarrachi MFY	1	t	170
7907	Toglik MFY	1	t	170
7908	Tuman MFY	1	t	170
7909	Turk MFY	1	t	170
7910	Urganji MFY	1	t	170
7911	Urta Kungirot MFY	1	t	170
7912	Uzumzor QFY	1	t	170
7913	Xakimto`ra MFY	1	t	170
7914	Xasankurgoncha MFY	1	t	170
7915	Xonobod MFY	1	t	170
7916	Xujauldi MFY	1	t	170
7917	Yangi xayot MFY	1	t	170
7918	Yangikadam QFY	1	t	170
7919	Yangikishlok MFY	1	t	170
7920	Yashnarobod MFY	1	t	170
7921	Yukori Mangit MFY	1	t	170
7922	Zarbuloq SHFY	1	t	170
7923	Abdusamad MFY	1	t	171
7924	Aravon MFY	1	t	171
7925	Arziqtepa MFY	1	t	171
7926	Bog`ish MFY	1	t	171
7927	Boy-bucha MFY	1	t	171
7928	Boy-buta MFY	1	t	171
7929	Burikum MFY	1	t	171
7930	Chinobod QFY	1	t	171
7931	Dang`ara SHFY	1	t	171
7932	Doimobod MFY	1	t	171
7933	G`alaba QFY	1	t	171
7934	Gumoyli MFY	1	t	171
7935	Kapasaroy MFY	1	t	171
7936	Katta Gajiravon MFY	1	t	171
7937	Katta-Amirobod MFY	1	t	171
7938	Katta-Oqtepa MFY	1	t	171
7939	Katta-turk MFY	1	t	171
7940	Kichik-turk MFY	1	t	171
7941	Mangit MFY	1	t	171
7942	Minglar MFY	1	t	171
7943	Mulkobod QFY	1	t	171
7944	Navbaxor MFY	1	t	171
7945	Naymancha QFY	1	t	171
7946	Oltikush MFY	1	t	171
7947	Oqjar QFY	1	t	171
7948	Pishkaron MFY	1	t	171
7949	Qashqar MFY	1	t	171
7950	Qiyali QFY	1	t	171
7951	Qiyali-qo`rg`oncha MFY	1	t	171
7952	Qizilmusht MFY	1	t	171
7953	Qora-kurpa MFY	1	t	171
7954	Qoramulla MFY	1	t	171
7955	Qumkiyali MFY	1	t	171
7956	Raxmatillo MFY	1	t	171
7957	Sanam QFY	1	t	171
7958	Shopo`lat MFY	1	t	171
7959	Soy-shildir MFY	1	t	171
7960	Teliming MFY	1	t	171
7961	Tangriqul MFY	1	t	171
7962	Taptiksaroy MFY	1	t	171
7963	Targova MFY	1	t	171
7964	Taypoq MFY	1	t	171
7965	Taypoq QFY	1	t	171
7966	To`laboy MFY	1	t	171
7967	Tumor MFY	1	t	171
7968	Urganji MFY	1	t	171
7969	Uvaysiy MFY	1	t	171
7970	Uymovut MFY	1	t	171
7971	Yangi-1 MFY	1	t	171
7972	Yashik MFY	1	t	171
7973	Guzarboshi MFY\r\n	1	t	172
7974	Beruniy MFY	1	t	172
7975	Boxor MFY	1	t	172
7976	Bo`tqachi MFY	1	t	172
7977	Cho`liguliston MFY	1	t	172
7978	Yoshlik MFY\r\n	1	t	172
7979	Gaston MFY	1	t	172
7980	Guliston QFY	1	t	172
7981	Qo├Жrg├Жoncha MFY\r\n	1	t	172
7982	Ishtirxon MFY\r\n	1	t	172
7983	Ittifoq MFY	1	t	172
7984	Porloq MFY\r\n	1	t	172
7985	Navro`z MFY	1	t	172
7986	Qorasaqol MFY\r\n	1	t	172
7987	Qorasoy MFY	1	t	172
7988	Qoratepa MFY\r\n	1	t	172
7989	Qotortol MFY \r\n	1	t	172
7990	 Do├Жstlik MFY\r\n	1	t	172
7991	Qum maxalla MFY	1	t	172
7992	Soybo├Жyi  MFY\r\n	1	t	172
7993	Yuqori Soybo├Жyi MFY\r\n	1	t	172
7994	Soyyoni MFY	1	t	172
7995	Suvliariq MFY	1	t	172
7996	Takalik MFY	1	t	172
7997	Toshxovuz MFY	1	t	172
7998	Tegirmonboshi MFY\r\n	1	t	172
7999	Xonobod MFY\r\n	1	t	172
8000	Yangibo├Жston MFY\r\n	1	t	172
8001	Yangiobod MFY	1	t	172
8002	Ijodkor MFY\r\n	1	t	172
8003	Markaziy Farg├Жona MFY\r\n	1	t	172
8004	Yozyovon MFY\r\n	1	t	172
8005	Yuqori   MFY\r\n	1	t	172
8006	Akbarobod QFY	1	t	173
8007	Baxor QFY	1	t	173
8008	Baynalminal QFY	1	t	173
8009	Bolalik MFY	1	t	173
8010	Boyiston MFY	1	t	173
8011	Chilon MFY	1	t	173
8012	Dexqonobod MFY	1	t	173
8013	Dexqonobod QFY	1	t	173
8014	Damariq MFY	1	t	173
8015	Do`stlik MFY	1	t	173
8016	G`alaba MFY	1	t	173
8017	Go`zal MFY	1	t	173
8018	Guliston MFY	1	t	173
8019	Gulobod MFY	1	t	173
8020	Iftixor QFY	1	t	173
8021	Ittifoq QFY	1	t	173
8022	Jalaler MFY	1	t	173
8023	Kandabuloq MFY	1	t	173
8024	Kattaqishloq MFY	1	t	173
8025	M.Xasanov MFY	1	t	173
8026	Madaniyat QFY	1	t	173
8027	Mustaqillik MFY	1	t	173
8028	Namuna QFY	1	t	173
8029	Nayman MFY	1	t	173
8030	Novk?nt MFY	1	t	173
8031	Oltiariq MFY	1	t	173
8032	Oqqo`rg`on MFY	1	t	173
8033	O`raboshi MFY	1	t	173
8034	O`zbekiston MFY	1	t	173
8035	Pandigon MFY	1	t	173
8036	Pastki Xo`ja-Xasan MFY	1	t	173
8037	Paxtakor MFY	1	t	173
8038	Qalinpo`stin MFY	1	t	173
8039	Qaqir MFY	1	t	173
8040	Qashqar-1 MFY	1	t	173
8041	Qashqar-2 MFY	1	t	173
8042	Qayirma MFY	1	t	173
8043	Qoraqum MFY	1	t	173
8044	Qorashox MFY	1	t	173
8045	Qo`rg`oncha MFY	1	t	173
8046	Quva MFY	1	t	173
8047	Rasta MFY	1	t	173
8048	Sanoatchilar SHFY	1	t	173
8049	Soykeldi MFY	1	t	173
8050	So`fi MFY	1	t	173
8051	Sultonobod MFY	1	t	173
8052	Taxtako`prik MFY	1	t	173
8053	Tinchlik MFY	1	t	173
8054	Tojik MFY	1	t	173
8055	Tolmozor MFY	1	t	173
8056	Toshkent MFY	1	t	173
8057	Toshxovuz MFY	1	t	173
8058	Turk MFY	1	t	173
8059	Turkravot QFY	1	t	173
8060	Xonobod MFY	1	t	173
8061	Yangich?k MFY	1	t	173
8062	Yangiobod MFY	1	t	173
8063	Yangiqishloq MFY	1	t	173
8064	Yangiqishloq QFY	1	t	173
8065	Yangixayot MFY	1	t	173
8066	Yangixayot QFY	1	t	173
8067	Yuziya MFY	1	t	173
8068	A.Novoiy MFY	1	t	174
8069	A.Temur MFY	1	t	174
8070	Arsif QFY	1	t	174
8071	Bog`bon MFY	1	t	174
8072	Bo`ston MFY	1	t	174
8073	Cho`lpon MFY	1	t	174
8074	Do`stlik SHFY	1	t	174
8075	Guliston MFY	1	t	174
8076	Isfayramsoy QFY	1	t	174
8077	Kalacha MFY	1	t	174
8078	Kokilon MFY	1	t	174
8079	Lashkar MFY	1	t	174
8080	M.Ulug`bek MFY	1	t	174
8081	Muyan MFY	1	t	174
8082	Namuna MFY	1	t	174
8083	Nayman SHFY	1	t	174
8084	Pakana MFY	1	t	174
8085	Polmon MFY	1	t	174
8086	Quchqorchi QFY	1	t	174
8087	S.Raximov MFY	1	t	174
8088	Soy-bo`yi MFY	1	t	174
8089	Sufon QFY	1	t	174
8090	Valik QFY	1	t	174
8091	X.Olimjon MFY	1	t	174
8092	Xuvaydo MFY	1	t	174
8093	Yangi obod MFY	1	t	174
8094	Yoshlik MFY	1	t	174
8095	Yu.Muyan MFY	1	t	174
8096	Zebuniso MFY	1	t	174
8097	Ziynat MFY	1	t	174
8098	A Navoiy MFY	1	t	175
8099	Achchiqko`l MFY	1	t	175
8100	Afg`onbog` MFY	1	t	175
8101	Artizon bo`yi MFY	1	t	175
8102	Arzik tepa MFY	1	t	175
8103	Ashurali zoxiriy MFY	1	t	175
8104	At-Termiziy MFY	1	t	175
8105	Birlik MFY	1	t	175
8106	Bo`ston MFY	1	t	175
8107	Buloqboshi MFY	1	t	175
8108	Bunyodkor MFY	1	t	175
8109	Charxini ko`prigi MFY	1	t	175
8110	D?grezlik MFY	1	t	175
8111	Davronbek MFY	1	t	175
8112	Do`stlik MFY	1	t	175
8113	g`alchasoy MFY	1	t	175
8114	g`ishtko`prik MFY	1	t	175
8115	g`ishtli masjid MFY	1	t	175
8116	g`oziyog`lik MFY	1	t	175
8117	Gala baqollik MFY	1	t	175
8118	Isfara guzar MFY	1	t	175
8119	Islomobod MFY	1	t	175
8120	Istiqlol MFY	1	t	175
8121	Ittifoq MFY	1	t	175
8122	Jumxuriyat MFY	1	t	175
8123	Kalvak MFY	1	t	175
8124	Marg`ilon darvozasi MFY	1	t	175
8125	Misgarlik MFY	1	t	175
8126	Muqimiy MFY	1	t	175
8127	Mustaqillik MFY	1	t	175
8128	Navbaxor MFY	1	t	175
8129	Navruz MFY	1	t	175
8130	Noib ko`prigi MFY	1	t	175
8131	Nonvoylikguzar MFY	1	t	175
8132	Nurafshon MFY	1	t	175
8133	Oq oltin MFY	1	t	175
8134	Ozodlik MFY	1	t	175
8135	O`rmon bog` MFY	1	t	175
8136	Parpashabof MFY	1	t	175
8137	Qalandarxona MFY	1	t	175
8138	Qaymoqli guzar MFY	1	t	175
8139	Qipchoq ariq MFY	1	t	175
8140	Qo`sh chinor MFY	1	t	175
8141	Quduqlik MFY	1	t	175
8142	Rayxon MFY	1	t	175
8143	Saodat MFY	1	t	175
8144	Shaldiramoq MFY	1	t	175
8145	Shayxon MFY	1	t	175
8146	Shikor begi MFY	1	t	175
8147	Shirin MFY	1	t	175
8148	Sobir Abdulla MFY	1	t	175
8149	Sunbula MFY	1	t	175
8150	Temir yo`lchi MFY	1	t	175
8151	Tolzor MFY	1	t	175
8152	Tug`onboshi MFY	1	t	175
8153	Tuxlimergan MFY	1	t	175
8154	Urganjibog` MFY	1	t	175
8155	Usta bozor MFY	1	t	175
8156	Vaqf chorsu MFY	1	t	175
8157	Xo`jand Daxasi MFY	1	t	175
8158	Xurlik MFY	1	t	175
8159	Yalong`och ota MFY	1	t	175
8160	Yangi chorsu MFY	1	t	175
8161	Yangi obod MFY	1	t	175
8162	Yog` bozori MFY	1	t	175
8163	Baland - Masjid MFY	1	t	176
8164	Barot MFY	1	t	176
8165	Boltakul SHFY	1	t	176
8166	Buston MFY	1	t	176
8167	Dexkonobod MFY	1	t	176
8168	Durmon MFY	1	t	176
8169	Durmon SHFY	1	t	176
8170	Eshonguzar MFY	1	t	176
8171	Fayz QFY	1	t	176
8172	Garimdon MFY	1	t	176
8173	Gishtmon MFY	1	t	176
8174	Gishtmon SHFY	1	t	176
8175	Istikbol MFY	1	t	176
8176	Karnaychi MFY	1	t	176
8177	Kattabeshkapa SHFY	1	t	176
8178	Kichikbeshkapa MFY	1	t	176
8179	Kiyki MFY	1	t	176
8180	Kora-arik SHFY	1	t	176
8181	Korajiyda SHFY	1	t	176
8182	Korakaltak MFY	1	t	176
8183	Korakushchi QFY	1	t	176
8184	Kumtpa QFY	1	t	176
8185	Kumtepa SHFY	1	t	176
8186	Kuprik boshi MFY	1	t	176
8187	Kurgoncha MFY	1	t	176
8188	Langar MFY	1	t	176
8189	Langar QFY	1	t	176
8190	Loyson QFY	1	t	176
8191	Oyimcha MFY	1	t	176
8192	Paxtakor QFY	1	t	176
8193	Qo`yi oktepa SHFY	1	t	176
8194	Sarmazor QFY	1	t	176
8195	Sarmazor SHFY	1	t	176
8196	Shakar MFY	1	t	176
8197	Shaxartepa QFY	1	t	176
8198	Shomirza MFY	1	t	176
8199	Solijonobod QFY	1	t	176
8200	Soy-buyi MFY	1	t	176
8201	Ukchi QFY	1	t	176
8202	Urta - ukchi MFY	1	t	176
8203	Vatan MFY	1	t	176
8204	Xalkabod QFY	1	t	176
8205	Xotinarik SHFY	1	t	176
8206	Xujakishlok MFY	1	t	176
8207	Yangi dukan MFY	1	t	176
8208	Yangiarik SHFY	1	t	176
8209	Yuldashobod QFY	1	t	176
8210	Erkin MFY	1	t	177
8211	Evkochar MFY	1	t	177
8212	A.Navoiy MFY	1	t	177
8213	A.Yassaviy MFY	1	t	177
8214	Ariq bo`yi MFY	1	t	177
8215	B.Margiloniy MFY	1	t	177
8216	Baxrin MFY	1	t	177
8217	Baynalminal MFY	1	t	177
8218	Bobur MFY	1	t	177
8219	Charog`on MFY	1	t	177
8220	Chilonzor MFY	1	t	177
8221	Chorchinor MFY	1	t	177
8222	Do`stlik MFY	1	t	177
8223	Galatoy MFY	1	t	177
8224	Go`ravvol MFY	1	t	177
8225	Guliston MFY	1	t	177
8226	Ikbol MFY	1	t	177
8227	Ipak yo`li MFY	1	t	177
8228	Ipakchi MFY	1	t	177
8229	Istiqlol MFY	1	t	177
8230	Kashkar MFY	1	t	177
8231	Kirguli MFY	1	t	177
8232	Kosibchilik MFY	1	t	177
8233	Maorif MFY	1	t	177
8234	Mashad MFY	1	t	177
8235	Miltiqsoz MFY	1	t	177
8236	Mustaqillik MFY	1	t	177
8237	Nadirmat MFY	1	t	177
8238	Navbaxor MFY	1	t	177
8239	Navruz MFY	1	t	177
8240	Orol bo`yi MFY	1	t	177
8241	Oxunboboev MFY	1	t	177
8242	O`rda tagi MFY	1	t	177
8243	Pichokchi MFY	1	t	177
8244	Roxat MFY	1	t	177
8245	Saxovat MFY	1	t	177
8246	Sholdirama MFY	1	t	177
8247	Terak tagi MFY	1	t	177
8248	Tog`lik MFY	1	t	177
8249	Toshkesar MFY	1	t	177
8250	Toshloq tepa MFY	1	t	177
8251	Turon MFY	1	t	177
8252	Tut tagi MFY	1	t	177
8253	Tuyagum MFY	1	t	177
8254	Uvaysiy MFY	1	t	177
8255	Uzumzor MFY	1	t	177
8256	Uzun xovuz MFY	1	t	177
8257	Vatan MFY	1	t	177
8258	Yagi obod MFY	1	t	177
8259	Yangi bog` MFY	1	t	177
8260	Yangi Marg`ilon MFY	1	t	177
8261	Yangi xat MFY	1	t	177
8262	Yayilma MFY	1	t	177
8263	Yo`rmado`z MFY	1	t	177
8264	Zuxro MFY	1	t	177
8265	Azimobod SHFY	1	t	178
8266	Beglar MFY	1	t	178
8267	Beruniy MFY	1	t	178
8268	Beshkovok MFY	1	t	178
8269	Birlashgan MFY	1	t	178
8270	Bozorboshi MFY	1	t	178
8271	Bugdoychi MFY	1	t	178
8272	Bunyodkor MFY	1	t	178
8273	Burbonlik SHFY	1	t	178
8274	Buston MFY	1	t	178
8275	Butabekov MFY	1	t	178
8276	Chinor SHFY	1	t	178
8277	Chinortagi MFY	1	t	178
8278	Do`stlik MFY	1	t	178
8279	Eskiarab SHFY	1	t	178
8280	Farovon MFY	1	t	178
8281	Fayziobod QFY	1	t	178
8282	Gayrat-1 MFY	1	t	178
8283	Gulobod MFY	1	t	178
8284	Ibn Sino MFY	1	t	178
8285	Jararik MFY	1	t	178
8286	Jarkurgon MFY	1	t	178
8287	Jonibek MFY	1	t	178
8288	Jurak SHFY	1	t	178
8289	Kapchugay QFY	1	t	178
8290	Katput SHFY	1	t	178
8291	Kaxramon MFY	1	t	178
8292	Kiziltepa QFY	1	t	178
8293	Kokir MFY	1	t	178
8294	Kulbuyi MFY	1	t	178
8295	Kumirchi MFY	1	t	178
8296	Kurgoncha MFY	1	t	178
8297	Kuvirboshi MFY	1	t	178
8298	Maorif MFY	1	t	178
8299	Mirfozil MFY	1	t	178
8300	Mukimiy MFY	1	t	178
8301	Mustakillik MFY	1	t	178
8302	Navkuron MFY	1	t	178
8303	Navoiy MFY	1	t	178
8304	Obod MFY	1	t	178
8305	Okbuyra SHFY	1	t	178
8306	Olmazor MFY	1	t	178
8307	Oltiarik SHFY	1	t	178
8308	Pavulgon SHFY	1	t	178
8309	Poloson SHFY	1	t	178
8310	Sertut MFY	1	t	178
8311	Shalola MFY	1	t	178
8312	Shark MFY	1	t	178
8313	Sodiyona MFY	1	t	178
8314	Shodlik MFY	1	t	178
8315	Tegirmonboshi MFY	1	t	178
8316	Tinchlik MFY	1	t	178
8317	Tinchlik SHFY	1	t	178
8318	Tolkucha MFY	1	t	178
8319	Toshkent MFY	1	t	178
8320	Toshobod MFY	1	t	178
8321	Usmonobod MFY	1	t	178
8322	Ustoz MFY	1	t	178
8323	Uzbekiston MFY	1	t	178
8324	Uzumchi MFY	1	t	178
8325	X.Olimjon MFY	1	t	178
8326	Yangi Fargona MFY	1	t	178
8327	Yangiarab MFY	1	t	178
8328	Yangiarab SHFY	1	t	178
8329	Yangiarik MFY	1	t	178
8330	Yangichek MFY	1	t	178
8331	Yangikurgon SHFY	1	t	178
8332	Yangiturmush MFY	1	t	178
8333	Yangixayot MFY	1	t	178
8334	Yoshlik MFY	1	t	178
8335	Yuksalish MFY	1	t	178
8336	Zarxal MFY	1	t	178
8337	Zilxa SHFY	1	t	178
8338	Yangi yul	1	t	179
8339	A.Navoiy MFY	1	t	179
8340	Amirobod	1	t	179
8341	Arik buyi	1	t	179
8342	Beshkapa SHFY	1	t	179
8343	Birlashgan	1	t	179
8344	Bogiston MFY	1	t	179
8345	Bujay	1	t	179
8346	Bulokboshi	1	t	179
8347	Buston	1	t	179
8348	Buston QFY	1	t	179
8349	Chek Jaler	1	t	179
8350	Chek Nasriddin	1	t	179
8351	Chinigaron MFY	1	t	179
8352	Chuburgon	1	t	179
8353	Chungara	1	t	179
8354	Dexkonobod MFY	1	t	179
8355	Dasht Pandigon	1	t	179
8356	Dasht Tegirmon	1	t	179
8357	Daxb?d MFY	1	t	179
8358	Dorilomon MFY	1	t	179
8359	Dutir	1	t	179
8360	Farovonlik MFY	1	t	179
8361	Guliston	1	t	179
8362	Gumbaz MFY	1	t	179
8363	Guzar	1	t	179
8364	Istikbol MFY	1	t	179
8365	Jalaer	1	t	179
8366	Jaxonobod	1	t	179
8367	Kalaynav	1	t	179
8368	Kayragoch QFY	1	t	179
8369	Koshkayron MFY	1	t	179
8370	Kozi-Axror MFY	1	t	179
8371	Kurgoncha	1	t	179
8372	Kuyi Avazboy	1	t	179
8373	M.Topvoldi?v MFY	1	t	179
8374	Mevazor	1	t	179
8375	Mexnatobod	1	t	179
8376	Mexnatobod QFY	1	t	179
8377	Markaz MFY	1	t	179
8378	Minor MFY	1	t	179
8379	Miskin MFY	1	t	179
8380	Mustofokul - ota	1	t	179
8381	Navbaxor	1	t	179
8382	Nosgar MFY	1	t	179
8383	o`Sobirov MFY	1	t	179
8384	Ok-er	1	t	179
8385	Ok-er SHFY	1	t	179
8386	Ok-oltin QFY	1	t	179
8387	Ok-tomir	1	t	179
8388	Pandigon	1	t	179
8389	Pastki Beshkapa	1	t	179
8390	Pastki Bulokboshi	1	t	179
8391	Rishton QFY	1	t	179
8392	Shokir-ota MFY	1	t	179
8393	Suxobod	1	t	179
8394	T`axmedov	1	t	179
8395	Toshogolik MFY	1	t	179
8396	Tuda QFY	1	t	179
8397	Turaobod	1	t	179
8398	Ucharik	1	t	179
8399	Uyrat SHFY	1	t	179
8400	Uzunkucha	1	t	179
8401	Voxim	1	t	179
8402	Xoji-kishlok	1	t	179
8403	Xuja-Ilgor MFY	1	t	179
8404	Xurramobod	1	t	179
8405	Yangi Bujay	1	t	179
8406	Yoshlik	1	t	179
8407	Yyilma QFY	1	t	179
8408	Yukori Avazboy	1	t	179
8409	Yukori Beshkapa	1	t	179
8410	Zar-arik MFY	1	t	179
8411	Zoxidon SHFY	1	t	179
8412	Bobokalon QFY	1	t	180
8413	Chashma MFY	1	t	180
8414	Chumokcha MFY	1	t	180
8415	Demursad MFY	1	t	180
8416	Devayron MFY	1	t	180
8417	Gaznov MFY	1	t	180
8418	Guliston MFY	1	t	180
8419	Istiqlol MFY	1	t	180
8420	Kakir MFY	1	t	180
8421	Kal`a MFY	1	t	180
8422	Kal`acha MFY	1	t	180
8423	Kizilkiyok MFY	1	t	180
8424	Lenbur MFY	1	t	180
8425	Mulgon MFY	1	t	180
8426	Navobod MFY	1	t	180
8427	Oftobru MFY	1	t	180
8428	Oxunboboev QFY	1	t	180
8429	Saribozorcha MFY	1	t	180
8430	Sarikanda MFY	1	t	180
8431	Sharkobod MFY	1	t	180
8432	Sux QFY	1	t	180
8433	Tul MFY	1	t	180
8434	Xusheyor QFY	1	t	180
8435	Yangiarik MFY	1	t	180
8436	Arabmozor QFY	1	t	181
8437	Axshak QFY	1	t	181
8438	Axshakguzar MFY	1	t	181
8439	Aylanmajar MFY	1	t	181
8440	Besarang MFY	1	t	181
8441	Birlik QFY	1	t	181
8442	Bo`ston MFY	1	t	181
8443	Chek MFY	1	t	181
8444	Chuqurkishloq MFY	1	t	181
8445	Do`stlik MFY	1	t	181
8446	Farg`ona MFY	1	t	181
8447	Furqat MFY	1	t	181
8448	Guzarboshi MFY	1	t	181
8449	Jarqishloq MFY	1	t	181
8450	Kattako`cha MFY	1	t	181
8451	Konizar MFY	1	t	181
8452	Ko`larik MFY	1	t	181
8453	Ko`rg`oncha QFY	1	t	181
8454	Ko`saqishloq MFY	1	t	181
8455	Mexnatobod MFY	1	t	181
8456	Nayman QFY	1	t	181
8457	Naymanbo`ston QFY	1	t	181
8458	Obisiyo MFY	1	t	181
8459	Oxunboboev MFY	1	t	181
8460	O`zbekiston MFY	1	t	181
8461	Piyozchilik MFY	1	t	181
8462	Qamchipurush MFY	1	t	181
8463	Qanjirg`a MFY	1	t	181
8464	Qipchoqariq MFY	1	t	181
8465	Qumariq QFY	1	t	181
8466	Qumqishloq MFY	1	t	181
8467	Sadda QFY	1	t	181
8468	Shilva MFY	1	t	181
8469	Soybo`yi MFY	1	t	181
8470	So`filar MFY	1	t	181
8471	So`kchilik MFY	1	t	181
8472	Suvboshi MFY	1	t	181
8473	Tegirmonboshi MFY	1	t	181
8474	Teraktagi MFY	1	t	181
8475	Tog`lik MFY	1	t	181
8476	Toshloq SHFY	1	t	181
8477	To`xtaboev QFY	1	t	181
8478	Turvat MFY	1	t	181
8479	Ucholish MFY	1	t	181
8480	Varzak QFY	1	t	181
8481	Xamrak MFY	1	t	181
8482	Xonaqa MFY	1	t	181
8483	Xonariq MFY	1	t	181
8484	Xotinqumi MFY	1	t	181
8485	Xo`jariq MFY	1	t	181
8486	Yakkavut MFY	1	t	181
8487	Yangiyo`l MFY	1	t	181
8488	Yuqoriqishloq MFY	1	t	181
8489	Zarkent MFY	1	t	181
8490	Kata-Kushtepa MFY	1	t	182
8491	Begmurod MFY	1	t	182
8492	Begobod SHFY	1	t	182
8493	Beshkapa MFY	1	t	182
8494	Baxrin MFY	1	t	182
8495	Boboshb?k MFY	1	t	182
8496	Buyrak MFY	1	t	182
8497	Chang MFY	1	t	182
8498	Chorbog` QFY	1	t	182
8499	G`ijdon SHFY	1	t	182
8500	G`ozig`ijdon QFY	1	t	182
8501	Kenagas QFY	1	t	182
8502	Kata-Kashkar MFY	1	t	182
8503	Kata-Korakul MFY	1	t	182
8504	Kattakenagas MFY	1	t	182
8505	Kichik-Kenagas MFY	1	t	182
8506	Korayantok MFY	1	t	182
8507	Kumarik SHFY	1	t	182
8508	Kurbonkashkar MFY	1	t	182
8509	Mergan MFY	1	t	182
8510	Mexnatobod QFY	1	t	182
8511	Mashad MFY	1	t	182
8512	Mirzaxuja MFY	1	t	182
8513	Navruz QFY	1	t	182
8514	Olmurod MFY	1	t	182
8515	Paloxon QFY	1	t	182
8516	Paloxon SHFY	1	t	182
8517	Puchugoy MFY	1	t	182
8518	Qo`qonboy SHFY	1	t	182
8519	Sarikurgon QFY	1	t	182
8520	Sarikurgon MFY	1	t	182
8521	Sobirjon SHFY	1	t	182
8522	Sulton MFY	1	t	182
8523	Tepakurgon MFY	1	t	182
8524	Toshkentliguzar MFY	1	t	182
8525	Tuksonkovun MFY	1	t	182
8526	Turgok MFY	1	t	182
8527	Uchkuprik QFY	1	t	182
8528	Uchkuprik SHFY	1	t	182
8529	Xasankora MFY	1	t	182
8530	Yakkamulla MFY	1	t	182
8531	Yakkatut MFY	1	t	182
8532	Yangier MFY	1	t	182
8533	Yangikishlok QFY	1	t	182
8534	Yangikishlok SHFY	1	t	182
8535	Yangiobod MFY	1	t	182
8536	Yulgunzor MFY	1	t	182
8537	Zigir MFY	1	t	182
8538	A. Jomiy MFY	1	t	183
8539	Akbarobod MFY	1	t	183
8540	Avgon MFY	1	t	183
8541	Bekabod MFY	1	t	183
8542	Beruniy MFY	1	t	183
8543	Bozor yaypan MFY	1	t	183
8544	Buston MFY	1	t	183
8545	Buzukkurgon MFY	1	t	183
8546	Dexkonobod MFY	1	t	183
8547	Dasht-chulpon MFY	1	t	183
8548	Daxanakakir MFY	1	t	183
8549	Dungsaroy MFY	1	t	183
8550	Elchi MFY	1	t	183
8551	Eski Yaypan MFY	1	t	183
8552	g`anobod QFY	1	t	183
8553	Gusht MFY	1	t	183
8554	Islom MFY	1	t	183
8555	Karimdevona MFY	1	t	183
8556	Katagon MFY	1	t	183
8557	Kaykubod MFY	1	t	183
8558	Kaynar QFY	1	t	183
8559	Kichik Okmachit MFY	1	t	183
8560	Kichik tagob MFY	1	t	183
8561	Kirketmon MFY	1	t	183
8562	Kizil-kakir QFY	1	t	183
8563	Kizil-kakir MFY	1	t	183
8564	Kizilbog MFY	1	t	183
8565	Konizar QFY	1	t	183
8566	Kota tagob MFY	1	t	183
8567	Kudash MFY	1	t	183
8568	Kul elash MFY	1	t	183
8569	Kulbek MFY	1	t	183
8570	Kum MFY	1	t	183
8571	Kumbosti MFY	1	t	183
8572	Kurgoncha MFY	1	t	183
8573	Kushkunok MFY	1	t	183
8574	Ming tut QFY	1	t	183
8575	Nursux QFY	1	t	183
8576	Okmachit MFY	1	t	183
8577	Oktepa MFY	1	t	183
8578	Olmazor MFY	1	t	183
8579	Ovchi QFY	1	t	183
8580	Ovchi MFY	1	t	183
8581	Oxunboboev QFY	1	t	183
8582	Oxunboboev MFY	1	t	183
8583	Oyimchakakir MFY	1	t	183
8584	O`qchi-dasht MFY	1	t	183
8585	Pastkurik MFY	1	t	183
8586	Rajabgardi MFY	1	t	183
8587	Rajabgardi QFY	1	t	183
8588	Shur kishlok MFY	1	t	183
8589	Shursuv SHFY	1	t	183
8590	Sochtepa MFY	1	t	183
8591	Tagob QFY	1	t	183
8592	Tovar MFY	1	t	183
8593	Turkiston MFY	1	t	183
8594	Tuyul MFY	1	t	183
8595	Uch bulak MFY	1	t	183
8596	Urta kishlok MFY	1	t	183
8597	Xaydarobod MFY	1	t	183
8598	Xotamitoy MFY	1	t	183
8599	Yakatut MFY	1	t	183
8600	Zinasha MFY	1	t	183
8601	Avval QFY	1	t	184
8602	Beruniy MFY	1	t	184
8603	Barkaror xam MFY	1	t	184
8604	Boy maxalla MFY	1	t	184
8605	Buston MFY	1	t	184
8606	Chek shura QFY	1	t	184
8607	Chimyon QFY	1	t	184
8608	Chimyon SHFY	1	t	184
8609	D.U.Toshboy MFY	1	t	184
8610	Damkul QFY	1	t	184
8611	Fargona MFY	1	t	184
8612	Guliston MFY	1	t	184
8613	Gulpiyon MFY	1	t	184
8614	Gulshan QFY	1	t	184
8615	Guzar MFY	1	t	184
8616	I.Siddikov MFY	1	t	184
8617	Ilgor MFY	1	t	184
8618	Kaptarxona QFY	1	t	184
8619	Korasuv MFY	1	t	184
8620	Korayantok MFY	1	t	184
8621	Kurgontepa QFY	1	t	184
8622	Kurik MFY	1	t	184
8623	Kurilish MFY	1	t	184
8624	Langar MFY	1	t	184
8625	Log`on QFY	1	t	184
8626	Mexnatobod MFY	1	t	184
8627	Margilon MFY	1	t	184
8628	Mash`al MFY	1	t	184
8629	Maydon MFY	1	t	184
8630	Mindon QFY	1	t	184
8631	Mindonobod MFY	1	t	184
8632	Mirzaolim MFY	1	t	184
8633	Mozortagi MFY	1	t	184
8634	Navruz MFY	1	t	184
8635	Novkent QFY	1	t	184
8636	Obod MFY	1	t	184
8637	Ok-oltin MFY	1	t	184
8638	Okbilol QFY	1	t	184
8639	Oktepa MFY	1	t	184
8640	Oktom MFY	1	t	184
8641	Paski Archa MFY	1	t	184
8642	Sanoat MFY	1	t	184
8643	Satkak MFY	1	t	184
8644	Sattorobod MFY	1	t	184
8645	Sh.Xakikati MFY	1	t	184
8646	Shifokor MFY	1	t	184
8647	Shoximardon QFY	1	t	184
8648	Shoximardonobod MFY	1	t	184
8649	Soybo`yi QFY	1	t	184
8650	Tinchlik MFY	1	t	184
8651	U.Shaxobov MFY	1	t	184
8652	Ulugbek MFY	1	t	184
8653	Urta kishlok MFY	1	t	184
8654	Uzbekiston MFY	1	t	184
8655	Vaziyo MFY	1	t	184
8656	Vodil QFY	1	t	184
8657	XA.Val? MFY	1	t	184
8658	X.Obilol MFY	1	t	184
8659	X.Zayni?v MFY	1	t	184
8660	Xonkiz QFY	1	t	184
8661	Xuroba MFY	1	t	184
8662	Yanbarok MFY	1	t	184
8663	Yangi yul MFY	1	t	184
8664	Yangiobod MFY	1	t	184
8665	Yordon MFY	1	t	184
8666	Yoyilma MFY	1	t	184
8667	Yu.Vodil QFY	1	t	184
8668	Yuqori Archa MFY	1	t	184
8669	Yuqori Gulshan MFY	1	t	184
8670	Yuqori Mindon MFY	1	t	184
8671	Zilol MFY	1	t	184
8672	1-Besh bola MFY	1	t	185
8673	A.Jomiy MFY	1	t	185
8674	A.Navoiy MFY	1	t	185
8675	A.Qodiriy MFY	1	t	185
8676	A.Xorazmiy MFY	1	t	185
8677	Al-Farg`oniy MFY	1	t	185
8678	Beglar MFY	1	t	185
8679	Beruniy MFY	1	t	185
8680	Besh-bola MFY	1	t	185
8681	Barkamol MFY	1	t	185
8682	Baxor MFY	1	t	185
8683	Bobur MFY	1	t	185
8684	Bo`ston MFY	1	t	185
8685	Do`stlik MFY	1	t	185
8686	Farg`ona MFY	1	t	185
8687	Guliston MFY	1	t	185
8688	Gulzor MFY	1	t	185
8689	Ibn-Sino MFY	1	t	185
8690	Ibrat MFY	1	t	185
8691	Iftixor MFY	1	t	185
8692	Ipak yo`li MFY	1	t	185
8693	Istiqbol MFY	1	t	185
8694	Istiqlol MFY	1	t	185
8695	Jo`ydam MFY	1	t	185
8696	Kimyogar MFY	1	t	185
8697	Kirguli MFY	1	t	185
8698	Lolazor MFY	1	t	185
8699	M.Ulug`b?k MFY	1	t	185
8700	Mexribonlik MFY	1	t	185
8701	Maarifat MFY	1	t	185
8702	Madadkor MFY	1	t	185
8703	Madaniyat MFY	1	t	185
8704	Mashaal MFY	1	t	185
8705	Muruvvat MFY	1	t	185
8706	Mustaqillik MFY	1	t	185
8707	Nafosat MFY	1	t	185
8708	Navbaxor MFY	1	t	185
8709	Navro`z MFY	1	t	185
8710	Nodirabegim MFY	1	t	185
8711	Oqariq MFY	1	t	185
8712	Oqariqobod MFY	1	t	185
8713	Oybek MFY	1	t	185
8714	Ozodlik MFY	1	t	185
8715	O`rmonchilar MFY	1	t	185
8716	O`zbekiston MFY	1	t	185
8717	Parvoz MFY	1	t	185
8718	S.Raximov MFY	1	t	185
8719	S.Temur MFY	1	t	185
8720	Sh.Rashidov MFY	1	t	185
8721	Shakarqishlo MFY	1	t	185
8722	Sharshara MFY	1	t	185
8723	Shodiyona MFY	1	t	185
8724	Shodlik MFY	1	t	185
8725	Simtepa MFY	1	t	185
8726	Sovurbuloq MFY	1	t	185
8727	Soxibkor MFY	1	t	185
8728	Soy-bo`yi MFY	1	t	185
8729	Surxtepa MFY	1	t	185
8730	Tabassum MFY	1	t	185
8731	Tinchlik MFY	1	t	185
8732	To`qimachilar MFY	1	t	185
8733	Xamkorlik MFY	1	t	185
8734	Xujamag`iz MFY	1	t	185
8735	Xuvaydo MFY	1	t	185
8736	Yangi soy MFY	1	t	185
8737	Yangi yo`l MFY	1	t	185
8738	Yormozor MFY	1	t	185
8739	Yoshlar MFY	1	t	185
8740	Yulduz MFY	1	t	185
8741	Zarbdor MFY	1	t	185
8742	Ardaxshon MFY	1	t	186
8743	Bekobod MFY	1	t	186
8744	Besh-og`a MFY	1	t	186
8745	Boltako`l MFY	1	t	186
8746	Chek-chuvaldoq MFY	1	t	186
8747	Chilgi-jiyda MFY	1	t	186
8748	Chirkay MFY	1	t	186
8749	Eshon MFY	1	t	186
8750	Eski MFY	1	t	186
8751	g`allakor QFY	1	t	186
8752	g`uncha QFY	1	t	186
8753	Ingichka MFY	1	t	186
8754	Jang-ketmon MFY	1	t	186
8755	Kaldushon MFY	1	t	186
8756	Karmak MFY	1	t	186
8757	Katta-yangi MFY	1	t	186
8758	Kichik-yangi MFY	1	t	186
8759	Ko`k-do`ppi MFY	1	t	186
8760	Mustaqillik MFY	1	t	186
8761	Navbaxor MFY	1	t	186
8762	Navbaxor QFY	1	t	186
8763	O`rta-qo`rg`on MFY	1	t	186
8764	Polvontosh MFY	1	t	186
8765	Qizil-qiyaq MFY	1	t	186
8766	Qo`qon QFY	1	t	186
8767	Qo`qonboy MFY	1	t	186
8768	Qushchi MFY	1	t	186
8769	Shoyimbek MFY	1	t	186
8770	Sho`r MFY	1	t	186
8771	Shunqor MFY	1	t	186
8772	Shunqor QFY	1	t	186
8773	Tomosha MFY	1	t	186
8774	Tomosha QFY	1	t	186
8775	Xayit MFY	1	t	186
8776	Yangi MFY	1	t	186
8777	Ashxabod MFY	1	t	187
8778	Bejganik MFY	1	t	187
8779	Besharik MFY	1	t	187
8780	Beshariq QFY	1	t	187
8781	Bog`ot SHFY	1	t	187
8782	Boyqozoq MFY	1	t	187
8783	Bo`ka MFY	1	t	187
8784	Bo`kaylar MFY	1	t	187
8785	Bo`saloq MFY	1	t	187
8786	Dexkonbozor QFY	1	t	187
8787	Dexkonobod MFY	1	t	187
8788	Esamat MFY	1	t	187
8789	Eshonlar MFY	1	t	187
8790	G`alaba MFY	1	t	187
8791	Guduklar MFY	1	t	187
8792	Hurriyat MFY	1	t	187
8793	Katta qo`madoq MFY	1	t	187
8794	Ko`na birlashuv MFY	1	t	187
8795	Mehnat gul MFY	1	t	187
8796	Mesit buyi MFY	1	t	187
8797	Mesit MFY	1	t	187
8798	Madaniyat MFY	1	t	187
8799	Madaniyat QFY	1	t	187
8800	Mayda millat MFY	1	t	187
8801	Miroblar MFY	1	t	187
8802	Nafas bobo MFY	1	t	187
8803	Nayman bo`yi MFY	1	t	187
8804	Nayman QFY	1	t	187
8805	Nukus MFY	1	t	187
8806	Nurafshon MFY	1	t	187
8807	Obod MFY	1	t	187
8808	Ogalar MFY	1	t	187
8809	Olchin solma MFY	1	t	187
8810	Oq oltin MFY	1	t	187
8811	Oq tepa MFY	1	t	187
8812	Osyop MFY	1	t	187
8813	O`g`uzrabot QFY	1	t	187
8814	O`rta badoq MFY	1	t	187
8815	O`zbekiston MFY	1	t	187
8816	O`zgarish MFY	1	t	187
8817	Qashqalar MFY	1	t	187
8818	Qipchoq MFY	1	t	187
8819	Qipchoq QFY	1	t	187
8820	Qipchoqlar MFY	1	t	187
8821	Qirmalar MFY	1	t	187
8822	Qorabog` MFY	1	t	187
8823	Qorayontok QFY	1	t	187
8824	Qo`ldov MFY	1	t	187
8825	Qo`ngirot MFY	1	t	187
8826	Qulonkorabog QFY	1	t	187
8827	Qushlilar MFY	1	t	187
8828	Saydalijon MFY	1	t	187
8829	Tozabozor MFY	1	t	187
8830	Ustalar MFY	1	t	187
8831	Ustalar MFY	1	t	187
8832	Uzgarish MFY	1	t	187
8833	Xitoy QFY	1	t	187
8834	Xujalik QFY	1	t	187
8835	Yangi kadam MFY	1	t	187
8836	Yosh usmir MFY	1	t	187
8837	Yumaloq to`qay MFY	1	t	187
8838	Zarbdor MFY	1	t	187
8839	"Besh uy" MFY	1	t	188
8840	"Baldokli" MFY	1	t	188
8841	"Birlashgan "maxalla	1	t	188
8842	"Buzkal`a" MFY	1	t	188
8843	"Chakkalar" MFY	1	t	188
8844	"Chinobod" MFY	1	t	188
8845	"Dehqon" MFY	1	t	188
8846	"Dehqonobod"MFY	1	t	188
8847	"Dusimbiy" qishlog`i	1	t	188
8848	"Dusimbiy"MFY	1	t	188
8849	"Do`stlik " MFY	1	t	188
8850	"Do`stlik" MFY	1	t	188
8851	"Do`stlik" bogi MFY	1	t	188
8852	"Do`stlik" MFY	1	t	188
8853	"Esabiy" MFY	1	t	188
8854	"Eshimjiron" MFY	1	t	188
8855	"Jaloir" MFY	1	t	188
8856	"Kangli" MFY	1	t	188
8857	"Kangli" MFY	1	t	188
8858	"Katarik" MFY	1	t	188
8859	"Mevazor" MFY	1	t	188
8860	"Marbugat" MFY	1	t	188
8861	"Moyli" MFY	1	t	188
8862	"Navbir yop" MFY	1	t	188
8863	"Navruz" MFY	1	t	188
8864	"Nukus " MFY	1	t	188
8865	"Nurafshon" MFY	1	t	188
8866	"Obod" MFY	1	t	188
8867	"Okkum" MFY	1	t	188
8868	"Olchin" MFY	1	t	188
8869	"Paxtachi" MFY	1	t	188
8870	"Saxtiyon" MFY	1	t	188
8871	"Shangi" MFY	1	t	188
8872	"Shangi" MFY	1	t	188
8873	"Sovunchi"MFY	1	t	188
8874	"Taxtakupir" MFY	1	t	188
8875	"Toza yorgan" maxalla	1	t	188
8876	"Uyilma" MFY	1	t	188
8877	"Yormish"MFY	1	t	188
8878	1-maxalla	1	t	188
8879	10-maxalla	1	t	188
8880	11-maxalla	1	t	188
8881	12-maxalla	1	t	188
8882	2-maxalla	1	t	188
8883	3-maxalla	1	t	188
8884	4-maxalla	1	t	188
8885	5-maxalla	1	t	188
8886	6- maxalla	1	t	188
8887	7-maxalla	1	t	188
8888	8- maxalla	1	t	188
8889	9- maxalla	1	t	188
8890	Birlashgan qishlog`i	1	t	188
8891	Eshimjiron qishlog`i	1	t	188
8892	Guliston qishlog`i	1	t	188
8893	Gurlan shaxarchasi fy	1	t	188
8894	Olga qishlog`i	1	t	188
8895	Saxtiyon qishlog`i	1	t	188
8896	Sholikor qishlog`i	1	t	188
8897	Vazir qishlog`i	1	t	188
8898	Xizir-eli qishlog`i	1	t	188
8899	1-mahalla FY	1	t	189
8900	1-mahalla FY	1	t	189
8901	1-mahalla FY	1	t	189
8902	1-mahalla Fy	1	t	189
8903	2-mahalla FY	1	t	189
8904	2-mahalla FY	1	t	189
8905	2-mahalla FY	1	t	189
8906	2-mahalla FY	1	t	189
8907	3-mahalla FY	1	t	189
8908	3-mahalla FY	1	t	189
8909	3-mahalla FY	1	t	189
8910	4-mahalla FY	1	t	189
8911	4-mahalla FY	1	t	189
8912	4-mahalla FY	1	t	189
8913	5-mahalla FY	1	t	189
8914	5-mahalla FY	1	t	189
8915	5-mahalla FY	1	t	189
8916	6-mahalla FY	1	t	189
8917	6-mahalla FY	1	t	189
8918	Amirqum MFY	1	t	189
8919	Arablar MFY	1	t	189
8920	Ayronko`l MFY	1	t	189
8921	Baratlar MFY	1	t	189
8922	Bo`rloq MFY	1	t	189
8923	Changli 1 MFY	1	t	189
8924	Changli 2 MFY	1	t	189
8925	Chiqirchi MFY	1	t	189
8926	Dovud MFY	1	t	189
8927	Elobod MFY	1	t	189
8928	G`ozovot QFY	1	t	189
8929	Ilgaldi MFY	1	t	189
8930	Ittifoq MFY	1	t	189
8931	Kenagas MFY	1	t	189
8932	Kenagas QFY	1	t	189
8933	Ko`nazay MFY	1	t	189
8934	Mehnatobod MFY	1	t	189
8935	Mast MFY	1	t	189
8936	Nezaxos MFY	1	t	189
8937	Oqdarband QFY	1	t	189
8938	Oshoq qa.la MFY	1	t	189
8939	O`rta QFY	1	t	189
8940	O`rtayop QFY	1	t	189
8941	O`zbekiston MFY	1	t	189
8942	O`zbekyop QFY	1	t	189
8943	Polvon MFY	1	t	189
8944	Qaravulqkala MFY	1	t	189
8945	Qoramon MFY	1	t	189
8946	Qoromon qal`a MFY	1	t	189
8947	Qorovul MFY	1	t	189
8948	Qotog`on QFY	1	t	189
8949	Qo`shko`pir SHFY	1	t	189
8950	Sherobod MFY	1	t	189
8951	Shix QFY	1	t	189
8952	Shixmashhad MFY	1	t	189
8953	Shixmashxad SHFY	1	t	189
8954	Shixobod FY	1	t	189
8955	Tagalak MFY	1	t	189
8956	Taqir davuq MFY	1	t	189
8957	Vaximchi MFY	1	t	189
8958	Xadra QFY	1	t	189
8959	Xayrabod MFY	1	t	189
8960	Xayrobod QFY	1	t	189
8961	Xonbod QFY	1	t	189
8962	Xosiyon MFY	1	t	189
8963	Xosiyon QFY	1	t	189
8964	Yangilik MFY,	1	t	189
8965	Yangilik MFY	1	t	189
8966	Yangilik QFY	1	t	189
8967	Yovg`ir MFY	1	t	189
8968	Zarbdor MFY	1	t	189
8969	A`azizova MFY	1	t	190
8970	Ak-Ariklar MFY	1	t	190
8971	Altinsarin MFY	1	t	190
8972	Amangaldi MFY	1	t	190
8973	Amudaryo MFY	1	t	190
8974	Anjirchilar MFY	1	t	190
8975	Arablar MFY	1	t	190
8976	Arbrblar MFY	1	t	190
8977	Bekobod QFY	1	t	190
8978	Beruniy MFY	1	t	190
8979	Baxshilar MFY	1	t	190
8980	Bogdorchi MFY	1	t	190
8981	Bokaylar MFY	1	t	190
8982	Chakka-kuli MFY	1	t	190
8983	Chakkasholikor QFY	1	t	190
8984	Chala ovul MFY	1	t	190
8985	Chandir MFY	1	t	190
8986	ChandirQiyot QFY	1	t	190
8987	Chandiryopbuyi MFY	1	t	190
8988	Chatkupir QFY	1	t	190
8989	Cholish QFY	1	t	190
8990	Chulobod MFY	1	t	190
8991	Dargalar MFY	1	t	190
8992	Dumbaylar MFY	1	t	190
8993	Do`stlik MFY	1	t	190
8994	Do`stlik MFY	1	t	190
8995	Do`stlik MFY	1	t	190
8996	E.Raxim MFY	1	t	190
8997	G`alaba QFY	1	t	190
8998	G`alaba MFY	1	t	190
8999	G`aybu QFY	1	t	190
9000	Gardonlar MFY	1	t	190
9001	Jambul MFY	1	t	190
9002	K.Otaniyazov MFY	1	t	190
9003	Kanal buyi MFY	1	t	190
9004	Karavul QFY	1	t	190
9005	Kattabog MFY	1	t	190
9006	Kaychili MFY	1	t	190
9007	Kazak ovul MFY	1	t	190
9008	Killavut MFY	1	t	190
9009	Qipchoq MFY	1	t	190
9010	Qiyot MFY	1	t	190
9011	Koramon QFY	1	t	190
9012	Koramon MFY	1	t	190
9013	Korayontok MFY	1	t	190
9014	Kozikoraboy MFY	1	t	190
9015	Koziovul MFY	1	t	190
9016	Kumravot MFY	1	t	190
9017	Kuna ovul MFY	1	t	190
9018	Kungirot MFY	1	t	190
9019	Kupaklar MFY	1	t	190
9020	Kushchilar MFY	1	t	190
9021	M.Xorazmiy MFY	1	t	190
9022	Mergan ovul MFY	1	t	190
9023	Mevazor MFY	1	t	190
9024	Matnazar Oxun MFY	1	t	190
9025	Mirboblar MFY	1	t	190
9026	Navoiy MFY	1	t	190
9027	Navruz MFY	1	t	190
9028	Obod MFY	1	t	190
9029	Ok matkab MFY	1	t	190
9030	Oq oltin MFY	1	t	190
9031	Ok-yop MFY	1	t	190
9032	Ola uylik MFY	1	t	190
9033	Oltinkul MFY	1	t	190
9034	Oyok bog MFY	1	t	190
9035	Qo`shbog` MFY	1	t	190
9036	Rovot MFY	1	t	190
9037	Sevanlar MFY	1	t	190
9038	Sarichilar MFY	1	t	190
9039	Sartavul MFY	1	t	190
9040	Shermatlar MFY	1	t	190
9041	Sholikor MFY	1	t	190
9042	Shoxidonlar MFY	1	t	190
9043	Tandirchi MFY	1	t	190
9044	Toshkupir MFY	1	t	190
9045	Turkmanlar MFY	1	t	190
9046	Urislar MFY	1	t	190
9047	Urtabog MFY	1	t	190
9048	Urtabog MFY	1	t	190
9049	Urtayop MFY	1	t	190
9050	Ustalar MFY	1	t	190
9051	Uygur MFY	1	t	190
9052	Uyshin MFY	1	t	190
9053	X.Olimjon MFY	1	t	190
9054	Xasaul MFY	1	t	190
9055	Xayvat MFY	1	t	190
9056	Xojiboylar MFY	1	t	190
9057	Yarmish yop MFY	1	t	190
9058	Yoshlik MFY	1	t	190
9059	Yukoribog QFY	1	t	190
9060	Yukoridurman QFY	1	t	190
9061	Yukorijirmiz MFY	1	t	190
9062	Yukoriovul MFY	1	t	190
9063	Zargarlar MFY	1	t	190
9064	33-maxalla MFY	1	t	191
9065	A.Do`schanov MFY	1	t	191
9066	Al-Xorazmiy MFY	1	t	191
9067	Ashxobod MFY	1	t	191
9068	Besh-mergan MFY	1	t	191
9069	Baynalmichi MFY	1	t	191
9070	Binokor MFY	1	t	191
9071	Bobur MFY	1	t	191
9072	Bo`ston MFY	1	t	191
9073	Do`stlik MFY	1	t	191
9074	E.Raxim MFY	1	t	191
9075	Feruz MFY	1	t	191
9076	Gulchilar MFY	1	t	191
9077	Gulshan MFY	1	t	191
9078	Gulzor MFY	1	t	191
9079	Istiqlol MFY	1	t	191
9080	Jambul MFY	1	t	191
9081	Jingovuz MFY	1	t	191
9082	K. Ataniyozov MFY	1	t	191
9083	Ko`hna-qal`a MFY	1	t	191
9084	Ma.rifat MFY	1	t	191
9085	Mash`al MFY	1	t	191
9086	Mustaqillik MFY	1	t	191
9087	Navbahor MFY	1	t	191
9088	Navro`z MFY	1	t	191
9089	Obi-hayot MFY	1	t	191
9090	Olimpiya MFY	1	t	191
9091	Sahovat MFY	1	t	191
9092	Shodlik MFY	1	t	191
9093	Temir-yo`lchi MFY	1	t	191
9094	Toza-Bog` MFY	1	t	191
9095	Umid MFY	1	t	191
9096	Yangi-hayot MFY	1	t	191
9097	Yangi-obod MFY	1	t	191
9098	Yuqori-bog` MFY	1	t	191
9099	Al Xorazmiy MFY	1	t	192
9100	Angarik MFY	1	t	192
9101	Arvik MFY	1	t	192
9102	Avaz dunak MFY	1	t	192
9103	Binokor MFY	1	t	192
9104	Buston MFY	1	t	192
9105	Chanashik MFY	1	t	192
9106	Chinobod QFY	1	t	192
9107	Chinobod MFY	1	t	192
9108	Doshyok QFY	1	t	192
9109	Doshyok MFY	1	t	192
9110	Do`stlik MFY	1	t	192
9111	Eski kiyat QFY	1	t	192
9112	Gandimyon QFY	1	t	192
9113	Gandimyon MFY	1	t	192
9114	Gazchi MFY	1	t	192
9115	Gilamchi MFY	1	t	192
9116	Gulirayxon MFY	1	t	192
9117	Guliston MFY	1	t	192
9118	Gulshan MFY	1	t	192
9119	Ichan kal?a MFY	1	t	192
9120	Indavak MFY	1	t	192
9121	Irdimzon QFY	1	t	192
9122	Istiqlol MFY	1	t	192
9123	Juryon QFY	1	t	192
9124	Kalta minor MFY	1	t	192
9125	Kaptarxona MFY	1	t	192
9126	Karadamak MFY	1	t	192
9127	Karakum MFY	1	t	192
9128	Kattibosh MFY	1	t	192
9129	Kibla Tozabog MFY	1	t	192
9130	Qiyot MFY	1	t	192
9131	Kulli MFY	1	t	192
9132	Kumyaska MFY	1	t	192
9133	Kushchi kattabog MFY	1	t	192
9134	Lolazor MFY	1	t	192
9135	Mevaston MFY	1	t	192
9136	Ok kul MFY	1	t	192
9137	Okyop QFY	1	t	192
9138	Okyop MFY	1	t	192
9139	Pano Maksim MFY	1	t	192
9140	Parchanxos MFY	1	t	192
9141	Pirnaxos MFY	1	t	192
9142	Pishkanik MFY	1	t	192
9143	Polosulton MFY	1	t	192
9144	Serchali MFY	1	t	192
9145	Sangar MFY	1	t	192
9146	Shixlar MFY	1	t	192
9147	Shomoxulum MFY	1	t	192
9148	Shomoxulum qfy	1	t	192
9149	Shurkul MFY	1	t	192
9150	Soyot QFY	1	t	192
9151	Soyot MFY	1	t	192
9152	Tozabog MFY	1	t	192
9153	Urta Xorvuz MFY	1	t	192
9154	Varagzon MFY	1	t	192
9155	Xorvuz MFY	1	t	192
9156	Yangi turmush MFY	1	t	192
9157	Yangi xayot MFY	1	t	192
9158	Yukori xorvuz MFY	1	t	192
9159	A.Ibragimov. MFY	1	t	193
9160	Beshta. MFY	1	t	193
9161	Bogdor. MFY	1	t	193
9162	G.Gulom. MFY	1	t	193
9163	Ishchilar. MFY	1	t	193
9164	Istiqlol MFY	1	t	193
9165	Jangiota MFY	1	t	193
9166	Juvondur MFY	1	t	193
9167	Kovunchi MFY	1	t	193
9168	Mustakillik	1	t	193
9169	Muxabbat MFY	1	t	193
9170	Navbaxor MFY	1	t	193
9171	Navro`z MFY	1	t	193
9172	Obod MFY	1	t	193
9173	Otalik MFY	1	t	193
9174	Oxunboboev MFY	1	t	193
9175	Oybek MFY	1	t	193
9176	Pastom MFY	1	t	193
9177	Saidlar MFY	1	t	193
9178	Sayapir MFY	1	t	193
9179	Sh.Rashidov MFY	1	t	193
9180	Shexlar MFY	1	t	193
9181	Sharlauk MFY	1	t	193
9182	Shovot MFY	1	t	193
9183	Sulaymon kaloa MFY	1	t	193
9184	Turta MFY	1	t	193
9185	Xazorasp MFY	1	t	193
9186	Yangiobod MFY	1	t	193
9187	Yoshlik MFY	1	t	193
9188	12-Narvon MFY	1	t	193
9189	Al .Xorazmiy MFY	1	t	193
9190	Alokali ko`l	1	t	193
9191	Amudaryo MFY	1	t	193
9192	B.Matirzaev MFY	1	t	193
9193	Beshta qishlog`i	1	t	193
9194	Bo`ston kishlog`i	1	t	193
9195	Buston MFY	1	t	193
9196	Karvak MFY	1	t	193
9197	Karvak qishlog`i	1	t	193
9198	Muxomon MFY	1	t	193
9199	Muxomon qishlog`i	1	t	193
9200	Ovshar kishlog`i	1	t	193
9201	Ovshar MFY	1	t	193
9202	Pichokchi MFY	1	t	193
9203	Pichoqchi qishlog`i	1	t	193
9204	Pitnak QFY	1	t	193
9205	Sanoat MFY	1	t	193
9206	Sanoat qishlog`i MFY	1	t	193
9207	Sarimoy QFY	1	t	193
9208	Shexyopi Mutpiri	1	t	193
9209	Tuproqqal`a QFY	1	t	193
9210	Uzukka qosh	1	t	193
9211	Xazorasp ShchaFY	1	t	193
9212	Yangi xayot MFY	1	t	193
9213	Yangibozor MFY	1	t	193
9214	Yangibozor qishlog`i	1	t	193
9215	1-MFY	1	t	194
9216	2-MFY	1	t	194
9217	3-MFY	1	t	194
9218	4-MFY	1	t	194
9219	5-MFY	1	t	194
9220	6-MFY	1	t	194
9221	7-MFY	1	t	194
9222	8-MFY	1	t	194
9223	9-MFY	1	t	194
9224	10-MFY	1	t	194
9225	11-MFY	1	t	194
9226	12-MFY	1	t	194
9227	13-MFY	1	t	194
9228	14-MFY	1	t	194
9229	15-MFY	1	t	194
9230	Amudaryo QFY	1	t	194
9231	Do`stlik MFY	1	t	194
9232	Durgadik MFY	1	t	194
9233	Durmon MFY	1	t	194
9234	G`ayrat MFY	1	t	194
9235	Guliston MFY	1	t	194
9236	Ilg`or MFY	1	t	194
9237	Istiqlol MFY	1	t	194
9238	Katta jirmiz QFY	1	t	194
9239	Katta kuch MFY	1	t	194
9240	Ko`pchilik MFY	1	t	194
9241	Mada er MFY	1	t	194
9242	Madaniyat MFY	1	t	194
9243	Madir QFY	1	t	194
9244	Mustaqillik MFY	1	t	194
9245	Namuna QFY	1	t	194
9246	Navro`z MFY	1	t	194
9247	Navxos QFY	1	t	194
9248	Nuravshon MFY	1	t	194
9249	Nurobod MFY	1	t	194
9250	Obod MFY	1	t	194
9251	Olaja QFY	1	t	194
9252	Olchin MFY	1	t	194
9253	Paxtagul MFY	1	t	194
9254	Paxtakor MFY	1	t	194
9255	Qirqyop QFY	1	t	194
9256	Qoramozi MFY	1	t	194
9257	Qoraqosh QFY	1	t	194
9258	Sarapoyon QFY	1	t	194
9259	Shirin MFY	1	t	194
9260	Shodlik MFY	1	t	194
9261	Toma MFY	1	t	194
9262	Tomadurgadik QFY	1	t	194
9263	Turkiston MFY	1	t	194
9264	Xonqa ShchaFY	1	t	194
9265	Yangi turmush MFY	1	t	194
9266	Yosh kuch MFY	1	t	194
9267	Znaxos MFY	1	t	194
9268	Arbek MFY	1	t	195
9269	Arbob MFY	1	t	195
9270	Asavey MFY	1	t	195
9271	Beshchiqir MFY	1	t	195
9272	Beshmargan MFY	1	t	195
9273	Beshmargan QFY	1	t	195
9274	Botirlar MFY	1	t	195
9275	Bo`ston MFY	1	t	195
9276	Bo`yrachi QFY	1	t	195
9277	Bo`yrachi MFY	1	t	195
9278	Bo`zqal`a MFY	1	t	195
9279	Bo`zqal`a MFY	1	t	195
9280	Chig`atoy MFY	1	t	195
9281	Chig`atoyqal`a MFY	1	t	195
9282	Chig`atoyqal`a QFY	1	t	195
9283	Cho`qli QFY	1	t	195
9284	Do`stlik MFY	1	t	195
9285	Do`stlik MFY	1	t	195
9286	Eshonqal`a MFY	1	t	195
9287	Guliston MFY	1	t	195
9288	Guliston MFY	1	t	195
9289	Idaliqal`a MFY	1	t	195
9290	Ijtimoiyat MFY	1	t	195
9291	Ijtimoiyat QFY	1	t	195
9292	Ipakchi MFY	1	t	195
9293	K.Raximov MFY	1	t	195
9294	Kangli QFY	1	t	195
9295	Kangli MFY	1	t	195
9296	Katqal`a MFY	1	t	195
9297	Komiljon ota MFY	1	t	195
9298	Madaniyat MFY	1	t	195
9299	Madaniyat MFY	1	t	195
9300	Monoq MFY	1	t	195
9301	Navro`z MFY	1	t	195
9302	Navro`z MFY	1	t	195
9303	Navro`z MFY	1	t	195
9304	Ogahiy MFY	1	t	195
9305	Oltinqal`a MFY	1	t	195
9306	Oq ko`l MFY	1	t	195
9307	Oq ko`l MFY	1	t	195
9308	Oq oltin MFY	1	t	195
9309	Ostona MFY	1	t	195
9310	Oxunboboev MFY	1	t	195
9311	Oydin MFY	1	t	195
9312	O`zbekiston QFY	1	t	195
9313	Paxtakor MFY	1	t	195
9314	Po`lat MFY	1	t	195
9315	Qiyot QFY	1	t	195
9316	Qiyot MFY	1	t	195
9317	Qozoqqal`a MFY	1	t	195
9318	Qo`shko`pir MFY	1	t	195
9319	Qum yop MFY	1	t	195
9320	Qunduz MFY	1	t	195
9321	Royat MFY	1	t	195
9322	Shovot MFY	1	t	195
9323	Shovot ShchaFY	1	t	195
9324	Shovotqal`a QFY	1	t	195
9325	To`qmang`it MFY	1	t	195
9326	To`qmang`it MFY	1	t	195
9327	Turkiston MFY	1	t	195
9328	Uzunko`l MFY	1	t	195
9329	Xitoy QFY	1	t	195
9330	Xitoy MFY	1	t	195
9331	Xunarmand MFY	1	t	195
9332	Yangi turmush MFY	1	t	195
9333	Yangi yo`l MFY	1	t	195
9334	Yangiobod MFY	1	t	195
9335	Achchiqquyi MFY	1	t	196
9336	Angiariq MFY	1	t	196
9337	Arboblar MFY	1	t	196
9338	Beshayvon MFY	1	t	196
9339	Boliqchi MFY	1	t	196
9340	Boromiq MFY	1	t	196
9341	Boyot MFY	1	t	196
9342	Bo`ston MFY	1	t	196
9343	Chakir MFY	1	t	196
9344	Chiqirchi MFY	1	t	196
9345	Chiqirchi QFY	1	t	196
9346	Do`stlik MFY	1	t	196
9347	Egrisolma MFY	1	t	196
9348	G`altak MFY	1	t	196
9349	Gulabod QFY	1	t	196
9350	Gullanbog` MFY	1	t	196
9351	Gullanbog` QFY	1	t	196
9352	Istiqlol MFY	1	t	196
9353	Jaloil MFY	1	t	196
9354	Kattabog` MFY	1	t	196
9355	Kattabog` QFY	1	t	196
9356	Killovit MFY	1	t	196
9357	Kushanda MFY	1	t	196
9358	Ogoxiy MFY	1	t	196
9359	Oq-machit MFY	1	t	196
9360	Ostona MFY	1	t	196
9361	Ostona QFY	1	t	196
9362	O`zbekiston MFY	1	t	196
9363	Po`rsang MFY	1	t	196
9364	Qarmish MFY	1	t	196
9365	Qarmish QFY	1	t	196
9366	Qorako`z MFY	1	t	196
9367	Qozoqli MFY	1	t	196
9368	Qo`ng`irot MFY	1	t	196
9369	Qo`riqtom MFY	1	t	196
9370	Qo`riqtom QFY	1	t	196
9371	Qo`shloq MFY	1	t	196
9372	Sevgan MFY	1	t	196
9373	Sardorlar MFY	1	t	196
9374	Sherobod MFY	1	t	196
9375	Shirsholi MFY	1	t	196
9376	Shixbog`i MFY	1	t	196
9377	Soburzon MFY	1	t	196
9378	Tagan MFY	1	t	196
9379	Tagan QFY	1	t	196
9380	Tuzloq MFY	1	t	196
9381	Ulug`bek MFY	1	t	196
9382	Urganch MFY	1	t	196
9383	Uyg`ur MFY	1	t	196
9384	Vakillar MFY	1	t	196
9385	Xo`jalar MFY	1	t	196
9386	Yangier MFY	1	t	196
9387	Yangiariq MFY	1	t	196
9388	Yangiariq SHFY	1	t	196
9389	Yangiobod MFY	1	t	196
9390	Bogolon MFY	1	t	197
9391	Bo`ston MFY	1	t	197
9392	Bo`zkal`a 1 MFY	1	t	197
9393	Bo`zkal`a 2 MFY	1	t	197
9394	Bo`zkal`a 3 MFY	1	t	197
9395	Chubolonchi MFY	1	t	197
9396	Do`stlik MFY	1	t	197
9397	Guliston MFY	1	t	197
9398	Jayxun MFY	1	t	197
9399	Katli MFY	1	t	197
9400	Qiyot MFY	1	t	197
9401	Qora tepa MFY	1	t	197
9402	Mangitlar MFY	1	t	197
9403	Ming Bog`olon MFY	1	t	197
9404	Navr yor MFY	1	t	197
9405	Navruz MFY	1	t	197
9406	Ocha kala MFY	1	t	197
9407	Oltinkul MFY	1	t	197
9408	Shirinlar MFY	1	t	197
9409	Shixlar MFY	1	t	197
9410	Shoirlar MFY	1	t	197
9411	Tozadurman MFY	1	t	197
9412	X.Olimjon MFY	1	t	197
9413	Xalqobod MFY	1	t	197
9414	Xayvat MFY	1	t	197
9415	Yangi yor MFY	1	t	197
9416	Yukori Boshkir MFY	1	t	197
9417	Bog`olon QFY	1	t	197
9418	Boshkirshix QFY	1	t	197
9419	Buzkal`a QFY	1	t	197
9420	Chubolonchi QFY	1	t	197
9421	Kalandardurman QFY	1	t	197
9422	Kargalar MFY	1	t	197
9423	Oyokdurman QFY	1	t	197
9424	Shirinkungirot QFY	1	t	197
9425	Uyg`ur QFY	1	t	197
9426	Yangibozor SHFY	1	t	197
9427	Abay MFY	1	t	198
9428	Bektemir MFY	1	t	198
9429	Binokor MFY	1	t	198
9430	Chashma MFY	1	t	198
9431	Istiqbol MFY	1	t	198
9432	Maxjnuntol MFY	1	t	198
9433	Mirishkor MFY	1	t	198
9434	Nurafshon MFY	1	t	198
9435	o`Ashurov MFY	1	t	198
9436	Roxat MFY	1	t	198
9437	X.Bayqaro MFY	1	t	198
9438	Zilola MFY	1	t	198
9439	A.Yugnakiy MFY	1	t	199
9440	Al-Farobiy MFY	1	t	199
9441	Alisher Navoiy MFY	1	t	199
9442	Alpomish MFY	1	t	199
9443	Avayxon MFY	1	t	199
9444	Axillik MFY	1	t	199
9445	Axmad Yassaviy MFY	1	t	199
9446	Azamat MFY	1	t	199
9447	Beshkapa MFY	1	t	199
9448	Baxor MFY	1	t	199
9449	Bobur MFY	1	t	199
9450	Bo`z-2 MFY	1	t	199
9451	Darxon MFY	1	t	199
9452	Feruza MFY	1	t	199
9453	Fayzulla Xo`jaev MFY	1	t	199
9454	Guliston MFY	1	t	199
9455	Gulzor MFY	1	t	199
9456	Katta Oltintepa MFY	1	t	199
9457	Katta Qorasuv MFY	1	t	199
9458	Katta Yalang`ochota MFY	1	t	199
9459	Lashkarbegi MFY	1	t	199
9460	M.Ismoiliy MFY	1	t	199
9461	Munavvarqori MFY	1	t	199
9462	Navruz MFY	1	t	199
9463	Nodirabegim MFY	1	t	199
9464	Nur MFY	1	t	199
9465	Olimlar MFY	1	t	199
9466	Olmachi MFY	1	t	199
9467	Oltintepa-10 MFY	1	t	199
9468	Oqibat MFY	1	t	199
9469	Oqqo`rg`on MFY	1	t	199
9470	Salar MFY	1	t	199
9471	Sayram MFY	1	t	199
9472	Shalola MFY	1	t	199
9473	Shaxriobod MFY	1	t	199
9474	Shaxrisabz MFY	1	t	199
9475	Sho`rtepa MFY	1	t	199
9476	Shukur Burxonov MFY	1	t	199
9477	Traktorsozlar MFY	1	t	199
9478	Turon MFY	1	t	199
9479	Ulug`bek MFY	1	t	199
9480	Umid MFY	1	t	199
9481	Uyg`onish MFY	1	t	199
9482	X`abdullaev MFY	1	t	199
9483	Xamid Olimjon MFY	1	t	199
9484	Xorazm MFY	1	t	199
9485	Xumoyun MFY	1	t	199
9486	Yalong`och MFY	1	t	199
9487	Yalong`och-ota MFY	1	t	199
9488	Yangi Avayxon MFY	1	t	199
9489	Yangi xayot MFY	1	t	199
9490	Yuzrabod MFY	1	t	199
9491	A`avloniy MFY	1	t	200
9492	A.Fitrat MFY	1	t	200
9493	Afrosiyob MFY	1	t	200
9494	At-Termiziy MFY	1	t	200
9495	Baratxuja MFY	1	t	200
9496	Baxor MFY	1	t	200
9497	Baynalminal MFY	1	t	200
9498	Bilimdon MFY	1	t	200
9499	Birodarlik MFY	1	t	200
9500	Bogishamol MFY	1	t	200
9501	Chinor MFY	1	t	200
9502	Do`stlik MFY	1	t	200
9503	Fayziobod	1	t	200
9504	Furkat MFY	1	t	200
9505	Istiqlol MFY	1	t	200
9506	Korasuv MFY	1	t	200
9507	Kuylik-ota MFY	1	t	200
9508	Matonat MFY	1	t	200
9509	Mingurik MFY	1	t	200
9510	Mirobod MFY	1	t	200
9511	Movarounnaxr MFY	1	t	200
9512	Mustakillik MFY	1	t	200
9513	Navbaxor MFY	1	t	200
9514	Navruz MFY	1	t	200
9515	Ok uy MFY	1	t	200
9516	Olmazor MFY	1	t	200
9517	Oltinkul MFY	1	t	200
9518	Oybek MFY	1	t	200
9519	Parvona MFY	1	t	200
9520	Salar MFY	1	t	200
9521	Sarikul MFY	1	t	200
9522	Sh.Rashidov MFY	1	t	200
9523	Shark Yulduzi MFY	1	t	200
9524	Temiryulchilar MFY	1	t	200
9525	Tolarik MFY	1	t	200
9526	Uzbekiston MFY	1	t	200
9527	Yangi Kuylik MFY	1	t	200
9528	Yangi Mirobod MFY	1	t	200
9529	Yangi Zamon MFY	1	t	200
9530	A.Navoiy MFY	1	t	201
9531	Achaobod MFY	1	t	201
9532	Allon MFY	1	t	201
9533	Axil MFY	1	t	201
9534	Axmad Yassaviy MFY	1	t	201
9535	Beruniy Maydoni MFY	1	t	201
9536	Beruniy MFY	1	t	201
9537	Beshqo`rg`on MFY	1	t	201
9538	Bo`ston MFY	1	t	201
9539	Chig`atoy Darboza MFY	1	t	201
9540	Chig`atoy Oqtepa MFY	1	t	201
9541	Chilto`g`on MFY	1	t	201
9542	Chimboy MFY	1	t	201
9543	Chuqursoy MFY	1	t	201
9544	Chustiy MFY	1	t	201
9545	Do`stlik MFY	1	t	201
9546	Eski shahar MFY	1	t	201
9547	G`alaba MFY	1	t	201
9548	G`ani A.zamov MFY	1	t	201
9549	Gulzor MFY	1	t	201
9550	Guruchariq MFY	1	t	201
9551	Guzarboshi MFY	1	t	201
9552	Ibroxim ota MFY	1	t	201
9553	Islom ota MFY	1	t	201
9554	Ismoil Shoshiy MFY	1	t	201
9555	Istiqbol MFY	1	t	201
9556	Istiqlol MFY	1	t	201
9557	Jiydali MFY	1	t	201
9558	K.G`ofurov MFY	1	t	201
9559	Mirza G`olib MFY	1	t	201
9560	Miskin MFY	1	t	201
9561	Moyarik MFY	1	t	201
9562	Mustaqillik MFY	1	t	201
9563	Namuna MFY	1	t	201
9564	Navbaxor MFY	1	t	201
9565	Nixol MFY	1	t	201
9566	Obod MFY	1	t	201
9567	Olimpiya MFY	1	t	201
9568	Paxta MFY	1	t	201
9569	Qichqiriq MFY	1	t	201
9570	Qorasaroy MFY	1	t	201
9571	Qushtut MFY	1	t	201
9572	S?bzor MFY	1	t	201
9573	Shifokorlar MFY	1	t	201
9574	Shodlik MFY	1	t	201
9575	Shuxrat MFY	1	t	201
9576	Tabassum MFY	1	t	201
9577	Taraqqiyot MFY	1	t	201
9578	Taxtapul MFY	1	t	201
9579	Umid MFY	1	t	201
9580	Universitet MFY	1	t	201
9581	Xastimom MFY	1	t	201
9582	Xislat MFY	1	t	201
9583	Xofiz Kuxakiy MFY	1	t	201
9584	Xonchorbog` MFY	1	t	201
9585	Yangi Sebzor MFY	1	t	201
9586	Yoshlik MFY	1	t	201
9587	Ziyo MFY	1	t	201
9588	A.Jomiy MFY	1	t	202
9589	A.Navoiy MFY	1	t	202
9590	A.Temur MFY	1	t	202
9591	Al-Farg`oniy MFY	1	t	202
9592	Bahor MFY	1	t	202
9593	Bobur MFY	1	t	202
9594	Chosh-tepa MFY	1	t	202
9595	Do`stlik MFY	1	t	202
9596	Guliston MFY	1	t	202
9597	Ittifoq MFY	1	t	202
9598	Kum-arik MFY	1	t	202
9599	Kush-kurgon MFY	1	t	202
9600	Madaniyat MFY	1	t	202
9601	Mustaqillik MFY	1	t	202
9602	Navro`z MFY	1	t	202
9603	Nilufar MFY	1	t	202
9604	Nog`ay-qo`rg`on MFY	1	t	202
9605	Obod MFY	1	t	202
9606	Oltin vodiy MFY	1	t	202
9607	Oqibat MFY	1	t	202
9608	Qipchoq MFY	1	t	202
9609	Sh.Burxonov MFY	1	t	202
9610	Temir yo`lchi MFY	1	t	202
9611	Tinchlik MFY	1	t	202
9612	Uchuvchilar MFY	1	t	202
9613	Uzgarish MFY	1	t	202
9614	Xabibiy MFY	1	t	202
9615	Xalkobod MFY	1	t	202
9616	Xonobod MFY	1	t	202
9617	Yangi hayot MFY	1	t	202
9618	Yangi Sergeli MFY	1	t	202
9619	Yorkin hayot MFY	1	t	202
9620	Yo`ldosh MFY	1	t	202
9621	A. Kodiriy MFY	1	t	203
9622	A. Soguniy MFY	1	t	203
9623	Al-Xorazmiy MFY	1	t	203
9624	Bekobod MFY	1	t	203
9625	Beshkayrogoch MFY	1	t	203
9626	Birlik MFY	1	t	203
9627	Bog`ichinor MFY	1	t	203
9628	Bogiston MFY	1	t	203
9629	Bogobod MFY	1	t	203
9630	Chamanzor MFY	1	t	203
9631	Chulpon ota MFY	1	t	203
9632	Degrez MFY	1	t	203
9633	Davlatobod MFY	1	t	203
9634	Farxod MFY	1	t	203
9635	Guzar MFY	1	t	203
9636	Ibrat MFY	1	t	203
9637	Istiroxat MFY	1	t	203
9638	Jarbuloq MFY	1	t	203
9639	Jurjoniy MFY	1	t	203
9640	Katta Ka.ni MFY	1	t	203
9641	Kori Yogdi MFY	1	t	203
9642	Koziguzar MFY	1	t	203
9643	Ko`kchaOqtepa MFY	1	t	203
9644	Ko`ksaroy MFY	1	t	203
9645	Ko`rkamobod MFY	1	t	203
9646	Ko`xnaCho`ponota MFY	1	t	203
9647	Latifguzar MFY	1	t	203
9648	Nayman MFY	1	t	203
9649	Nishabariq MFY	1	t	203
9650	Nurobod MFY	1	t	203
9651	Okmachit MFY	1	t	203
9652	Paxtakor MFY	1	t	203
9653	Qo`rg`ontepa MFY	1	t	203
9654	QuyiDarxon MFY	1	t	203
9655	Shark Guli MFY	1	t	203
9656	Shark Yulduzi MFY	1	t	203
9657	Shirin MFY	1	t	203
9658	Shofayzibogi MFY	1	t	203
9659	Shoftolizor MFY	1	t	203
9660	Taqachi MFY	1	t	203
9661	Tinchlikobod MFY	1	t	203
9662	Uchtepa MFY	1	t	203
9663	Urikzor MFY	1	t	203
9664	Utkir MFY	1	t	203
9665	Vatan MFY	1	t	203
9666	Vatanparvar MFY	1	t	203
9667	Xayratiy MFY	1	t	203
9668	Xojiobod MFY	1	t	203
9669	Xondamir MFY	1	t	203
9670	Xuroson MFY	1	t	203
9671	Xurshid MFY	1	t	203
9672	Yu.Sakkokiy MFY	1	t	203
9673	Zulfizar MFY	1	t	203
9674	Al-Buxoriy MFY	1	t	204
9675	Alisher Navoiy MFY	1	t	204
9676	Amir Temur MFY	1	t	204
9677	Asalobod MFY	1	t	204
9678	Aviasozlar MFY	1	t	204
9679	Axmad Yassaviy MFY	1	t	204
9680	Behizor MFY	1	t	204
9681	Besh bola MFY	1	t	204
9682	Bahor MFY	1	t	204
9683	Binokor MFY	1	t	204
9684	Birlashgan MFY	1	t	204
9685	Bobur MFY	1	t	204
9686	Boyqo`rg`on MFY	1	t	204
9687	Boysun MFY	1	t	204
9688	Bunyodkor MFY	1	t	204
9689	Cho`lpon MFY	1	t	204
9690	Donishmand MFY	1	t	204
9691	Do`stlik MFY	1	t	204
9692	Go`zal MFY	1	t	204
9693	Guliston MFY	1	t	204
9694	Hamza MFY	1	t	204
9695	Iltifot MFY	1	t	204
9696	Iqbol MFY	1	t	204
9697	Istiqlol MFY	1	t	204
9698	Jarqo`rg`on MFY	1	t	204
9699	Jo`rabek MFY	1	t	204
9700	Katta Yangiobod MFY	1	t	204
9701	Ma`rifat MFY	1	t	204
9702	Mashinasozlar MFY	1	t	204
9703	Maxmur MFY	1	t	204
9704	Mirzo Ulug`bek MFY	1	t	204
9705	Moxinur MFY	1	t	204
9706	Muqimiy MFY	1	t	204
9707	Mustakillik 10 yil MFY	1	t	204
9708	Mustaqillik MFY	1	t	204
9709	Muxtor Ashrafiy MFY	1	t	204
9710	Navro`z MFY	1	t	204
9711	Nodira MFY	1	t	204
9712	Olmos MFY	1	t	204
9713	Oydinko`l MFY	1	t	204
9714	O`rta Masjid MFY	1	t	204
9715	Parvoz MFY	1	t	204
9716	Qatta qo`yliq MFY	1	t	204
9717	Qo`ylik ota MFY	1	t	204
9718	Taraqqiyot MFY	1	t	204
9719	Tarnov boshi MFY	1	t	204
9720	To`y tepa MFY	1	t	204
9721	Tuzel MFY	1	t	204
9722	Umid MFY	1	t	204
9723	Usmon Nosir MFY	1	t	204
9724	Xarbiylar MFY	1	t	204
9725	Yangi Davr MFY	1	t	204
9726	Yanginur MFY	1	t	204
9727	Yangiobod MFY	1	t	204
9728	Yangiqo`rg`on MFY	1	t	204
9729	1-Charx Kamolon MFY	1	t	205
9730	1-Qatortol MFY	1	t	205
9731	2-Charx Kamolon MFY	1	t	205
9732	2-Qatortol MFY	1	t	205
9733	3-Charx Kamolon MFY	1	t	205
9734	Al-Xorazmiy MFY	1	t	205
9735	Bekto`pi MFY	1	t	205
9736	Beshqo`rg`on MFY	1	t	205
9737	Beshyog`och MFY	1	t	205
9738	Bahoriston MFY	1	t	205
9739	Bog`iston MFY	1	t	205
9740	Botirma MFY	1	t	205
9741	Bo`ri jar MFY	1	t	205
9742	Chilonzor MFY	1	t	205
9743	Cho`pon-ota MFY	1	t	205
9744	Do`mbirobod MFY	1	t	205
9745	Do`stlik MFY	1	t	205
9746	G`ofur G`ulom MFY	1	t	205
9747	Guliston MFY	1	t	205
9748	Hamza MFY	1	t	205
9749	Hayrobod MFY	1	t	205
9750	Katta Dumbiraobod MFY	1	t	205
9751	Katta Chilonzor-1 MFY	1	t	205
9752	Katta Chilonzor-2 MFY	1	t	205
9753	Katta Chilonzor-3 MFY	1	t	205
9754	Katta Qozirobod MFY	1	t	205
9755	Katta Xirmon tepa MFY	1	t	205
9756	Kichik Xirmontepa MFY	1	t	205
9757	Ko`tarma MFY	1	t	205
9758	Lutfiy MFY	1	t	205
9759	Mehrjon MFY	1	t	205
9760	Mevazor MFY	1	t	205
9761	Mavzu-8 MFY	1	t	205
9762	Naqqoshlik MFY	1	t	205
9763	Navbahor MFY	1	t	205
9764	Novza MFY	1	t	205
9765	No`g`oy-Qo`rg`on MFY	1	t	205
9766	Olmazor MFY	1	t	205
9767	Oq-tepa MFY	1	t	205
9768	Qatortol MFY	1	t	205
9769	Sharaf MFY	1	t	205
9770	Sharq MFY	1	t	205
9771	Sharq Tongi MFY	1	t	205
9772	Tinchlik MFY	1	t	205
9773	Tirsakobod MFY	1	t	205
9774	Xalqlar Do`stligi MFY	1	t	205
9775	Xirmon tepa MFY	1	t	205
9776	Yakkabog`MFY	1	t	205
9777	Yakkatut MFY	1	t	205
9778	Beltepa MFY	1	t	206
9779	Bog` ko`cha MFY	1	t	206
9780	Bo`ston MFY	1	t	206
9781	Chaqar MFY	1	t	206
9782	Chorsu MFY	1	t	206
9783	Cho`ponota MFY	1	t	206
9784	Eshonguzar MFY	1	t	206
9785	EskiJararik MFY	1	t	206
9786	Gulbozor MFY	1	t	206
9787	Gulobod MFY	1	t	206
9788	Ibn Sino MFY	1	t	206
9789	Ilg`or MFY	1	t	206
9790	Ipakchi MFY	1	t	206
9791	Islomobod MFY	1	t	206
9792	Janggox MFY	1	t	206
9793	Jarariq MFY	1	t	206
9794	Kamolon MFY	1	t	206
9795	Kattabog` MFY	1	t	206
9796	Kattaxovuz MFY	1	t	206
9797	Koxota MFY	1	t	206
9798	Ko`kcha MFY	1	t	206
9799	Labzak MFY	1	t	206
9800	M.Uyg`ur MFY	1	t	206
9801	Novza MFY	1	t	206
9802	o`Xo`jaev MFY	1	t	206
9803	Obinazir MFY	1	t	206
9804	Olmazor MFY	1	t	206
9805	Oqilon MFY	1	t	206
9806	Oqtepa MFY	1	t	206
9807	O`qchi MFY	1	t	206
9808	O`rda MFY	1	t	206
9809	O`zbekiston MFY	1	t	206
9810	Qoratosh MFY	1	t	206
9811	S.Darvoza MFY	1	t	206
9812	Sarxumdon MFY	1	t	206
9813	Saayxontoxur MFY	1	t	206
9814	Saodlik MFY	1	t	206
9815	Saofayzi MFY	1	t	206
9816	Suzukota MFY	1	t	206
9817	Taxtapul MFY	1	t	206
9818	Tinchlik MFY	1	t	206
9819	Xadra MFY	1	t	206
9820	Xuvaydo MFY	1	t	206
9821	Yangi Komolon MFY	1	t	206
9822	Yangi-Beltepa MFY	1	t	206
9823	Yangiobod MFY	1	t	206
9824	Yangishaxar MFY	1	t	206
9825	Zafarobod MFY	1	t	206
9826	Zangiota MFY	1	t	206
9827	Akbarobod MFY	1	t	207
9828	Astrobod MFY	1	t	207
9829	Axilobod MFY	1	t	207
9830	Axmad Donish MFY	1	t	207
9831	Beruniy MFY	1	t	207
9832	Bobodexkon MFY	1	t	207
9833	Bodomzor MFY	1	t	207
9834	Bogishamol MFY	1	t	207
9835	Chinor MFY	1	t	207
9836	Chosh-tepa MFY	1	t	207
9837	Do`stlik MFY	1	t	207
9838	Firdavsiy MFY	1	t	207
9839	G`. Abdullaev MFY	1	t	207
9840	Gayratiy MFY	1	t	207
9841	Guliston MFY	1	t	207
9842	Islomobod MFY	1	t	207
9843	Ittifoq MFY	1	t	207
9844	Jomiy MFY	1	t	207
9845	Kashkar MFY	1	t	207
9846	Kulolkurgon MFY	1	t	207
9847	Kushchinor MFY	1	t	207
9848	M. Ulugbek MFY	1	t	207
9849	Matonat MFY	1	t	207
9850	Ming-Urik MFY	1	t	207
9851	Minor MFY	1	t	207
9852	Navruz MFY	1	t	207
9853	Nodirabegim MFY	1	t	207
9854	Obod MFY	1	t	207
9855	Okibat MFY	1	t	207
9856	Okkurgon MFY	1	t	207
9857	Oktepa MFY	1	t	207
9858	Otchopar-1 MFY	1	t	207
9859	Otchopar-2 MFY	1	t	207
9860	Oybek MFY	1	t	207
9861	Posira MFY	1	t	207
9862	Sharq-Haqiqati MFY	1	t	207
9863	Shaxriston MFY	1	t	207
9864	Shayx Shivli MFY	1	t	207
9865	Shodlik MFY	1	t	207
9866	Sobirobod MFY	1	t	207
9867	Tinchlik MFY	1	t	207
9868	Turk-Kurgon MFY	1	t	207
9869	Turkiston MFY	1	t	207
9870	Turon MFY	1	t	207
9871	Uch-Kaxramon MFY	1	t	207
9872	Umid MFY	1	t	207
9873	Usta-Shirin MFY	1	t	207
9874	Uvaysiy MFY	1	t	207
9875	Uzbek.Mustak. MFY	1	t	207
9876	Xasanboy MFY	1	t	207
9877	Xiyobon tepa MFY	1	t	207
9878	Xusniobod MFY	1	t	207
9879	Yangi-xayot MFY	1	t	207
9880	Yangiarik MFY	1	t	207
9881	Yangiobod MFY	1	t	207
9882	Yunus ota MFY	1	t	207
9883	Yunusobod MFY	1	t	207
9884	 Yakkasaroy MFY	1	t	208
9885	 Yakkasaroy 2 MFY	1	t	208
9886	 Rakat MFY	1	t	208
9887	 A.Avloniy MFY	1	t	208
9888	 Muqimiy MFY	1	t	208
9889	 O`rikzor MFY	1	t	208
9890	 To`qimachi MFY	1	t	208
9891	 Bobur MFY	1	t	208
9892	 Qushbegi MFY	1	t	208
9893	 Boshliq MFY	1	t	208
9894	 Usmon Nosir MFY	1	t	208
9895	 Abdulla Qaxxor MFY	1	t	208
9896	 Dam-ariq MFY	1	t	208
9897	 Konstitutsiya MFY	1	t	208
9898	 Tepa MFY	1	t	208
9899	 Turkiston MFY	1	t	208
9900	 Hamid Sulaymonov MFY	1	t	208
9901	 Yunus Rajabiy MFY	1	t	208
9902	Adabiyot OFY	1	t	20
9903	O├Жrnak OFY	1	t	20
9904	Turon MFY	1	t	20
9905	Bo├Жston MFY	1	t	20
9906	Turkiston MFY	1	t	20
9907	Xorazm OFY	1	t	20
9908	Qanli OFY	1	t	20
9909	Olmazor MFY	1	t	20
9910	Gulobod MFY	1	t	20
9911	Qumbuz OFY	1	t	20
9912	Novoiy MFY	1	t	20
9913	Temiryo├Жl MFY	1	t	20
9914	Abad makan MP	1	t	209
9915	Jayxun MP	1	t	209
9916	Taqiyatas MP	1	t	209
9917	Shamshiraq MP	1	t	209
9918	Dosliq MP	1	t	209
9919	Xaliqlar doslig'i MP	1	t	209
9920	Qusshiliq MP	1	t	209
9921	Orayliq MP	1	t	209
9922	Aydin jol MP	1	t	209
9923	Nurli kelejek MP	1	t	209
9924	Naymankol AP	1	t	209
9925	Keneges AP	1	t	209
9926	Saraykol AP	1	t	209
9927	Yangi qishloq MFY	1	t	130
9928	Xalqabod MFY	1	t	130
9929	Qipchoq OFY	1	t	20
9930	Ajiniyaz OFY	1	t	20
9931	Suuenli OFY	1	t	20
9932	Ravshan OFY	1	t	20
9933	Mehnatobod OFY	1	t	20
9934	Ko├Жkdaryo OFY	1	t	20
9935	Ustirt OFY	1	t	20
9936	Qo├Жng├Жirot OFY	1	t	20
9937	Qung'irot MFY	1	t	20
9938	Ozodlik MFY	1	t	20
9939	Taraqli MFY	1	t	20
9940	Jinishke MFY	1	t	20
9941	Sanoat MFY	1	t	20
9942	Hokim ota MFY	1	t	20
9943	Mingjarg├Жon MFY	1	t	20
9944	Talliq MFY	1	t	20
9945	Qoratol MFY	1	t	20
9946	Xanjap MFY	1	t	20
9947	Monshaqli MFY	1	t	20
9948	Qumbiz MFY	1	t	20
9949	Berdax MFY	1	t	20
9950	Qashi MFY	1	t	20
9951	Kiyet MFY	1	t	20
9952	Oltinko├Жl ShFY	1	t	20
9953	Elobod ShFY	1	t	20
9954	Jasliq ShFY	1	t	20
9955	Qirq qiz ShFY	1	t	20
9956	Qoraqalpog├Жiston ShFY	1	t	20
9957	Abay OFY	1	t	16
9958	Amir Temur MFY	1	t	16
9959	Beruniy OFY	1	t	16
9960	Biybazar OFY	1	t	16
9961	Birlik MFY	1	t	16
9962	Bunyodkor MFY	1	t	16
9963	Bo'ston MFY	1	t	16
9964	Guliston MFY	1	t	16
9965	Do'stlik MFY	1	t	16
9966	Do'stlik OFY	1	t	16
9967	Jayxun MFY	1	t	16
9968	Jumaniyazov MFY	1	t	16
9969	Ibn-Sino MFY	1	t	16
9970	Istiqlol MFY	1	t	16
9971	Qangshartal MFY	1	t	16
9972	Qiyot MFY	1	t	16
9973	Qizilqal'a OFY	1	t	16
9974	Markaziy MFY	1	t	16
9975	Maxtumquli OFY	1	t	16
9976	Mustaqillik MFY	1	t	16
9977	Navoiy MFY	1	t	16
9978	Navoiy OFY	1	t	16
9979	Navro'z MFY	1	t	16
9980	Nayman MFY	1	t	16
9981	Ozod OFY	1	t	16
9982	Oltinsoy OFY	1	t	16
9983	Palvash MFY	1	t	16
9984	Paxtakor MFY	1	t	16
9985	Sarkop OFY	1	t	16
9986	Tinchlik OFY	1	t	16
9987	To'qimachi MFY	1	t	16
9988	Turon MFY	1	t	16
9989	Xorazm MFY	1	t	16
9990	Shabboz OFY	1	t	16
9991	Shimom OFY	1	t	16
9992	Shobboz MFY	1	t	16
9993	Yangiobod MFY	1	t	16
9994	Bayterak OFY	1	t	26
9995	Juzimzar OFY	1	t	26
9996	Tinichlik OFY	1	t	26
9997	Kun Nuri OFY	1	t	26
9998	Murtazabiy OFY	1	t	26
9999	Madeniyat OFY	1	t	26
10000	Janajap OFY	1	t	26
10001	Nurli jol OFY	1	t	26
10002	Qiqinchi OFY	1	t	26
10003	Suwenli OFY	1	t	26
10004	Parvoz OFY	1	t	26
10005	Qumbiz OFY	1	t	26
10006	Shagala OFY	1	t	26
10007	Tutzor OFY	1	t	26
10008	Bunyuodkor OFY	1	t	26
10009	Nawriz-mfylar OFY	1	t	26
10010	Kulap OFY	1	t	26
10011	Sarshingul OFY	1	t	26
10012	Mustaqillik OFY	1	t	26
10013	Amudaryo OFY	1	t	26
10014	Qumjiqqin OFY	1	t	26
10015	Samankul OFY	1	t	26
10016	Vodnik-poselkasi	1	t	26
10017	Obod OFY	1	t	26
10018	Arzimbetqum OFY	1	t	18
10019	Besko'pir OFY	1	t	18
10020	Bo'ston OFY	1	t	18
10021	Jayhun MFY	1	t	18
10022	Jana qala OFY	1	t	18
10023	Qosjap OFY	1	t	18
10024	Navruz OFY	1	t	18
10025	Qonliko'l OFY	1	t	18
10026	Do'stlik MFY	1	t	18
10027	Madaniyat MFY	1	t	18
10028	Qonliko'l SHFY	1	t	18
10029	Taxtako`pir PFY	1	t	24
10030	Aydin jol MFY	1	t	24
10031	Dawir MFY	1	t	24
10032	G`arezsizlik MFY	1	t	24
10033	Taxtako`pir OFY	1	t	24
10034	Atako`l OFY	1	t	24
10035	O`zbekiston OFY	1	t	24
10036	Qaraoy MFY	1	t	24
10037	Qarateren` OFY	1	t	24
10038	Da`wqara MFY	1	t	24
10039	Mulik OFY	1	t	24
10040	Dawitsay MFY	1	t	24
10041	Marjanko`l OFY	1	t	24
10042	Jan`adarya OFY	1	t	24
10043	Beltaw OFY	1	t	24
10044	Qon`iratko`l OFY	1	t	24
10045	Qostruba KMFY	1	t	24
10046	Iftixor MFY	1	t	185
10047	O'rmonchilar MFY	1	t	185
10048	Sh. Rashidov MFY	1	t	185
10049	Tinchlik MFY	1	t	185
10050	Al-Farg'oniy MFY	1	t	185
10051	Soy bo'yi MFY	1	t	185
10052	Ibrat MFY	1	t	185
10053	Yoshlar MFY	1	t	185
10054	Farg'ona MFY	1	t	185
10055	Shodiyona MFY	1	t	185
10056	Yangi soy MFY	1	t	185
10057	Ma'rifat MFY	1	t	185
10058	Simtepa MFY	1	t	185
10059	Baxor MFY	1	t	185
10060	Furqat MFY	1	t	185
10061	Oybek MFY	1	t	185
10062	Yangi yo'l MFY	1	t	185
10063	Istiqlol MFY	1	t	185
10064	Zarbdor MFY	1	t	185
10065	Guliston MFY	1	t	185
10066	Bo'ston MFY	1	t	185
10067	Mustaqillik MFY	1	t	185
10068	1-Beshbola MFY	1	t	185
10069	Shakarqishloq MFY	1	t	185
10070	Jo'ydam MFY	1	t	185
10071	To'qimachilar MFY	1	t	185
10072	S. Temur MFY	1	t	185
10073	Navro'z MFY	1	t	185
10074	Mash'al MFY	1	t	185
10075	A. Navoiy MFY	1	t	185
10076	Oqariqobod MFY	1	t	185
10077	Al-Xorazmiy MFY	1	t	185
10078	A. Jomiy MFY	1	t	185
10079	Do'stlik MFY	1	t	185
10080	Bobur MFY	1	t	185
10081	Lolazor MFY	1	t	185
10082	A. Qodiriy MFY	1	t	185
10083	Sovurbuloq MFY	1	t	185
10084	Afrosiyob MFY	1	t	185
10085	Madadkor MFY	1	t	185
10086	M. Ulug'bek MFY	1	t	185
10087	Parvoz MFY	1	t	185
10088	Nodirabegim MFY	1	t	185
10089	Besh Bola MFY	1	t	185
10090	Yormazor MFY	1	t	185
10091	Oq-ariq MFY	1	t	185
10092	Ipak yo'li MFY	1	t	185
10093	Sharshara MFY	1	t	185
10094	Shodlik MFY	1	t	185
10095	Nafosat MFY	1	t	185
10096	Sohibkor MFY	1	t	185
10097	Gulzor MFY	1	t	185
10098	Beglar MFY	1	t	185
10099	O'zbekiston MFY	1	t	185
10100	Tabassum MFY	1	t	185
10101	Beruniy MFY	1	t	185
10102	Xamkorlik MFY	1	t	185
10103	Madaniyat MFY	1	t	185
10104	Istiqbol MFY	1	t	185
10105	Mehribonlik MFY	1	t	185
10106	Navbaxor MFY	1	t	185
10107	Yulduz MFY	1	t	185
10108	Ibn Sino MFY	1	t	185
10109	Barkamol MFY	1	t	185
10110	Kimyogar MFY	1	t	185
10111	Muruvvat MFY	1	t	185
10112	Xuvaydo MFY	1	t	185
10113	Kirgili MFY	1	t	185
10114	Surxtepa MFY	1	t	185
10115	Xo'jamag'iz MFY	1	t	185
10116	Aybiynur OFY	1	t	28
10117	Ak jap OFY	1	t	28
10118	Begjap OFY	1	t	28
10119	Birleshik OFY	1	t	28
10120	Diyxanabad OFY	1	t	28
10121	Ketenler OFY	1	t	28
10122	Mamiy OFY	1	t	28
10123	Sarmanbaykol OFY	1	t	28
10124	2-sonli MFY 	1	t	28
10125	4-sonli MFY	1	t	28
10126	1-sonli MFY	1	t	28
10127	1-sonli MFY	1	t	28
10128	Bandixon MFY	1	t	130
10129	Toktau MPJ	1	t	22
10130	Arbashi OFY	1	t	22
10131	Bakanshakli OFY	1	t	22
10132	Kerder OFY	1	t	22
10133	Krantau OFY	1	t	22
10134	Kutankul MFY	1	t	22
10135	Oqmangit PFY	1	t	22
10136	Oqterak MFY	1	t	22
10137	Samanbay OFY	1	t	22
10138	Takirkul OFY	1	t	22
10139	Qo'riq QFY	1	t	72
10140	Uchturgan QFY	1	t	72
10141	Pastkichaqir QFY	1	t	72
10142	Sohibkor QFY	1	t	72
10143	Iskandar QFY	1	t	72
10144	Jo'langar QFY	1	t	72
10145	Namingon QFY	1	t	72
10146	Mo'g'ol QFY	1	t	72
10147	Xo'jamishkent QFY	1	t	72
10148	Chakand QFY	1	t	72
10149	Istiqlol MFY\r\n	1	t	172
10150	Taraqqiyot MFY\r\n	1	t	172
10151	Oftobmakon MFY\r\n	1	t	138
10152	Ma├Жrifat MFY	1	t	215
10153	Halimkop MFY	1	t	215
10154	Gulobod MFY	1	t	215
10155	Gultepa MFY	1	t	215
10156	Kalas MFY	1	t	215
10157	Farovon MFY	1	t	215
10158	Chuvalachi MFY	1	t	215
10159	Navoiy MFY	1	t	215
10160	Hasanboy MFY	1	t	215
10161	Keles shahri	1	t	215
10162	Qizg├Жaldoq MFY	1	t	215
10163	Keles massivi	1	t	215
10164	Uch chinor MFY	1	t	215
10165	Ittifoq MFY	1	t	215
10166	G├Жishtko├Жprik MFY	1	t	215
10167	Guliston MFY	1	t	215
10168	Masalboy MFY	1	t	215
10169	Parvoz MFY	1	t	156
10170	Navro'z MFY	1	t	213
10171	Sabo MFY	1	t	213
10172	Mustaqillik MFY	1	t	213
10173	Baxt MFY	1	t	213
10174	Ishchilar shaharchasi MFY	1	t	213
10175	Olmos (S.Sultonova) MFY	1	t	213
10176	Yangi bog' (N.Niyozov) MFY	1	t	213
10177	Mezon MFY	1	t	213
10178	Ramadon MFY	1	t	213
10179	Mevazor MFY	1	t	213
10180	Oltinobod MFY	1	t	213
10181	Fayzobod MFY	1	t	213
10182	Fayzli (Farxod) MFY	1	t	213
11183	Adolat MFY	1	t	207
11184	Taraqqiyot MFY	1	t	52
\.


--
-- Data for Name: user_region; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_region (id, title, sort, is_active) FROM stdin;
1	Qoraqalpog'iston Respublikasi	1	t
2	Andijon viloyati	1	t
3	Buxoro viloyati	1	t
4	Jizzax viloyati	1	t
5	Qashqadaryo viloyati	1	t
6	Navoiy viloyati	1	t
7	Namangan viloyati	1	t
8	Samarqand viloyati	1	t
9	Surxandaryo viloyati	1	t
10	Sirdaryo viloyati	1	t
11	Toshkent viloyati	1	t
12	Farg'ona viloyati	1	t
13	Xorazm viloyati	1	t
14	Toshkent shahri	1	t
\.


--
-- Data for Name: user_section; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_section (id, title, is_active, pay_for_service, address, parent_id, region_id) FROM stdin;
1	Buxoro viloyat IIB YHXB	t	f	Buxoro viloyati Buxoro shahri	\N	3
2	1-son RO' va IOB	t	t	Buxoro shahri Qayum Murtazoyev ko'chasi	1	3
3	3-son RO' va IOB	t	t	Buxoro viloyati Jondor tumani	1	3
4	2-son RO' va IOB	t	t	Buxoro viloyati Vobkent tumani	1	3
\.


--
-- Data for Name: user_section_district; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_section_district (id, section_id, district_id) FROM stdin;
1	2	47
2	2	48
3	2	52
4	2	53
5	2	55
6	3	56
7	3	51
8	3	54
9	4	49
10	4	50
11	4	59
\.


--
-- Data for Name: user_sms; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_sms (id, created_at, updated_at, is_active, sms_count, text, sms_id, status, phone) FROM stdin;
1	2021-10-16 14:43:13.482873+05	2021-10-16 14:43:13.48292+05	t	1	E-RIB dasturidan ro'yhatdan o'tishni yakunlash va tizimga kirish ma'lumotlari  \nLogin: 972800809 \nParol: 26154	17952689	102	972800809
\.


--
-- Data for Name: user_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user (id, password, last_name, first_name, middle_name, role, address, email, birthday, username, phone, passport_seriya, passport_number, person_id, issue_by_whom, is_staff, is_superuser, is_active, last_login, date_joined, gender, turbo, secret_key, district_id, quarter_id, region_id, section_id) FROM stdin;
6	pbkdf2_sha256$216000$H864mqxZqMj6$kenxMlHEbB+BdYkmxJKDFuOBlTMZN8FGTs3gtwJ2BPI=	Gafurova	Zebiniso	Raxmatovna	1	Usmonobod qishlog'i		1981-02-11	914436148	914436148	AA	1430438	41102815300018	KOGON TUMANI IIB	f	f	t	2021-10-11 08:57:33.657+05	2021-10-11 08:51:14.38+05	0	28040	8e462628-7516-4fce-8fd3-b70ea101f5c7	52	1664	3	\N
8	pbkdf2_sha256$216000$qEW5h31CBuUu$T/q2ZUxYIxu0cd8ZcUrAMbTN2Adi/FEp/nfYgGQhG1c=	Nasriddinov	Shoxrux	Zayni o'g'li	1	Piridastgir 9/7		1998-04-11	914438896	914438896	AA	4438896	56565489898795	BUXORO SHAHAR IIB	f	f	t	2021-10-12 09:36:44.581+05	2021-10-12 09:35:02.087+05	0	38356	17ef53fb-682e-4956-abdb-2a80ca45e469	47	1409	3	\N
7	pbkdf2_sha256$216000$F52PDIX64K2y$rhTdviQF8r9S3rez70JXcp5wO4+Ar4USRxvWW34cBJ0=	Yoqubov	Sirojiddin	Tojiddin o'g'li	1	M.Iqbol 38		2021-10-12	919791999	919791999	AA	3865694	15997266845269	BUXORO SHAHAR IIB	f	f	t	2021-10-15 20:56:18.537693+05	2021-10-12 09:12:04.625+05	0	m6232971M	15ed2cfb-a38e-4bda-a7cf-fe0c7657cd32	52	1648	3	\N
5	pbkdf2_sha256$216000$jOZowEwb8R0q$8ICmdMEcEiketFfDR0jjYIpTSwlkFhDV41dosyGZc1s=	Yoqubov	Salohiddin	Tojiddinovich	2	Hh		1996-10-10	906366264	906366264	AA	34686673	69498638838823	BUXORO SHAHAR IIB	f	f	t	2021-10-16 09:21:21.007495+05	2021-10-10 22:22:09.223+05	0	67096	3b329708-1bde-48df-a7be-c0e117513eea	52	1664	3	2
1	pbkdf2_sha256$216000$36vCyz8TRgM6$b6EaeKWkZs+h5Q9TVu0eDbNng60BSIv7p1ZVneBdUt0=				1	\N		2021-10-03	admin	\N	\N	\N	\N	\N	t	t	t	2021-10-17 11:36:42.559857+05	2021-10-03 15:18:46.583+05	0	\N	1220402c-aa90-4b1e-bde7-8b17359593d3	\N	\N	\N	\N
3	pbkdf2_sha256$216000$TnZqyob9wpBp$WzFgy+VC6RJ6uVlCVCGwMFGqoq+c2LnLj8ZRwUOqUKo=	Yoqubov	Salohiddin	Tojiddin o'g'li	8	M.Iqbol		2020-01-01	972800908	972800908	AA	3565655	42554622222623	BUXORO SHAHAR IIB	f	f	t	2021-10-17 12:15:25.89011+05	2021-10-04 17:55:10.759+05	0	91879	09fa6588-985f-46ba-b9c8-8dee2fd242a0	47	1369	3	2
9	pbkdf2_sha256$216000$eF46T59z7dp1$BJgKstbpTnPa/VniWpKsHzZdHYpvgfEni1t574+bCD8=	Yoqubov	Salohiddin	Tojiddin o'g'li	1	Rabotipoyon qishlog'i 76-uy		1996-06-07	972800809	972800809	AD	311169	30706965300029	KOGON TUMANI IIB 	f	f	t	2021-10-17 16:16:54.898366+05	2021-10-16 14:43:12.3996+05	0	26154	cd9e5f80-cd59-41a2-a8fb-af8945112678	52	1664	3	\N
\.


--
-- Data for Name: user_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: user_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: account_emailaddress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailaddress_id_seq', 1, false);


--
-- Name: account_emailconfirmation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_emailconfirmation_id_seq', 1, false);


--
-- Name: application_application_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.application_application_id_seq', 21, true);


--
-- Name: application_applicationcashbymoderator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.application_applicationcashbymoderator_id_seq', 9, true);


--
-- Name: application_applicationdocument_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.application_applicationdocument_id_seq', 15, true);


--
-- Name: application_applicationdocumentattachment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.application_applicationdocumentattachment_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 176, true);


--
-- Name: click_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.click_order_id_seq', 1, false);


--
-- Name: clickuz_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clickuz_transaction_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 83, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 44, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 128, true);


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_site_id_seq', 1, true);


--
-- Name: paycom_paycomtransaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paycom_paycomtransaction_id_seq', 1, false);


--
-- Name: service_amountbasecalculation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_amountbasecalculation_id_seq', 1, true);


--
-- Name: service_exampledocument_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_exampledocument_id_seq', 4, true);


--
-- Name: service_paidstateduty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_paidstateduty_id_seq', 8, true);


--
-- Name: service_service_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_service_document_id_seq', 9, true);


--
-- Name: service_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_service_id_seq', 6, true);


--
-- Name: service_stateduty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_stateduty_id_seq', 2, true);


--
-- Name: service_statedutypercent_car_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_statedutypercent_car_type_id_seq', 27, true);


--
-- Name: service_statedutypercent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_statedutypercent_id_seq', 29, true);


--
-- Name: service_statedutypercent_service_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_statedutypercent_service_id_seq', 53, true);


--
-- Name: service_statedutyscore_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_statedutyscore_id_seq', 37, true);


--
-- Name: socialaccount_socialaccount_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialaccount_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_id_seq', 1, false);


--
-- Name: socialaccount_socialapp_sites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialapp_sites_id_seq', 1, false);


--
-- Name: socialaccount_socialtoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.socialaccount_socialtoken_id_seq', 1, false);


--
-- Name: user_bodytype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_bodytype_id_seq', 2, true);


--
-- Name: user_car_device_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_car_device_id_seq', 1, false);


--
-- Name: user_car_fuel_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_car_fuel_type_id_seq', 28, true);


--
-- Name: user_car_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_car_id_seq', 36, true);


--
-- Name: user_car_re_fuel_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_car_re_fuel_type_id_seq', 1, false);


--
-- Name: user_carmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_carmodel_id_seq', 74, true);


--
-- Name: user_cartype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_cartype_id_seq', 11, true);


--
-- Name: user_color_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_color_id_seq', 83, true);


--
-- Name: user_constant_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_constant_id_seq', 1, false);


--
-- Name: user_device_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_device_id_seq', 4, true);


--
-- Name: user_district_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_district_id_seq', 215, true);


--
-- Name: user_fueltype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_fueltype_id_seq', 2, true);


--
-- Name: user_notification_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_notification_id_seq', 2, true);


--
-- Name: user_organization_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_organization_id_seq', 1, true);


--
-- Name: user_quarter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_quarter_id_seq', 11184, true);


--
-- Name: user_region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_region_id_seq', 14, true);


--
-- Name: user_section_district_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_section_district_id_seq', 11, true);


--
-- Name: user_section_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_section_id_seq', 4, true);


--
-- Name: user_sms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_sms_id_seq', 1, true);


--
-- Name: user_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_groups_id_seq', 1, false);


--
-- Name: user_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_id_seq', 9, true);


--
-- Name: user_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_user_user_permissions_id_seq', 1, false);


--
-- Name: account_emailaddress account_emailaddress_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_email_key UNIQUE (email);


--
-- Name: account_emailaddress account_emailaddress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_pkey PRIMARY KEY (id);


--
-- Name: account_emailconfirmation account_emailconfirmation_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_key_key UNIQUE (key);


--
-- Name: account_emailconfirmation account_emailconfirmation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirmation_pkey PRIMARY KEY (id);


--
-- Name: application_application application_application_file_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_application_file_name_key UNIQUE (file_name);


--
-- Name: application_application application_application_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_application_pkey PRIMARY KEY (id);


--
-- Name: application_applicationcashbymoderator application_applicationcashbymoderator_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationcashbymoderator
    ADD CONSTRAINT application_applicationcashbymoderator_pkey PRIMARY KEY (id);


--
-- Name: application_applicationdocument application_applicationdocument_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocument
    ADD CONSTRAINT application_applicationdocument_pkey PRIMARY KEY (id);


--
-- Name: application_applicationdocumentattachment application_applicationdocumentattachment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocumentattachment
    ADD CONSTRAINT application_applicationdocumentattachment_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: click_order click_order_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.click_order
    ADD CONSTRAINT click_order_pkey PRIMARY KEY (id);


--
-- Name: clickuz_transaction clickuz_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clickuz_transaction
    ADD CONSTRAINT clickuz_transaction_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site django_site_domain_a2e37b91_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);


--
-- Name: django_site django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: paycom_paycomtransaction paycom_paycomtransaction_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paycom_paycomtransaction
    ADD CONSTRAINT paycom_paycomtransaction_pkey PRIMARY KEY (id);


--
-- Name: service_amountbasecalculation service_amountbasecalculation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_amountbasecalculation
    ADD CONSTRAINT service_amountbasecalculation_pkey PRIMARY KEY (id);


--
-- Name: service_exampledocument service_exampledocument_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_exampledocument
    ADD CONSTRAINT service_exampledocument_key_key UNIQUE (key);


--
-- Name: service_exampledocument service_exampledocument_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_exampledocument
    ADD CONSTRAINT service_exampledocument_pkey PRIMARY KEY (id);


--
-- Name: service_paidstateduty service_paidstateduty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_paidstateduty
    ADD CONSTRAINT service_paidstateduty_pkey PRIMARY KEY (id);


--
-- Name: service_service_document service_service_document_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service_document
    ADD CONSTRAINT service_service_document_pkey PRIMARY KEY (id);


--
-- Name: service_service_document service_service_document_service_id_exampledocume_d666dbce_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service_document
    ADD CONSTRAINT service_service_document_service_id_exampledocume_d666dbce_uniq UNIQUE (service_id, exampledocument_id);


--
-- Name: service_service service_service_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service
    ADD CONSTRAINT service_service_key_key UNIQUE (key);


--
-- Name: service_service service_service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service
    ADD CONSTRAINT service_service_pkey PRIMARY KEY (id);


--
-- Name: service_stateduty service_stateduty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_stateduty
    ADD CONSTRAINT service_stateduty_pkey PRIMARY KEY (id);


--
-- Name: service_statedutypercent_car_type service_statedutypercent_car_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_car_type
    ADD CONSTRAINT service_statedutypercent_car_type_pkey PRIMARY KEY (id);


--
-- Name: service_statedutypercent service_statedutypercent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent
    ADD CONSTRAINT service_statedutypercent_pkey PRIMARY KEY (id);


--
-- Name: service_statedutypercent_service service_statedutypercent_service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_service
    ADD CONSTRAINT service_statedutypercent_service_pkey PRIMARY KEY (id);


--
-- Name: service_statedutypercent_car_type service_statedutypercent_statedutypercent_id_cart_4d97b02e_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_car_type
    ADD CONSTRAINT service_statedutypercent_statedutypercent_id_cart_4d97b02e_uniq UNIQUE (statedutypercent_id, cartype_id);


--
-- Name: service_statedutypercent_service service_statedutypercent_statedutypercent_id_serv_69dc7887_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_service
    ADD CONSTRAINT service_statedutypercent_statedutypercent_id_serv_69dc7887_uniq UNIQUE (statedutypercent_id, service_id);


--
-- Name: service_statedutyscore service_statedutyscore_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutyscore
    ADD CONSTRAINT service_statedutyscore_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_provider_uid_fc810c6e_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_provider_uid_fc810c6e_uniq UNIQUE (provider, uid);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp__socialapp_id_site_id_71a9a768_uniq UNIQUE (socialapp_id, site_id);


--
-- Name: socialaccount_socialapp socialaccount_socialapp_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp
    ADD CONSTRAINT socialaccount_socialapp_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialapp_sites socialaccount_socialapp_sites_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_socialapp_sites_pkey PRIMARY KEY (id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq UNIQUE (app_id, account_id);


--
-- Name: socialaccount_socialtoken socialaccount_socialtoken_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_socialtoken_pkey PRIMARY KEY (id);


--
-- Name: user_bodytype user_bodytype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_bodytype
    ADD CONSTRAINT user_bodytype_pkey PRIMARY KEY (id);


--
-- Name: user_car_device user_car_device_car_id_device_id_247d4617_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_device
    ADD CONSTRAINT user_car_device_car_id_device_id_247d4617_uniq UNIQUE (car_id, device_id);


--
-- Name: user_car_device user_car_device_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_device
    ADD CONSTRAINT user_car_device_pkey PRIMARY KEY (id);


--
-- Name: user_car_fuel_type user_car_fuel_type_car_id_fueltype_id_d3e9f1bd_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_fuel_type
    ADD CONSTRAINT user_car_fuel_type_car_id_fueltype_id_d3e9f1bd_uniq UNIQUE (car_id, fueltype_id);


--
-- Name: user_car_fuel_type user_car_fuel_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_fuel_type
    ADD CONSTRAINT user_car_fuel_type_pkey PRIMARY KEY (id);


--
-- Name: user_car user_car_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_pkey PRIMARY KEY (id);


--
-- Name: user_car_re_fuel_type user_car_re_fuel_type_car_id_fueltype_id_00be2196_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_re_fuel_type
    ADD CONSTRAINT user_car_re_fuel_type_car_id_fueltype_id_00be2196_uniq UNIQUE (car_id, fueltype_id);


--
-- Name: user_car_re_fuel_type user_car_re_fuel_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_re_fuel_type
    ADD CONSTRAINT user_car_re_fuel_type_pkey PRIMARY KEY (id);


--
-- Name: user_carmodel user_carmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_carmodel
    ADD CONSTRAINT user_carmodel_pkey PRIMARY KEY (id);


--
-- Name: user_cartype user_cartype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_cartype
    ADD CONSTRAINT user_cartype_pkey PRIMARY KEY (id);


--
-- Name: user_color user_color_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_color
    ADD CONSTRAINT user_color_pkey PRIMARY KEY (id);


--
-- Name: user_constant user_constant_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_constant
    ADD CONSTRAINT user_constant_pkey PRIMARY KEY (id);


--
-- Name: user_device user_device_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_device
    ADD CONSTRAINT user_device_pkey PRIMARY KEY (id);


--
-- Name: user_district user_district_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_district
    ADD CONSTRAINT user_district_pkey PRIMARY KEY (id);


--
-- Name: user_fueltype user_fueltype_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_fueltype
    ADD CONSTRAINT user_fueltype_pkey PRIMARY KEY (id);


--
-- Name: user_notification user_notification_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification
    ADD CONSTRAINT user_notification_pkey PRIMARY KEY (id);


--
-- Name: user_organization user_organization_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_organization
    ADD CONSTRAINT user_organization_pkey PRIMARY KEY (id);


--
-- Name: user_quarter user_quarter_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_quarter
    ADD CONSTRAINT user_quarter_pkey PRIMARY KEY (id);


--
-- Name: user_region user_region_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_region
    ADD CONSTRAINT user_region_pkey PRIMARY KEY (id);


--
-- Name: user_section_district user_section_district_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section_district
    ADD CONSTRAINT user_section_district_pkey PRIMARY KEY (id);


--
-- Name: user_section_district user_section_district_section_id_district_id_3b1d1fa3_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section_district
    ADD CONSTRAINT user_section_district_section_id_district_id_3b1d1fa3_uniq UNIQUE (section_id, district_id);


--
-- Name: user_section user_section_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section
    ADD CONSTRAINT user_section_pkey PRIMARY KEY (id);


--
-- Name: user_sms user_sms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_sms
    ADD CONSTRAINT user_sms_pkey PRIMARY KEY (id);


--
-- Name: user_user_groups user_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_pkey PRIMARY KEY (id);


--
-- Name: user_user_groups user_user_groups_user_id_group_id_bb60391f_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_group_id_bb60391f_uniq UNIQUE (user_id, group_id);


--
-- Name: user_user user_user_phone_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_phone_key UNIQUE (phone);


--
-- Name: user_user user_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_pkey PRIMARY KEY (id);


--
-- Name: user_user user_user_secret_key_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_secret_key_key UNIQUE (secret_key);


--
-- Name: user_user_user_permissions user_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: user_user_user_permissions user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq UNIQUE (user_id, permission_id);


--
-- Name: user_user user_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_username_key UNIQUE (username);


--
-- Name: account_emailaddress_email_03be32b2_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_email_03be32b2_like ON public.account_emailaddress USING btree (email varchar_pattern_ops);


--
-- Name: account_emailaddress_user_id_2c513194; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailaddress_user_id_2c513194 ON public.account_emailaddress USING btree (user_id);


--
-- Name: account_emailconfirmation_email_address_id_5b7f8c58; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_email_address_id_5b7f8c58 ON public.account_emailconfirmation USING btree (email_address_id);


--
-- Name: account_emailconfirmation_key_f43612bd_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX account_emailconfirmation_key_f43612bd_like ON public.account_emailconfirmation USING btree (key varchar_pattern_ops);


--
-- Name: application_application_car_id_5c379ac3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_car_id_5c379ac3 ON public.application_application USING btree (car_id);


--
-- Name: application_application_created_user_id_af2baa12; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_created_user_id_af2baa12 ON public.application_application USING btree (created_user_id);


--
-- Name: application_application_file_name_5d9763f7_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_file_name_5d9763f7_like ON public.application_application USING btree (file_name varchar_pattern_ops);


--
-- Name: application_application_inspector_id_85a5b21c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_inspector_id_85a5b21c ON public.application_application USING btree (inspector_id);


--
-- Name: application_application_organization_id_917a8f4a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_organization_id_917a8f4a ON public.application_application USING btree (organization_id);


--
-- Name: application_application_section_id_b8812a68; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_section_id_b8812a68 ON public.application_application USING btree (section_id);


--
-- Name: application_application_service_id_bfd98186; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_application_service_id_bfd98186 ON public.application_application USING btree (service_id);


--
-- Name: application_applicationcas_paid_state_duty_id_b1c41afc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_applicationcas_paid_state_duty_id_b1c41afc ON public.application_applicationcashbymoderator USING btree (paid_state_duty_id);


--
-- Name: application_applicationcashbymoderator_application_id_5f3afd45; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_applicationcashbymoderator_application_id_5f3afd45 ON public.application_applicationcashbymoderator USING btree (application_id);


--
-- Name: application_applicationcashbymoderator_moderator_id_d0e4f073; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_applicationcashbymoderator_moderator_id_d0e4f073 ON public.application_applicationcashbymoderator USING btree (moderator_id);


--
-- Name: application_applicationdoc_application_document_id_d5df8b12; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_applicationdoc_application_document_id_d5df8b12 ON public.application_applicationdocumentattachment USING btree (application_document_id);


--
-- Name: application_applicationdocument_application_id_fb8da163; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_applicationdocument_application_id_fb8da163 ON public.application_applicationdocument USING btree (application_id);


--
-- Name: application_applicationdocument_example_document_id_48f532dc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX application_applicationdocument_example_document_id_48f532dc ON public.application_applicationdocument USING btree (example_document_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: click_order_service_id_a658b85c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX click_order_service_id_a658b85c ON public.click_order USING btree (service_id);


--
-- Name: click_order_user_id_a4619fcc; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX click_order_user_id_a4619fcc ON public.click_order USING btree (user_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: django_site_domain_a2e37b91_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);


--
-- Name: service_exampledocument_key_d077a531_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_exampledocument_key_d077a531_like ON public.service_exampledocument USING btree (key varchar_pattern_ops);


--
-- Name: service_paidstateduty_application_id_7ece44a6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_paidstateduty_application_id_7ece44a6 ON public.service_paidstateduty USING btree (application_id);


--
-- Name: service_paidstateduty_percent_id_b6bdb667; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_paidstateduty_percent_id_b6bdb667 ON public.service_paidstateduty USING btree (percent_id);


--
-- Name: service_paidstateduty_score_id_b2b81fac; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_paidstateduty_score_id_b2b81fac ON public.service_paidstateduty USING btree (score_id);


--
-- Name: service_service_document_exampledocument_id_0f212f43; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_service_document_exampledocument_id_0f212f43 ON public.service_service_document USING btree (exampledocument_id);


--
-- Name: service_service_document_service_id_e4912b68; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_service_document_service_id_e4912b68 ON public.service_service_document USING btree (service_id);


--
-- Name: service_service_key_eeae4df0_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_service_key_eeae4df0_like ON public.service_service USING btree (key varchar_pattern_ops);


--
-- Name: service_stateduty_application_id_2548835d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_stateduty_application_id_2548835d ON public.service_stateduty USING btree (application_id);


--
-- Name: service_stateduty_percent_id_9a40d479; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_stateduty_percent_id_9a40d479 ON public.service_stateduty USING btree (percent_id);


--
-- Name: service_stateduty_score_id_3f948ea5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_stateduty_score_id_3f948ea5 ON public.service_stateduty USING btree (score_id);


--
-- Name: service_statedutypercent_car_type_cartype_id_7a0b31ae; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_statedutypercent_car_type_cartype_id_7a0b31ae ON public.service_statedutypercent_car_type USING btree (cartype_id);


--
-- Name: service_statedutypercent_car_type_statedutypercent_id_832830b7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_statedutypercent_car_type_statedutypercent_id_832830b7 ON public.service_statedutypercent_car_type USING btree (statedutypercent_id);


--
-- Name: service_statedutypercent_service_service_id_a40f80b5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_statedutypercent_service_service_id_a40f80b5 ON public.service_statedutypercent_service USING btree (service_id);


--
-- Name: service_statedutypercent_service_statedutypercent_id_0b674262; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_statedutypercent_service_statedutypercent_id_0b674262 ON public.service_statedutypercent_service USING btree (statedutypercent_id);


--
-- Name: service_statedutyscore_district_id_dfa49147; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_statedutyscore_district_id_dfa49147 ON public.service_statedutyscore USING btree (district_id);


--
-- Name: service_statedutyscore_region_id_4e77d9ed; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX service_statedutyscore_region_id_4e77d9ed ON public.service_statedutyscore USING btree (region_id);


--
-- Name: socialaccount_socialaccount_user_id_8146e70c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialaccount_user_id_8146e70c ON public.socialaccount_socialaccount USING btree (user_id);


--
-- Name: socialaccount_socialapp_sites_site_id_2579dee5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialapp_sites_site_id_2579dee5 ON public.socialaccount_socialapp_sites USING btree (site_id);


--
-- Name: socialaccount_socialapp_sites_socialapp_id_97fb6e7d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialapp_sites_socialapp_id_97fb6e7d ON public.socialaccount_socialapp_sites USING btree (socialapp_id);


--
-- Name: socialaccount_socialtoken_account_id_951f210e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialtoken_account_id_951f210e ON public.socialaccount_socialtoken USING btree (account_id);


--
-- Name: socialaccount_socialtoken_app_id_636a42d7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX socialaccount_socialtoken_app_id_636a42d7 ON public.socialaccount_socialtoken USING btree (app_id);


--
-- Name: user_car_body_type_id_21c4537f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_body_type_id_21c4537f ON public.user_car USING btree (body_type_id);


--
-- Name: user_car_color_id_ee091945; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_color_id_ee091945 ON public.user_car USING btree (color_id);


--
-- Name: user_car_device_car_id_b6c8b569; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_device_car_id_b6c8b569 ON public.user_car_device USING btree (car_id);


--
-- Name: user_car_device_device_id_d484cb24; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_device_device_id_d484cb24 ON public.user_car_device USING btree (device_id);


--
-- Name: user_car_fuel_type_car_id_26c11553; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_fuel_type_car_id_26c11553 ON public.user_car_fuel_type USING btree (car_id);


--
-- Name: user_car_fuel_type_fueltype_id_7a4640f7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_fuel_type_fueltype_id_7a4640f7 ON public.user_car_fuel_type USING btree (fueltype_id);


--
-- Name: user_car_history_id_4478bf5d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_history_id_4478bf5d ON public.user_car USING btree (history_id);


--
-- Name: user_car_model_id_68774db0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_model_id_68774db0 ON public.user_car USING btree (model_id);


--
-- Name: user_car_re_color_id_e0ade455; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_re_color_id_e0ade455 ON public.user_car USING btree (re_color_id);


--
-- Name: user_car_re_fuel_type_car_id_c948f05e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_re_fuel_type_car_id_c948f05e ON public.user_car_re_fuel_type USING btree (car_id);


--
-- Name: user_car_re_fuel_type_fueltype_id_c0519d25; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_re_fuel_type_fueltype_id_c0519d25 ON public.user_car_re_fuel_type USING btree (fueltype_id);


--
-- Name: user_car_type_id_04d77292; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_car_type_id_04d77292 ON public.user_car USING btree (type_id);


--
-- Name: user_carmodel_created_user_id_94fba26c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_carmodel_created_user_id_94fba26c ON public.user_carmodel USING btree (created_user_id);


--
-- Name: user_color_created_user_id_3f411bfe; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_color_created_user_id_3f411bfe ON public.user_color USING btree (created_user_id);


--
-- Name: user_district_region_id_0199e8e1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_district_region_id_0199e8e1 ON public.user_district USING btree (region_id);


--
-- Name: user_notification_application_id_b015cd1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_notification_application_id_b015cd1b ON public.user_notification USING btree (application_id);


--
-- Name: user_notification_receiver_id_761ebb04; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_notification_receiver_id_761ebb04 ON public.user_notification USING btree (receiver_id);


--
-- Name: user_notification_sender_id_81a0991b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_notification_sender_id_81a0991b ON public.user_notification USING btree (sender_id);


--
-- Name: user_organization_created_user_id_86c4dcfa; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_organization_created_user_id_86c4dcfa ON public.user_organization USING btree (created_user_id);


--
-- Name: user_organization_legal_address_district_id_1480546f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_organization_legal_address_district_id_1480546f ON public.user_organization USING btree (legal_address_district_id);


--
-- Name: user_organization_legal_address_region_id_ac9cd8b1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_organization_legal_address_region_id_ac9cd8b1 ON public.user_organization USING btree (legal_address_region_id);


--
-- Name: user_quarter_district_id_3f653c9f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_quarter_district_id_3f653c9f ON public.user_quarter USING btree (district_id);


--
-- Name: user_section_district_district_id_72ef3d63; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_section_district_district_id_72ef3d63 ON public.user_section_district USING btree (district_id);


--
-- Name: user_section_district_section_id_6347e1a2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_section_district_section_id_6347e1a2 ON public.user_section_district USING btree (section_id);


--
-- Name: user_section_parent_id_531db2e6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_section_parent_id_531db2e6 ON public.user_section USING btree (parent_id);


--
-- Name: user_section_region_id_d4013886; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_section_region_id_d4013886 ON public.user_section USING btree (region_id);


--
-- Name: user_user_district_id_4fe67f1c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_district_id_4fe67f1c ON public.user_user USING btree (district_id);


--
-- Name: user_user_groups_group_id_c57f13c0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_groups_group_id_c57f13c0 ON public.user_user_groups USING btree (group_id);


--
-- Name: user_user_groups_user_id_13f9a20d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_groups_user_id_13f9a20d ON public.user_user_groups USING btree (user_id);


--
-- Name: user_user_quarter_id_95535c6f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_quarter_id_95535c6f ON public.user_user USING btree (quarter_id);


--
-- Name: user_user_region_id_83df24c6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_region_id_83df24c6 ON public.user_user USING btree (region_id);


--
-- Name: user_user_section_id_2bda3ca4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_section_id_2bda3ca4 ON public.user_user USING btree (section_id);


--
-- Name: user_user_user_permissions_permission_id_ce49d4de; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_user_permissions_permission_id_ce49d4de ON public.user_user_user_permissions USING btree (permission_id);


--
-- Name: user_user_user_permissions_user_id_31782f58; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_user_permissions_user_id_31782f58 ON public.user_user_user_permissions USING btree (user_id);


--
-- Name: user_user_username_e2bdfe0c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX user_user_username_e2bdfe0c_like ON public.user_user USING btree (username varchar_pattern_ops);


--
-- Name: account_emailaddress account_emailaddress_user_id_2c513194_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailaddress
    ADD CONSTRAINT account_emailaddress_user_id_2c513194_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: account_emailconfirmation account_emailconfirm_email_address_id_5b7f8c58_fk_account_e; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account_emailconfirmation
    ADD CONSTRAINT account_emailconfirm_email_address_id_5b7f8c58_fk_account_e FOREIGN KEY (email_address_id) REFERENCES public.account_emailaddress(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_applicationdocumentattachment application_applicat_application_document_d5df8b12_fk_applicati; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocumentattachment
    ADD CONSTRAINT application_applicat_application_document_d5df8b12_fk_applicati FOREIGN KEY (application_document_id) REFERENCES public.application_applicationdocument(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_applicationcashbymoderator application_applicat_application_id_5f3afd45_fk_applicati; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationcashbymoderator
    ADD CONSTRAINT application_applicat_application_id_5f3afd45_fk_applicati FOREIGN KEY (application_id) REFERENCES public.application_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_applicationdocument application_applicat_application_id_fb8da163_fk_applicati; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocument
    ADD CONSTRAINT application_applicat_application_id_fb8da163_fk_applicati FOREIGN KEY (application_id) REFERENCES public.application_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_application application_applicat_created_user_id_af2baa12_fk_user_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_applicat_created_user_id_af2baa12_fk_user_user FOREIGN KEY (created_user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_applicationdocument application_applicat_example_document_id_48f532dc_fk_service_e; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationdocument
    ADD CONSTRAINT application_applicat_example_document_id_48f532dc_fk_service_e FOREIGN KEY (example_document_id) REFERENCES public.service_exampledocument(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_applicationcashbymoderator application_applicat_moderator_id_d0e4f073_fk_user_user; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationcashbymoderator
    ADD CONSTRAINT application_applicat_moderator_id_d0e4f073_fk_user_user FOREIGN KEY (moderator_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_application application_applicat_organization_id_917a8f4a_fk_user_orga; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_applicat_organization_id_917a8f4a_fk_user_orga FOREIGN KEY (organization_id) REFERENCES public.user_organization(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_applicationcashbymoderator application_applicat_paid_state_duty_id_b1c41afc_fk_service_p; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_applicationcashbymoderator
    ADD CONSTRAINT application_applicat_paid_state_duty_id_b1c41afc_fk_service_p FOREIGN KEY (paid_state_duty_id) REFERENCES public.service_paidstateduty(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_application application_applicat_service_id_bfd98186_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_applicat_service_id_bfd98186_fk_service_s FOREIGN KEY (service_id) REFERENCES public.service_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_application application_application_car_id_5c379ac3_fk_user_car_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_application_car_id_5c379ac3_fk_user_car_id FOREIGN KEY (car_id) REFERENCES public.user_car(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_application application_application_inspector_id_85a5b21c_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_application_inspector_id_85a5b21c_fk_user_user_id FOREIGN KEY (inspector_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: application_application application_application_section_id_b8812a68_fk_user_section_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.application_application
    ADD CONSTRAINT application_application_section_id_b8812a68_fk_user_section_id FOREIGN KEY (section_id) REFERENCES public.user_section(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: click_order click_order_service_id_a658b85c_fk_service_service_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.click_order
    ADD CONSTRAINT click_order_service_id_a658b85c_fk_service_service_id FOREIGN KEY (service_id) REFERENCES public.service_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: click_order click_order_user_id_a4619fcc_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.click_order
    ADD CONSTRAINT click_order_user_id_a4619fcc_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_paidstateduty service_paidstatedut_application_id_7ece44a6_fk_applicati; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_paidstateduty
    ADD CONSTRAINT service_paidstatedut_application_id_7ece44a6_fk_applicati FOREIGN KEY (application_id) REFERENCES public.application_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_paidstateduty service_paidstatedut_percent_id_b6bdb667_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_paidstateduty
    ADD CONSTRAINT service_paidstatedut_percent_id_b6bdb667_fk_service_s FOREIGN KEY (percent_id) REFERENCES public.service_statedutypercent(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_paidstateduty service_paidstatedut_score_id_b2b81fac_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_paidstateduty
    ADD CONSTRAINT service_paidstatedut_score_id_b2b81fac_fk_service_s FOREIGN KEY (score_id) REFERENCES public.service_statedutyscore(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_service_document service_service_docu_exampledocument_id_0f212f43_fk_service_e; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service_document
    ADD CONSTRAINT service_service_docu_exampledocument_id_0f212f43_fk_service_e FOREIGN KEY (exampledocument_id) REFERENCES public.service_exampledocument(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_service_document service_service_docu_service_id_e4912b68_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_service_document
    ADD CONSTRAINT service_service_docu_service_id_e4912b68_fk_service_s FOREIGN KEY (service_id) REFERENCES public.service_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_stateduty service_stateduty_application_id_2548835d_fk_applicati; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_stateduty
    ADD CONSTRAINT service_stateduty_application_id_2548835d_fk_applicati FOREIGN KEY (application_id) REFERENCES public.application_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_stateduty service_stateduty_percent_id_9a40d479_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_stateduty
    ADD CONSTRAINT service_stateduty_percent_id_9a40d479_fk_service_s FOREIGN KEY (percent_id) REFERENCES public.service_statedutypercent(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_stateduty service_stateduty_score_id_3f948ea5_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_stateduty
    ADD CONSTRAINT service_stateduty_score_id_3f948ea5_fk_service_s FOREIGN KEY (score_id) REFERENCES public.service_statedutyscore(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_statedutypercent_car_type service_statedutyper_cartype_id_7a0b31ae_fk_user_cart; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_car_type
    ADD CONSTRAINT service_statedutyper_cartype_id_7a0b31ae_fk_user_cart FOREIGN KEY (cartype_id) REFERENCES public.user_cartype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_statedutypercent_service service_statedutyper_service_id_a40f80b5_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_service
    ADD CONSTRAINT service_statedutyper_service_id_a40f80b5_fk_service_s FOREIGN KEY (service_id) REFERENCES public.service_service(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_statedutypercent_service service_statedutyper_statedutypercent_id_0b674262_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_service
    ADD CONSTRAINT service_statedutyper_statedutypercent_id_0b674262_fk_service_s FOREIGN KEY (statedutypercent_id) REFERENCES public.service_statedutypercent(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_statedutypercent_car_type service_statedutyper_statedutypercent_id_832830b7_fk_service_s; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutypercent_car_type
    ADD CONSTRAINT service_statedutyper_statedutypercent_id_832830b7_fk_service_s FOREIGN KEY (statedutypercent_id) REFERENCES public.service_statedutypercent(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_statedutyscore service_statedutyscore_district_id_dfa49147_fk_user_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutyscore
    ADD CONSTRAINT service_statedutyscore_district_id_dfa49147_fk_user_district_id FOREIGN KEY (district_id) REFERENCES public.user_district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: service_statedutyscore service_statedutyscore_region_id_4e77d9ed_fk_user_region_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service_statedutyscore
    ADD CONSTRAINT service_statedutyscore_region_id_4e77d9ed_fk_user_region_id FOREIGN KEY (region_id) REFERENCES public.user_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_social_account_id_951f210e_fk_socialacc; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_social_account_id_951f210e_fk_socialacc FOREIGN KEY (account_id) REFERENCES public.socialaccount_socialaccount(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialtoken socialaccount_social_app_id_636a42d7_fk_socialacc; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialtoken
    ADD CONSTRAINT socialaccount_social_app_id_636a42d7_fk_socialacc FOREIGN KEY (app_id) REFERENCES public.socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialapp_sites socialaccount_social_site_id_2579dee5_fk_django_si; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_site_id_2579dee5_fk_django_si FOREIGN KEY (site_id) REFERENCES public.django_site(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialapp_sites socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialapp_sites
    ADD CONSTRAINT socialaccount_social_socialapp_id_97fb6e7d_fk_socialacc FOREIGN KEY (socialapp_id) REFERENCES public.socialaccount_socialapp(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: socialaccount_socialaccount socialaccount_socialaccount_user_id_8146e70c_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.socialaccount_socialaccount
    ADD CONSTRAINT socialaccount_socialaccount_user_id_8146e70c_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car user_car_body_type_id_21c4537f_fk_user_bodytype_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_body_type_id_21c4537f_fk_user_bodytype_id FOREIGN KEY (body_type_id) REFERENCES public.user_bodytype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car user_car_color_id_ee091945_fk_user_color_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_color_id_ee091945_fk_user_color_id FOREIGN KEY (color_id) REFERENCES public.user_color(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car_device user_car_device_car_id_b6c8b569_fk_user_car_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_device
    ADD CONSTRAINT user_car_device_car_id_b6c8b569_fk_user_car_id FOREIGN KEY (car_id) REFERENCES public.user_car(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car_device user_car_device_device_id_d484cb24_fk_user_device_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_device
    ADD CONSTRAINT user_car_device_device_id_d484cb24_fk_user_device_id FOREIGN KEY (device_id) REFERENCES public.user_device(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car_fuel_type user_car_fuel_type_car_id_26c11553_fk_user_car_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_fuel_type
    ADD CONSTRAINT user_car_fuel_type_car_id_26c11553_fk_user_car_id FOREIGN KEY (car_id) REFERENCES public.user_car(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car_fuel_type user_car_fuel_type_fueltype_id_7a4640f7_fk_user_fueltype_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_fuel_type
    ADD CONSTRAINT user_car_fuel_type_fueltype_id_7a4640f7_fk_user_fueltype_id FOREIGN KEY (fueltype_id) REFERENCES public.user_fueltype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car user_car_history_id_4478bf5d_fk_user_car_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_history_id_4478bf5d_fk_user_car_id FOREIGN KEY (history_id) REFERENCES public.user_car(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car user_car_model_id_68774db0_fk_user_carmodel_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_model_id_68774db0_fk_user_carmodel_id FOREIGN KEY (model_id) REFERENCES public.user_carmodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car user_car_re_color_id_e0ade455_fk_user_color_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_re_color_id_e0ade455_fk_user_color_id FOREIGN KEY (re_color_id) REFERENCES public.user_color(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car_re_fuel_type user_car_re_fuel_type_car_id_c948f05e_fk_user_car_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_re_fuel_type
    ADD CONSTRAINT user_car_re_fuel_type_car_id_c948f05e_fk_user_car_id FOREIGN KEY (car_id) REFERENCES public.user_car(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car_re_fuel_type user_car_re_fuel_type_fueltype_id_c0519d25_fk_user_fueltype_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car_re_fuel_type
    ADD CONSTRAINT user_car_re_fuel_type_fueltype_id_c0519d25_fk_user_fueltype_id FOREIGN KEY (fueltype_id) REFERENCES public.user_fueltype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_car user_car_type_id_04d77292_fk_user_cartype_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_car
    ADD CONSTRAINT user_car_type_id_04d77292_fk_user_cartype_id FOREIGN KEY (type_id) REFERENCES public.user_cartype(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_carmodel user_carmodel_created_user_id_94fba26c_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_carmodel
    ADD CONSTRAINT user_carmodel_created_user_id_94fba26c_fk_user_user_id FOREIGN KEY (created_user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_color user_color_created_user_id_3f411bfe_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_color
    ADD CONSTRAINT user_color_created_user_id_3f411bfe_fk_user_user_id FOREIGN KEY (created_user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_district user_district_region_id_0199e8e1_fk_user_region_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_district
    ADD CONSTRAINT user_district_region_id_0199e8e1_fk_user_region_id FOREIGN KEY (region_id) REFERENCES public.user_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_notification user_notification_application_id_b015cd1b_fk_applicati; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification
    ADD CONSTRAINT user_notification_application_id_b015cd1b_fk_applicati FOREIGN KEY (application_id) REFERENCES public.application_application(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_notification user_notification_receiver_id_761ebb04_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification
    ADD CONSTRAINT user_notification_receiver_id_761ebb04_fk_user_user_id FOREIGN KEY (receiver_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_notification user_notification_sender_id_81a0991b_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_notification
    ADD CONSTRAINT user_notification_sender_id_81a0991b_fk_user_user_id FOREIGN KEY (sender_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_organization user_organization_created_user_id_86c4dcfa_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_organization
    ADD CONSTRAINT user_organization_created_user_id_86c4dcfa_fk_user_user_id FOREIGN KEY (created_user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_organization user_organization_legal_address_distri_1480546f_fk_user_dist; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_organization
    ADD CONSTRAINT user_organization_legal_address_distri_1480546f_fk_user_dist FOREIGN KEY (legal_address_district_id) REFERENCES public.user_district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_organization user_organization_legal_address_region_ac9cd8b1_fk_user_regi; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_organization
    ADD CONSTRAINT user_organization_legal_address_region_ac9cd8b1_fk_user_regi FOREIGN KEY (legal_address_region_id) REFERENCES public.user_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_quarter user_quarter_district_id_3f653c9f_fk_user_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_quarter
    ADD CONSTRAINT user_quarter_district_id_3f653c9f_fk_user_district_id FOREIGN KEY (district_id) REFERENCES public.user_district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_section_district user_section_district_district_id_72ef3d63_fk_user_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section_district
    ADD CONSTRAINT user_section_district_district_id_72ef3d63_fk_user_district_id FOREIGN KEY (district_id) REFERENCES public.user_district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_section_district user_section_district_section_id_6347e1a2_fk_user_section_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section_district
    ADD CONSTRAINT user_section_district_section_id_6347e1a2_fk_user_section_id FOREIGN KEY (section_id) REFERENCES public.user_section(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_section user_section_parent_id_531db2e6_fk_user_section_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section
    ADD CONSTRAINT user_section_parent_id_531db2e6_fk_user_section_id FOREIGN KEY (parent_id) REFERENCES public.user_section(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_section user_section_region_id_d4013886_fk_user_region_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_section
    ADD CONSTRAINT user_section_region_id_d4013886_fk_user_region_id FOREIGN KEY (region_id) REFERENCES public.user_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user user_user_district_id_4fe67f1c_fk_user_district_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_district_id_4fe67f1c_fk_user_district_id FOREIGN KEY (district_id) REFERENCES public.user_district(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_groups user_user_groups_group_id_c57f13c0_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_group_id_c57f13c0_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_groups user_user_groups_user_id_13f9a20d_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_groups
    ADD CONSTRAINT user_user_groups_user_id_13f9a20d_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user user_user_quarter_id_95535c6f_fk_user_quarter_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_quarter_id_95535c6f_fk_user_quarter_id FOREIGN KEY (quarter_id) REFERENCES public.user_quarter(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user user_user_region_id_83df24c6_fk_user_region_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_region_id_83df24c6_fk_user_region_id FOREIGN KEY (region_id) REFERENCES public.user_region(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user user_user_section_id_2bda3ca4_fk_user_section_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user
    ADD CONSTRAINT user_user_section_id_2bda3ca4_fk_user_section_id FOREIGN KEY (section_id) REFERENCES public.user_section(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_user_permissions user_user_user_permi_permission_id_ce49d4de_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permi_permission_id_ce49d4de_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_user_user_permissions user_user_user_permissions_user_id_31782f58_fk_user_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_user_user_permissions
    ADD CONSTRAINT user_user_user_permissions_user_id_31782f58_fk_user_user_id FOREIGN KEY (user_id) REFERENCES public.user_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

