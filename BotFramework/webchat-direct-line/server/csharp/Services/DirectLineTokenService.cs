using System;
using System.Net.Http;
using System.Net.Mime;
using System.Text;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Threading;
using System.Threading.Tasks;
using TokenApi.Models;

namespace TokenApi.Services
{
    public class DirectLineTokenService
    {
        private readonly HttpClient _httpClient;

        public DirectLineTokenService(HttpClient httpClient)
        {
            httpClient.BaseAddress = new Uri("https://directline.botframework.com/");

            _httpClient = httpClient;
        }

        // Calls Direct Line API to generate a Direct Line token
        // Provides user ID in the request body to bind the user ID to the token
        public async Task<DirectLineTokenDetails> GenerateTokenAsync(string directLineSecret, string userId, CancellationToken cancellationToken = default)
        {
            if (String.IsNullOrEmpty(directLineSecret)) throw new ArgumentNullException(nameof(directLineSecret));
            if (String.IsNullOrEmpty(userId)) throw new ArgumentNullException(nameof(userId));

            var fetchTokenRequestBody = new { user = new { id = userId } };

            var fetchTokenRequest = new HttpRequestMessage(HttpMethod.Post, "v3/directline/tokens/generate")
            {
                Headers =
                {
                    { "Authorization", $"Bearer {directLineSecret}" },
                },
                Content = new StringContent(JsonSerializer.Serialize(fetchTokenRequestBody), Encoding.UTF8, MediaTypeNames.Application.Json),
            };

            var fetchTokenResponse = await _httpClient.SendAsync(fetchTokenRequest, cancellationToken);

            if (!fetchTokenResponse.IsSuccessStatusCode)
            {
                throw new InvalidOperationException($"Direct Line token API call failed with status code {fetchTokenResponse.StatusCode}");
            }

            using var responseContentStream = await fetchTokenResponse.Content.ReadAsStreamAsync();
            var tokenApiResponse = await JsonSerializer.DeserializeAsync<DirectLineTokenApiResponse>(responseContentStream);

            return new DirectLineTokenDetails
            {
                Token = tokenApiResponse.Token,
                ExpiresIn = tokenApiResponse.ExpiresIn,
                ConversationId = tokenApiResponse.ConversationId,
            };
        }

        private class DirectLineTokenApiResponse
        {
            [JsonPropertyName("token")]
            public string Token { get; set; }

            [JsonPropertyName("expires_in")]
            public int ExpiresIn { get; set; }

            [JsonPropertyName("conversationId")]
            public string ConversationId { get; set; }
        }
    }
}
