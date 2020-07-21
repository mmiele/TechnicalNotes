using System;
using System.Security.Cryptography;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using TokenApi.Models;
using TokenApi.Services;

namespace TokenApi.Controllers
{
    [ApiController]
    public class DirectLineTokenController : ControllerBase
    {
        private readonly DirectLineTokenService _directLineTokenService;
        private readonly IConfiguration _configuration;

        public DirectLineTokenController(DirectLineTokenService directLineTokenService, IConfiguration configuration)
        {
            _directLineTokenService = directLineTokenService;
            _configuration = configuration;
        }

        // Endpoint for generating a Direct Line token bound to a random user ID
        // For simplicity, uses a CORS policy that allows requests from all origins
        // You should restrict this to specific domains
        [HttpPost]
        [Route("/api/direct-line-token")]
        [EnableCors("AllowAllPolicy")]
        public async Task<IActionResult> Post()
        {
            // Generate a random user ID to use for DirectLine token
            var randomUserId = GenerateRandomUserId();

            // Get user-specific DirectLine token and return it
            var directLineSecret = _configuration["DirectLine:DirectLineSecret"];
            DirectLineTokenDetails directLineTokenDetails;
            try
            {
                directLineTokenDetails = await _directLineTokenService.GenerateTokenAsync(directLineSecret, randomUserId);
            }
            catch (InvalidOperationException invalidOpException)
            {
                return BadRequest(new { message = invalidOpException.Message });
            }

            var response = new
            {
                conversationId = directLineTokenDetails.ConversationId,
                token = directLineTokenDetails.Token,
                expiresIn = directLineTokenDetails.ExpiresIn,
                userId = randomUserId,
            };
            return Ok(response);
        }

        // Generates a random user ID
        // Prefixed with "dl_", as required by the Direct Line API
        private static string GenerateRandomUserId()
        {
            byte[] tokenData = new byte[16];
            using var rng = new RNGCryptoServiceProvider();
            rng.GetBytes(tokenData);

            return $"dl_{BitConverter.ToString(tokenData).Replace("-", "").ToLower()}";
        }
    }
}
