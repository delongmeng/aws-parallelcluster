"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.4.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pcluster_client.api_client import ApiClient, Endpoint as _Endpoint
from pcluster_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pcluster_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from pcluster_client.model.get_image_log_events_response_content import GetImageLogEventsResponseContent
from pcluster_client.model.get_image_stack_events_response_content import GetImageStackEventsResponseContent
from pcluster_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from pcluster_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from pcluster_client.model.list_image_log_streams_response_content import ListImageLogStreamsResponseContent
from pcluster_client.model.not_found_exception_response_content import NotFoundExceptionResponseContent
from pcluster_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent


class ImageLogsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_image_log_events_endpoint = _Endpoint(
            settings={
                'response_type': (GetImageLogEventsResponseContent,),
                'auth': [
                    'aws.auth.sigv4'
                ],
                'endpoint_path': '/v3/images/custom/{imageId}/logstreams/{logStreamName}',
                'operation_id': 'get_image_log_events',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'image_id',
                    'log_stream_name',
                    'region',
                    'next_token',
                    'start_from_head',
                    'limit',
                    'start_time',
                    'end_time',
                ],
                'required': [
                    'image_id',
                    'log_stream_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'image_id',
                ]
            },
            root_map={
                'validations': {
                    ('image_id',): {

                        'regex': {
                            'pattern': r'^[a-zA-Z][a-zA-Z0-9-]+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'image_id':
                        (str,),
                    'log_stream_name':
                        (str,),
                    'region':
                        (str,),
                    'next_token':
                        (str,),
                    'start_from_head':
                        (bool,),
                    'limit':
                        (float,),
                    'start_time':
                        (datetime,),
                    'end_time':
                        (datetime,),
                },
                'attribute_map': {
                    'image_id': 'imageId',
                    'log_stream_name': 'logStreamName',
                    'region': 'region',
                    'next_token': 'nextToken',
                    'start_from_head': 'startFromHead',
                    'limit': 'limit',
                    'start_time': 'startTime',
                    'end_time': 'endTime',
                },
                'location_map': {
                    'image_id': 'path',
                    'log_stream_name': 'path',
                    'region': 'query',
                    'next_token': 'query',
                    'start_from_head': 'query',
                    'limit': 'query',
                    'start_time': 'query',
                    'end_time': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_image_stack_events_endpoint = _Endpoint(
            settings={
                'response_type': (GetImageStackEventsResponseContent,),
                'auth': [
                    'aws.auth.sigv4'
                ],
                'endpoint_path': '/v3/images/custom/{imageId}/stackevents',
                'operation_id': 'get_image_stack_events',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'image_id',
                    'region',
                    'next_token',
                ],
                'required': [
                    'image_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'image_id',
                ]
            },
            root_map={
                'validations': {
                    ('image_id',): {

                        'regex': {
                            'pattern': r'^[a-zA-Z][a-zA-Z0-9-]+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'image_id':
                        (str,),
                    'region':
                        (str,),
                    'next_token':
                        (str,),
                },
                'attribute_map': {
                    'image_id': 'imageId',
                    'region': 'region',
                    'next_token': 'nextToken',
                },
                'location_map': {
                    'image_id': 'path',
                    'region': 'query',
                    'next_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_image_log_streams_endpoint = _Endpoint(
            settings={
                'response_type': (ListImageLogStreamsResponseContent,),
                'auth': [
                    'aws.auth.sigv4'
                ],
                'endpoint_path': '/v3/images/custom/{imageId}/logstreams',
                'operation_id': 'list_image_log_streams',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'image_id',
                    'region',
                    'next_token',
                ],
                'required': [
                    'image_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'image_id',
                ]
            },
            root_map={
                'validations': {
                    ('image_id',): {

                        'regex': {
                            'pattern': r'^[a-zA-Z][a-zA-Z0-9-]+$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'image_id':
                        (str,),
                    'region':
                        (str,),
                    'next_token':
                        (str,),
                },
                'attribute_map': {
                    'image_id': 'imageId',
                    'region': 'region',
                    'next_token': 'nextToken',
                },
                'location_map': {
                    'image_id': 'path',
                    'region': 'query',
                    'next_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_image_log_events(
        self,
        image_id,
        log_stream_name,
        **kwargs
    ):
        """get_image_log_events  # noqa: E501

        Retrieve the events associated with an image build.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_image_log_events(image_id, log_stream_name, async_req=True)
        >>> result = thread.get()

        Args:
            image_id (str): Id of the image.
            log_stream_name (str): Name of the log stream.

        Keyword Args:
            region (str): AWS Region that the operation corresponds to.. [optional]
            next_token (str): Token to use for paginated requests.. [optional]
            start_from_head (bool): If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. (Defaults to 'false'.). [optional]
            limit (float): The maximum number of log events returned. If you don't specify a value, the maximum is as many log events as can fit in a response size of 1 MB, up to 10,000 log events.. [optional]
            start_time (datetime): The start of the time range, expressed in ISO 8601 format (e.g. '2021-01-01T20:00:00Z'). Events with a timestamp equal to this time or later than this time are included.. [optional]
            end_time (datetime): The end of the time range, expressed in ISO 8601 format (e.g. '2021-01-01T20:00:00Z'). Events with a timestamp equal to or later than this time are not included.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetImageLogEventsResponseContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['image_id'] = \
            image_id
        kwargs['log_stream_name'] = \
            log_stream_name
        return self.get_image_log_events_endpoint.call_with_http_info(**kwargs)

    def get_image_stack_events(
        self,
        image_id,
        **kwargs
    ):
        """get_image_stack_events  # noqa: E501

        Retrieve the events associated with the stack for a given image build.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_image_stack_events(image_id, async_req=True)
        >>> result = thread.get()

        Args:
            image_id (str): Id of the image.

        Keyword Args:
            region (str): AWS Region that the operation corresponds to.. [optional]
            next_token (str): Token to use for paginated requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetImageStackEventsResponseContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['image_id'] = \
            image_id
        return self.get_image_stack_events_endpoint.call_with_http_info(**kwargs)

    def list_image_log_streams(
        self,
        image_id,
        **kwargs
    ):
        """list_image_log_streams  # noqa: E501

        Retrieve the list of log streams associated with an image.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_image_log_streams(image_id, async_req=True)
        >>> result = thread.get()

        Args:
            image_id (str): Id of the image.

        Keyword Args:
            region (str): Region that the given image belongs to.. [optional]
            next_token (str): Token to use for paginated requests.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ListImageLogStreamsResponseContent
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['image_id'] = \
            image_id
        return self.list_image_log_streams_endpoint.call_with_http_info(**kwargs)

